from fastapi import FastAPI
import psycopg2
import db as db
from typing import List

app = FastAPI()

# get the bank list
@app.get("/banks")
def get_banks():
    conn = db.get_db_conn()
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT name FROM banks ORDER BY name")
    banks = [row[0] for row in cur.fetchall()]
    cur.close()
    conn.close()
    return banks

# get the branch detail using ifsc code

@app.get("/branches/{ifsc}")
def get_branch_details(ifsc: str):
    conn = db.get_db_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM branches WHERE ifsc = %s", (ifsc,))
    branch = cur.fetchone()
    cur.close()
    conn.close()
    return branch

# search for a bank

@app.get("/banks/search")
def search_banks(name: str):
    conn = db.get_db_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM banks WHERE name ILIKE %s ORDER BY name", (f"%{name}%",))
    banks = cur.fetchall()
    cur.close()
    conn.close()
    return banks



# returns the list of branches of that bank

def get_bank_branches_view(bank_name: str):
    conn = db.get_db_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM bank_branches WHERE bank_name ILIKE %s ORDER BY bank_name", (f"%{bank_name}%",))
    branches = cur.fetchall()
    cur.close()
    conn.close()
    return branches

# endpoint to call get_bank_branches_view funciton
@app.get("/banks/{bank_name}/branches_view")
def get_bank_branches_view_endpoint(bank_name: str):
    branches = get_bank_branches_view(bank_name)
    return branches