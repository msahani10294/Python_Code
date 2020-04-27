import os
from gtts import gTTS

text_word = "kiske baare me bol rahi ho aarti"

tts = gTTS(text=text_word, lang="en", slow=True)
tts.save("voice3.mp4")

os.system("start voice3.mp4")
