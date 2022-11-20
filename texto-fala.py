from gtts import gTTS
from playsound import playsound

audio = "audio.mp3"
language = "de"

sp = gTTS(
    text = "Hallo, vielen Dank für Ihren Besuch auf meinem Profil!",
    lang=language
)

sp.save(audio)
playsound(audio)