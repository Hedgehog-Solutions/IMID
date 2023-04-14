import sqlite3

# utworzenie połączenia z bazą danych
conn = sqlite3.connect('test.db')

# utworzenie tabeli variants
conn.execute('''CREATE TABLE IF NOT EXISTS variants
             (variant_id INTEGER PRIMARY KEY AUTOINCREMENT,
              sex TEXT NOT NULL,
              chr TEXT NOT NULL,
              pos TEXT NOT NULL,
              ref TEXT NOT NULL,
              alt TEXT NOT NULL);''')

# utworzenie tabeli variant_columns
conn.execute('''CREATE TABLE IF NOT EXISTS variant_columns 
             (column_id INTEGER PRIMARY KEY AUTOINCREMENT,
              metadata text NOT NULL,
              type TEXT NOT NULL);''')

# utworzenie tabeli versions
conn.execute('''CREATE TABLE IF NOT EXISTS versions 
             (version_id INTEGER PRIMARY KEY AUTOINCREMENT,
              from_date TEXT NOT NULL);''')

# utworzenie tabeli volumn_versions z kluczem obcym na tabelę versions oraz variant_columns
conn.execute('''CREATE TABLE IF NOT EXISTS column_versions
             (version_id INTEGER NOT NULL,
              column_id INTEGER NOT NULL,
              FOREIGN KEY(version_id) REFERENCES versions(version_id),
              FOREIGN KEY(column_id) REFERENCES variant_columns(column_id));''')

# utworzenie tabeli variant_column_values z kluczem obcym na tabelę variants, versions oraz variant_columns
conn.execute('''CREATE TABLE IF NOT EXISTS variant_column_values
             (variant_id INTEGER NOT NULL,
              column_id INTEGER NOT NULL,
              version_id INTEGER NOT NULL,
              value TEXT NOT NULL,
              FOREIGN KEY(variant_id) REFERENCES variant_columns(variant_id),
              FOREIGN KEY(column_id) REFERENCES variant_columns(column_id),
              FOREIGN KEY(version_id) REFERENCES versions(version_id));''')

print("Database created successfully")

# zatwierdzenie zmian
conn.commit()

# zamknięcie połączenia
conn.close()
