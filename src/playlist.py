from playsound3 import playsound
import time

# Onde fica as músicas
playlist = [
    "music/onrepeat.mp3",
    "music/rhythmmagnet.mp3"
]

for musica in playlist:
    print(f"Tocando: {musica}")
    som = playsound(musica, block=False)

    while som.is_alive():
        time.sleep(0.5)

    som.stop()