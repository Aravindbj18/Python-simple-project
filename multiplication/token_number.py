
import io
from gtts import gTTS 
from playsound import playsound


# token = input("Enter the token: ")
# txt = " ടോക്കൺ നമ്പർ " + token
# ob = gTTS(txt, lang='ml')
# ob.save("token.mp3")
# playsound("token.mp3")

fp = io.open("book.txt", mode="r", encoding="utf-8")
book_content = fp.read()
ob = gTTS(book_content, lang='ml')
ob.save("book.mp3")
playsound("book.mp3")