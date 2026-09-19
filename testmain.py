# A simple script for calling functions in isolation.
import data_management
import sys, sqlite3

def main():

    con = data_management.open_create_db("test.db")
    cur = con.cursor()
    res = cur.execute("SELECT * FROM transactions")
    print(res.fetchall())
    return

main()