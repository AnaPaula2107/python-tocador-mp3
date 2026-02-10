from playsound3 import playsound

# Reproduz o áudio de forma síncrona
playsound("music/onrepeat.mp3")
# Direitos no requirements.txt

# Reproduz o áudio de forma assíncrona
som = playsound("music/onrepeat.mp3", block=False)

if som.is_alive():
    print("Tocando...")

som.stop()