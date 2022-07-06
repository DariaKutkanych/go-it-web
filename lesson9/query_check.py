import sqlite3

query = """SELECT a.id, r.name, b.bd_date, p.number, d.address, e.email FROM addressbook as a
           LEFT JOIN record AS r ON a.id = r.book_id
           LEFT JOIN birthday AS b ON r.id = b.user_id
           LEFT JOIN phone AS p ON r.id = p.user_id
           LEFT JOIN address AS d ON r.id = d.user_id
           LEFT JOIN email AS e ON r.id = e.user_id
           GROUP BY a.id, r.name, b.bd_date, p.number, d.address, e.email
           """

with sqlite3.connect("helper.db") as con:
    cur = con.cursor()
    result = cur.execute(query)

for row in result:
    print(row)