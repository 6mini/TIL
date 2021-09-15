import psycopg2

conn = psycopg2.connect(
    host="chunee.db.elephantsql.com",
    database="fqislexi",
    user="fqislexi",
    password="6pgNvWfm3XLnJK_t0dsyph8i1GnIMx_T")

print(conn)

cur.execute("""CREATE TABLE test_table (
				        name VARCHAR(32),
				        age INT);
			      """)

cur.execute("INSERT INTO test_table (name, age) VALUES ('spongebob', 12);")

name = 'banana'
age = 13

cur.execute("INSERT INTO test_table (name, age) VALUES (%s, %s)",(name,age))

conn.commit()