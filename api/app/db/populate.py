import psycopg2
import pandas as pd


def get_stable_columns(cursor):
    variants_atr = list()
    cursor.execute("""SELECT column_name
                    FROM information_schema.columns
                    WHERE table_name = 'variants'""")
    for row in cursor:
        variants_atr.append(row[0])
    return variants_atr


def get_attributes(cursor):
    variants_metadata = list()
    cursor.execute("SELECT metadata FROM variant_columns")
    for row in cursor:
        variants_metadata.append(row[0])
    return variants_metadata


def get_attributes_in_version(cursor, version):
    variants_metadata = list()
    cursor.execute("""SELECT col.metadata
                    FROM variant_column_values val 
                    JOIN versions ver ON(val.version_id = ver.version_id)
                    JOIN variant_columns col ON(val.column_id = col.column_id)
                    WHERE ver.version_id = %s
                    GROUP BY col.metadata""", (version,))
    for row in cursor:
        variants_metadata.append(row[0])
    return variants_metadata


def create_view(host, database, user, password, version):
    # version = 1
    sql_query = "CREATE MATERIALIZED VIEW IF NOT EXISTS variants_view AS SELECT "
    sql_from = "FROM Variant_column_values val JOIN variant_columns col ON(val.column_id = col.column_id) JOIN versions ver ON(val.version_id = ver.version_id) JOIN variants var ON(val.variant_id = var.variant_id) "
    sql_where = "WHERE ver.version_id = " + str(version) + " "
    sql_group_by = "GROUP BY "
    sql_order_by = "ORDER BY var.variant_id; "

    conn = psycopg2.connect(
        host=host,
        database=database,
        user=user,
        password=password)
    
    cursor = conn.cursor()

    # wczytanie wszystkich stałych atrybutów variants
    variants_atr = get_stable_columns(cursor)
    for var in variants_atr:
        sql_query = sql_query + "var." + str(var) + ', '
        sql_group_by = sql_group_by + "var." + str(var) + ', '
    sql_group_by = sql_group_by[:-2] + ' '

    # wczytanie wszystkich aktualnych metadanych z variant_columns
    variants_metadata = get_attributes_in_version(cursor, version)
    for var in variants_metadata:
        sql_query = sql_query + "MAX(CASE WHEN col.metadata = '" + str(var) + "' THEN value ELSE '-' END) AS " + '"' + str(var) + '"' + ", "
    sql_query = sql_query[:-2] + ' '

    sql_query = sql_query + sql_from + sql_where + sql_group_by + sql_order_by
    cursor.execute(sql_query)
    conn.commit()

    cursor.close()
    conn.close()


def populate(host, database, user, password, data_name, datetime):

    df = pd.read_csv(data_name, sep="\t", index_col=0)
    df = df.rename(columns=lambda x: x.lower())

    # utworzenie połączenia z bazą danych
    conn = psycopg2.connect(
        host=host,
        database=database,
        user=user,
        password=password)
    
    cursor = conn.cursor()

    # wczytanie wszystkich stałych atrybutów variants
    variants_atr = get_stable_columns(cursor)

    # wczytanie wszystkich aktualnych metadanych z variant_columns
    variants_metadata = get_attributes(cursor)

    cursor.execute("INSERT INTO versions (from_date) VALUES (%s) "
                   "RETURNING version_id", (datetime, ))

    version = cursor.fetchone()[0]

    i = 0 #TODO TEMP
    for index, row in df.iterrows():
        i = i+1

        cursor.execute('''INSERT INTO variants (sex, chr, pos, ref, alt) 
                    VALUES (%s, %s, %s, %s, %s) RETURNING variant_id''', (row['sex'], row['chr'], row['pos'], row['ref'], row['alt']))

        variant_id = cursor.fetchone()[0]
        print(variant_id) #TODO TEMP

        values = []
        for column in df.columns:

            if column not in variants_atr:
                if column not in variants_metadata:
                    cursor.execute('''INSERT INTO variant_columns (metadata, type)
                                 VALUES (%s, %s)''', (column, "object"))
                    variants_metadata.append(column)
                
                cursor.execute("SELECT column_id FROM variant_columns WHERE metadata = %s",(column, ))
                column_id = cursor.fetchone()[0]
                
                val = (variant_id, column_id, version, row[column])
                values.append(val)

        cursor.executemany('''INSERT INTO variant_column_values (variant_id, column_id, version_id, value)
                              VALUES (%s, %s, %s, %s)''', values)
                
        #TODO TEMP
        if i > 50:
            break

    print("Database populated successfully")
            
    conn.commit()

    cursor.close()
    conn.close()


if __name__ == '__main__':

    host=" "
    database=" "
    user=" "
    password=" "
    version = 3

    file_path = "RG-corriell_S7_VEP.tsv"
    # populate(host, database, user, password, file_path, version)
#    create_view(host, database, user, password, version)
