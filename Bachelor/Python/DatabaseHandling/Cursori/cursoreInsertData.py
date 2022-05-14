import mysql.connector as ms
import numpy as np 
from faker import Faker  


def fetchCompanyData(cursore, connessione):

    companyData = []

    query = "SELECT nome_azienda from azienda"   # Table --> azienda, Attributo --> nome_azienda

    cursore.execute(query)
    result = cursore.fetchall()
    
    return result


def formatData(Data = []):

    formattedData = []

    for i in Data:
        formattedData.append(i[0])

    return formattedData



def generaNomeAzienda():
    faker = Faker()
    nome = faker.company()
    while True:
        if len(nome) <= 32:   # nella CREATE TABLE il campo "nome_azienda" e' un VARCHAR(32)
            break
        nome = faker.company()
    return nome

def generaIntero(low = 1, high = 15):
    return np.random.randint(low, high)  # ritorna un intero nel range [low, high-1]



# numberOfRecords e' il numero di record che si vogliono inserire
def addData(cursore, connessione, numberOfRecords = 50):

    companyData = fetchCompanyData(cursore, connessione)

    formattedCompanyData = formatData(companyData)
    inUseKeyData = formattedCompanyData[:]    # lista per tenere traccia dei nomi usati e non usarli piu' volte dato che sono chiavi
    
    
    # nota: anche per interi va bene usare il formatting %s delle stringhe, ci pensa MySQL a fare il casting tra tipi
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

    connessione.commit()   # conferma le modifiche


def connect(hostName = 'localhost', userName = 'root', databaseName = 'prova'):
    passwd = input('Inserisci la password per utente ' + userName + ': ')
    connessione = ms.connect(host = hostName, user = userName, database = databaseName, password = passwd)
    cursore = connessione.cursor()

    cursore.execute('USE ' + databaseName)

    addData(cursore, connessione)


if __name__ == '__main__':
    connect()
