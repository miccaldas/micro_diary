from mysql.connector import connect, Error
import urwid


def exit_on_q(key):
    if key in ('q', 'Q'):
        raise urwid.ExitMainLoop()


def see():
    try:
        conn = connect(
                host="localhost",
                user="mic",
                password="xxxx",
                database="micro_diary")
        cur = conn.cursor()
        query = 'SELECT COUNT(*) FROM micro_diary'
        cur.execute(query,)
        row = cur.fetchone()
        print(row)
        result = str(row)
        result = result[1:-2]
        print(result)
    except Error as e:
        print("Error while connecting to db", e)
    finally:
        if(conn):
            conn.close()


if __name__ == '__main__':
    see()