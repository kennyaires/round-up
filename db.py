import os
import psycopg2

from dotenv import load_dotenv

load_dotenv()

con = psycopg2.connect(host=os.environ["DB_HOST"], database=os.environ["DB_NAME"],
user=os.environ["DB_USER"], password=os.environ["DB_PASS"])
cur = con.cursor()
cur.execute('select * from donations')
recset = cur.fetchall()
for rec in recset:
    print (rec)
con.close()