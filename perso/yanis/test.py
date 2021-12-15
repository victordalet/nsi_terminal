import sqlite3
    
conn = sqlite3.connect('baseDonnees.db')
cur = conn.cursor()

cur.execute("CREATE TABLE CLIENTS IF NOT EXISTS(idClients)")
cur.execute("CREATE TABLE GENRE IF NOT EXISTS(idGenre)")
cur.execute("CREATE TABLE FIL IF NOT EXISTS(idFilm, idGenre)")

conn.commit()

cur.close()
conn.close()
