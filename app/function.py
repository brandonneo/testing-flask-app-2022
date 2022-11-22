from app import db, app

from app.db_connect import connect

def get_roles(roles_id):
    conn = connect()
    with conn.cursor() as cur:
        sql = f'SELECT * FROM user where id ={roles_id}'
        cur.execute(sql)
        return cur.fetchall()