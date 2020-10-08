# Importiamo la funzione randrange dal modulo random
from random import randrange

# Utilizziamo la funzione randrange per assegnare un numero casuale da 1 a 9
lato = randrange(1,9)

# Stampiamo il lato e utilizziamo la funzione str per convertire l'intero in una stringa
print("lato=" + str(lato))

# Calcoliamo l'area del quadrato
area = lato * lato

# Stampiamo la domanda e memorizziamo la risposta da input
print("Qual e' l'area del quadrato di lato " + str(lato) + "?")

risposta = input()

while(risposta != area):
    # Se la risposta e' diversa dall'area calcolata
    # Ripetiamo la domanda e sovrascriviamo la risposta finche' non e' inserita la risposta corretta
    print("Risposta sbagliata.")

    print("Qual e' l'area del quadrato di lato " + str(lato) + "?")

    risposta = input()

print("Bene! Risposta giusta.")
