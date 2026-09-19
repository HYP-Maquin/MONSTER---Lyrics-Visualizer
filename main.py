#Full code coming soon...
import time 

lyrics = [
    ("ciao 1", 0.1, 0.3),
    ("ciao 2", 0.2, 0.4)
]

for testo, tempo, pausa in lyrics:
    for lettere in testo:
        print(lettere, end="", flush = True)
        time.sleep(tempo)
    print()
    time.sleep(pausa)
