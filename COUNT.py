import mysql.connector as mc
conn = mc.connect(host='localhost', user='Chris', password='C123456789.', db='menagerie')
c = conn.cursor()


def COUNT():
    c.execute('SELECT owner, COUNT(*) FROM pet GROUP BY owner')
    pets = c.fetchall()
    for pet in pets:
        print(pet)


def main():
    COUNT()

if __name__ == '__main__':
    main()