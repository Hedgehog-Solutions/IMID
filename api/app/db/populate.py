import sqlite3
import psycopg2
import pandas as pd


def populate(host, database, user, password, data_name):

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
    variants_atr = list()
    cursor.execute("""SELECT column_name
                    FROM information_schema.columns
                    WHERE table_name = 'variants'""")
    for row in cursor:
        variants_atr.append(row[0])

    # wczytanie wszystkich aktualnych metadanych z variant_columns
    variants_metadata = list()
    cursor.execute("SELECT metadata FROM variant_columns")
    for row in cursor:
        variants_metadata.append(row)

    cursor.execute("INSERT INTO versions (version_id, from_date) VALUES (1, '14.04.2023')",)

    i = 0 #TODO TEMP
    for index, row in df.iterrows():
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
                
                val = (variant_id, column_id, 1, row[column])
                values.append(val)

        cursor.executemany('''INSERT INTO variant_column_values (variant_id, column_id, version_id, value)
                              VALUES (%s, %s, %s, %s)''', values)
                
        #TODO TEMP
        i = i+1
        if i > 50:
            break

    print("Database populated successfully")
            
    conn.commit()

    cursor.close()
    conn.close()


# if __name__ == '__main__':

#     file_path = "RG-corriell_S7_VEP.tsv"
#     populate(host, database, user, password, file_path)
