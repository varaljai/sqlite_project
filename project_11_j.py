import sqlite3
with open("periodusos_rendszer.txt") as elem:
    lista = [sor.strip().split("\t") for sor in elem]
    
print(lista)

con = sqlite3.connect("adatok.db")
cor = con.cursor()

