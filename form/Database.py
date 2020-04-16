import sqlite3
def connexion():
    conn = sqlite3.connect('../config/santeplus.db')
    cursor = conn.cursor()
    return conn, cursor

def close_db(conn):
    conn.commit()
    conn.close()

if __name__ == '__main__':
    conx,cur = connexion()
    close_db(conx)
