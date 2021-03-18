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
        query = "SELECT * FROM micro_diary"
        cur.execute(query,)
        records = cur.fetchall()
        records = str(records)
        for row in records:
            txt = urwid.Text(('banner', '%s' % (row[0])), align='center')
            fill = urwid.Filler(txt)
            loop = urwid.MainLoop(fill, unhandled_input=exit_on_q)
            loop.run()

    except Error as e:
        print("Error while connecting to db", e)
    finally:
        if(conn):
            conn.close()


if __name__ == '__main__':
    see()
