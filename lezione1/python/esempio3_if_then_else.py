print("Dimmi un numero")

# "Prendo" la risposta attraverso un azione di ingresso input()
numero = input()

# Uso l'operatore % per ottenere il resto della divisione numero/2
# Confronto il resto della divisione per verificare che sia uguale (==) 0
if(numero%2==0):
    # Se il resto e' uguale a 0 il numero e' pari
    print("Il numero inserito e' pari!")
else:
    # Altrimenti sara' dispari
    print("Il numero inserito e' dispari!")

print("Fine del programma.")