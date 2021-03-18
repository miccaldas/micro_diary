from mysql.connector import connect, Error


def connections():
    f = open('post.txt', 'r')
    f_tags = open('tags.txt', 'r')

    post_content = f.read()
    tags_content = f_tags.read()

    try:
        conn = connect(
                host="localhost",
                user="mic",
                password="xxxx",
                database="micro_diary")
        cur = conn.cursor()
        answers = [post_content, tags_content]
        query = """ INSERT INTO micro_diary (text, tags) VALUES (%s, %s) """
        cur.execute(query, answers)
        conn.commit()
    except Error as e:
        print("Error while connecting to db", e)
    finally:
        if(conn):
            conn.close()

    f.close()
    f_tags.close()


if __name__ == '__main__':
    connections()
