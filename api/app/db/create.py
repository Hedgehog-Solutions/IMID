import sqlite3
import psycopg2

def create(host, database, user, password):

    # utworzenie połączenia z bazą danych
    # conn = sqlite3.connect(db_name)
    conn = psycopg2.connect(
        host=host,
        database=database,
        user=user,
        password=password)
    
    cur = conn.cursor()

    cur.execute('''DROP TABLE IF EXISTS variant_column_values''')
    cur.execute('''DROP TABLE IF EXISTS column_versions''')
    cur.execute('''DROP TABLE IF EXISTS versions''')
    cur.execute('''DROP TABLE IF EXISTS variant_columns''')
    cur.execute('''DROP TABLE IF EXISTS variants''')
    
    # utworzenie tabeli variants
    cur.execute('''CREATE TABLE IF NOT EXISTS variants
                 (variant_id SERIAL PRIMARY KEY,
                  sex TEXT NOT NULL,
                  chr TEXT NOT NULL,
                  pos TEXT NOT NULL,
                  ref TEXT NOT NULL,
                  alt TEXT NOT NULL);''')

    # utworzenie tabeli variant_columns
    cur.execute('''CREATE TABLE IF NOT EXISTS variant_columns 
                 (column_id SERIAL PRIMARY KEY,
                  metadata text NOT NULL,
                  type TEXT NOT NULL);''')

    # utworzenie tabeli versions
    cur.execute('''CREATE TABLE IF NOT EXISTS versions 
                 (version_id SERIAL PRIMARY KEY,
                  from_date TEXT NOT NULL);''')

    # utworzenie tabeli volumn_versions z kluczem obcym na tabelę versions oraz variant_columns
    cur.execute('''CREATE TABLE IF NOT EXISTS column_versions
                 (version_id INTEGER NOT NULL,
                  column_id INTEGER NOT NULL,
                  FOREIGN KEY(version_id) REFERENCES versions(version_id),
                  FOREIGN KEY(column_id) REFERENCES variant_columns(column_id));''')

    # utworzenie tabeli variant_column_values z kluczem obcym na tabelę variants, versions oraz variant_columns
    cur.execute('''CREATE TABLE IF NOT EXISTS variant_column_values
                 (variant_id INTEGER NOT NULL,
                  column_id INTEGER NOT NULL,
                  version_id INTEGER NOT NULL,
                  value TEXT NOT NULL,
                  FOREIGN KEY(variant_id) REFERENCES variants(variant_id),
                  FOREIGN KEY(column_id) REFERENCES variant_columns(column_id),
                  FOREIGN KEY(version_id) REFERENCES versions(version_id));''')

    print("Database created successfully")

    # zatwierdzenie zmian
    conn.commit()

    # zamknięcie połączenia
    cur.close()
    conn.close()

# if __name__ == '__main__':
#     create('test.db')
