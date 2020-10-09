# Dichiariamo la somma uguale a 0
somma = 0

# Chiediamo il totale di numeri da sommare tra di loro e lo memorizziamo in n
print("Quanti numeri vuoi sommare?")

# Salviamo l'input come in un intero
n = int(input())

# Chiediamo un nuovo numero tante volte quanto dichiarato precedentemente utilizzando la funzione range
for i in range(n):
    print("Dammi un nuovo numero da sommare")
    nuovo_numero = int(input())
    # Sommiamo il nuovo nummero alla somma parziale
    somma = somma + nuovo_numero

# Stampiamo la somma totale
print("La somma totale e' " + str(somma))