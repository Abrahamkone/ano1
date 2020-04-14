# import sqlite3
#
# def connexion():
#     try:
#         conn = sqlite3.connect('../config/santeplus.db')
#     except Exception as e:
#         print(e)
#     cursor = conn.cursor()
#     return conn, cursor
#
# def close_db(conn):
#     conn.commit()
#     conn.close()
#
# if __name__ == '__main__':
#     conx,cur = connexion()
#     close_db(conx)
