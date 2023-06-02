import mysql.connector as mc
conn = mc.connect(host='localhost', user='Chris', password='C123456789.', db='menagerie')
c = conn.cursor()


def show_data():
    c.execute('SELECT name, birth, MONTH(birth) FROM pet')
    months = c.fetchall()
    for month in months:
        print(month)


def main():
    show_data()


if __name__ == '__main__':
    main()