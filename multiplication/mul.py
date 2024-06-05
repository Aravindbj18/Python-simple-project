import pyttsx3


n = input("Enter a number: ")

dic ={ 
    "1" : "once",
    "2" : "twice",
    "3" : "Threes",
    "4" : "fourth",
    "5" : "fifth",
    "6" : "sixth",
    "7" : "seventh",
    "8" : "eighth",
    "9" : "nines",
    "10" : "tenth"

}

txt = ""
for i in range(1,11):
    mul = i * int(n)
    txt += str(i) + " "+ dic[n] + " are "+ str(mul) + "\n"

engine = pyttsx3.init()
engine.say(txt)
engine.runAndWait()    
