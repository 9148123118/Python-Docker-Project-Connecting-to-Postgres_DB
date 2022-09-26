import psycopg2

#connect to the db 
con = psycopg2.connect(
            host = "localhost",
            database="postgres",
            user = "postgres",
            password = "postgres")

#cursor 
cur = con.cursor()

# cur.execute("insert into employees (id, name) values (%s, %s)", (1, "Hussein") )

# #execute query
cur.execute("select id, name from student")

rows = cur.fetchall()

for r in rows:
    print (f"id {r[0]} name {r[1]}")

#commit the transcation 
con.commit()

#close the cursor
cur.close()

#close the connection
con.close()