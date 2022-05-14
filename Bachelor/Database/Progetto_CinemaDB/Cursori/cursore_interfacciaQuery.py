import mysql.connector as ms

def eseguiQuery(cursore):

    query = ""
    
    while True:

        query = input('Inserisci la query che vorresti eseguire: ')

        if query in ("exit", "Exit", "logout", "Logout", "quit", "Quit", "q", "Q"):
            print('Bye!')
            break
        
        cursore.execute(query)
        result = cursore.fetchall()

        for row in result:
            print(row, '\n')

def connect(hostName = 'localhost', userName = 'root', databaseName = 'cinemadb'):
    passwd = input('Inserisci la password per utente ' + userName + ': ')
    connessione = ms.connect(host = hostName, user = userName, database = databaseName, password = passwd)
    cursore = connessione.cursor()

    cursore.execute('USE ' + databaseName)

    eseguiQuery(cursore)


if __name__ == '__main__':
    connect()

