import numpy as np 
import random
import names   # pip install names
from faker import Faker  # pip install Faker


def generaNomeCompleto():
    return names.get_full_name()

def generaNome():
    return names.get_first_name()

def generaCognome():
    return names.get_last_name()



def generaIntero(low = 1, high = 11):
    return np.random.randint(low, high)  # ritorna un intero nel range [low, high-1]

# 'start' ed 'end' indicano il range in cui verra' estratto il numero, di default e' tra 0 ed 1
# 'rounded' indica il numero di cifre decimali cui verra' arrotondato il numero, di default e' 2
def generaFloat(start = 0, end = 1, rounded = 2):
    return round(random.uniform(start, end), rounded)


# NOTA: adattare la lunghezza delle stringhe generate al massimo numero di caratteri dell'attributo nelle tabelle
def generaIndirizzo():
    faker = Faker()
    indirizzo = faker.street_address()
    while True:
        if len(indirizzo) <= 32:
            break
        indirizzo = faker.street_address()
    return indirizzo

def generaNomeAzienda():
    faker = Faker()
    nome = faker.company()
    while True:
        if len(nome) <= 32:
            break
        nome = faker.company()
    return nome

def generaNumeroTelefono():   
    faker = Faker()
    number = ''
    while(len(number) != 10):
        number = faker.phone_number()
    return number   # ritorna numero di telefono a 10 cifre

def generaNomeCitta():
    faker = Faker()
    citta = faker.city()
    while True:
        if len(citta) <= 24:
            break
        citta = faker.city()
    return citta   # di default genera nomi di citta' en-us





