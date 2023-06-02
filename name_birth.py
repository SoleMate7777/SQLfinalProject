import mysql.connector as mc
conn = mc.connect(host='localhost', user='Chris', password='C123456789.', db='menagerie')
c = conn.cursor()


def show_data():
    c.execute('SELECT name, birth FROM pet')
    pets = c.fetchall()
    for pet in pets:
        print(pet)


def main():
    show_data()

if __name__ == '__main__':
    main()