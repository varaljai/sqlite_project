import sqlite3
with open("periodusos_rendszer.txt") as elem:
    lista = [sor.strip().split(",") for sor in elem]


con = sqlite3.connect("adatok.db")
cur = con.cursor()

cur.execute("CREATE TABLE periodusos_tabla(AtomicNumber INT, Element TEXT, Symbol TEXT, AtomicMass FLOAT)")

cur.executemany("INSERT INTO periodusos_tabla VALUES(?,?,?,?)", lista)
con.commit()

print(lista)

