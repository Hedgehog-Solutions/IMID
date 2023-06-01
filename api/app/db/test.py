import sqlite3
import psycopg2


def test(host, database, user, password):

    # utworzenie połączenia z bazą danych
    conn = psycopg2.connect(
        host=host,
        database=database,
        user=user,
        password=password)

    cursor = conn.cursor()

    cursor.execute(f"SELECT chr FROM variants")
    rows = cursor.fetchall()
    print("kilka wartosci chr")
    print(f"wartosc 25: {rows[2]}")
    print(f"wartosc 125: {rows[5]}")
    print(f"wartosc 1225: {rows[25]}")

    print()

    cursor.execute('''SELECT v3.metadata, v2.value 
                             FROM variants v1 
                             JOIN variant_column_values v2 ON(v1.variant_id = v2.variant_id)
                             JOIN variant_columns v3 ON(v2.column_id = v3.column_id)
                             WHERE v1.variant_id = 3''')
    print("wartosci variantów uzytkowinika z id = 3")
    for metadata, value in cursor:
        print(f"{metadata}\t: {value}")

    cursor.close()
    conn.close()


# if __name__ == '__main__':
#     test(host, database, user, password)
