import sqlite3
import pandas as pd


def populate(db_name, data_name):

    df = pd.read_csv(data_name, sep="\t", index_col=0)
    df = df.rename(columns=lambda x: x.lower())

    # utworzenie połączenia z bazą danych
    conn = sqlite3.connect(db_name)

    # wczytanie wszystkich stałych atrybutów variants
    variants_atr = list()
    cursor = conn.execute("PRAGMA table_info(variants)")
    for row in cursor:
        variants_atr.append(row[1])

    # wczytanie wszystkich aktualnych metadanych z variant_columns
    variants_metadata = list()
    cursor = conn.execute("SELECT metadata FROM variant_columns")
    for row in cursor:
        variants_metadata.append(row)
        
    conn.execute("INSERT INTO versions (version_id, from_date) VALUES (1, '14.04.2023')",)


    for index, row in df.iterrows():
        conn.execute(f'''INSERT INTO variants (sex, chr, pos, ref, alt) 
                         VALUES ("{row['sex']}", "{row['chr']}", "{row['pos']}", "{row['ref']}", "{row['alt']}")''')
        variant_id = conn.execute("SELECT last_insert_rowid()").fetchone()[0]
        
        for column in df.columns:
            if column not in variants_atr:
                if column not in variants_metadata:
                    conn.execute(f'''INSERT INTO variant_columns (metadata, type)
                                 VALUES ("{column}", "object")''')
                    variants_metadata.append(column)
                
                column_id = conn.execute(f"SELECT column_id FROM variant_columns WHERE metadata = '{column}'").fetchone()[0]
                
                conn.execute(f'''INSERT INTO variant_column_values (variant_id, column_id, version_id, value)
                                 VALUES ({variant_id}, {column_id}, 1, "{row[column]}")''')
            
    print("Database populated successfully")
            
    conn.commit()

    conn.close()


if __name__ == '__main__':
    populate('test.db', 'RG-corriell_S7_VEP.tsv')
