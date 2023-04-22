import sqlite3


def test(db_name):

    # utworzenie połączenia z bazą danych
    conn = sqlite3.connect('test.db')

    cursor = conn.execute(f"SELECT chr FROM variants").fetchall()
    print("kilka wartosci chr")
    print(f"wartosc 25: {cursor[25]}")
    print(f"wartosc 125: {cursor[125]}")
    print(f"wartosc 1225: {cursor[1225]}")

    print()

    cursor = conn.execute('''SELECT v3.metadata, v2.value 
                             FROM variants v1 
                             JOIN variant_column_values v2 ON(v1.variant_id = v2.variant_id)
                             JOIN variant_columns v3 ON(v2.column_id = v3.column_id)
                             WHERE v1.variant_id = 3''').fetchall()
    print("wartosci variantów uzytkowinika z id = 3")
    for metadata, value in cursor:
        print(f"{metadata}\t: {value}")


    conn.close()


if __name__ == '__main__':
    test('test.db')
