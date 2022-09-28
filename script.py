from multiprocessing import connection
import psycopg2
from flask import Flask
app = Flask(__name__)
  
@app.route('/')
def hello():
    return "Hi, Welcome to Python project"
  
#connect to the db 
con = psycopg2.connect(
            host = "postgres_c",
            database="postgres",
            user = "postgres",
            password = "postgres")

#cursor q
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

if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 5001, debug = True) 
