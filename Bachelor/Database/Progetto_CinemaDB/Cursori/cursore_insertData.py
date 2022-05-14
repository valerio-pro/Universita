import mysql.connector as ms
import numpy as np 
from faker import Faker  


def generaNomeAzienda():
    faker = Faker()
    nome = faker.company()
    while True:
        if len(nome) <= 32:
            break
        nome = faker.company()
    return nome

def generaIntero(low = 1, high = 15):
    return np.random.randint(low, high)     # ritorna un intero nel range [low, high-1]



def fetchCompanyData(cursore, connessione):

    companyData = []

    query = "SELECT nome_azienda from azienda"

    cursore.execute(query)
    result = cursore.fetchall()
    
    return result


def formatData(Data = []):

    formattedData = []

    for i in Data:
        formattedData.append(i[0])

    return formattedData






def addData(cursore, connessione, numberOfRecords = 50):

    companyData = fetchCompanyData(cursore, connessione)

    formattedCompanyData = formatData(companyData)
    inUseKeyData = formattedCompanyData[:]

    query = "INSERT INTO azienda VALUES (%s, %s, %s)"

    for i in range(numberOfRecords):
        nome = generaNomeAzienda()
        if nome not in inUseKeyData:
            inUseKeyData.append(nome)
        else:
            continue
        year = generaIntero(1902, 2005)
        net_worth = generaIntero(320000, 2147483646)
        data = (nome, year, net_worth)
        
        cursore.execute(query, data)

    connessione.commit()


def connect(hostName = 'localhost', userName = 'root', databaseName = 'cinemadb'):
    passwd = input('Inserisci la password per utente ' + userName + ': ')
    connessione = ms.connect(host = hostName, user = userName, database = databaseName, password = passwd)
    cursore = connessione.cursor()

    cursore.execute('USE ' + databaseName)

    addData(cursore, connessione)


if __name__ == '__main__':
    connect()
