from hangman_pics import hangman
import random

def guess_word():
    word = random.choice(words)
    print("Guess the fruet")
    return word

def is_present(letter):
    if letter.lower() in word.lower():#letter lover #comp guess word full lower
        return letter.lower()
    else: 
        return False

def fill_blank(letter):
    global display_dash,word
    display_dash = list(display_dash)#change string to list
    for i,l in enumerate(word):# enumerate = index and letter to got it
        if letter == l:
            display_dash[i]=letter
    print("".join(display_dash))        #list to convert join
def make_hangman():
    global chances
    chances +=1  #to the fist wrong guess the chances was 1 --to repeat wrong answer....updates
    print(hangman[chances])

def check_letter(user_choice):# when user enters singel letters
    letter = is_present(user_choice)
    if letter:
        fill_blank(letter)
    else:
        make_hangman()    

def check_word(user_choice): #wen user enters full word
    if user_choice.lower() == word.lower():
        return True
    else:
        return False


#initial setup
chances = 0
is_win = False
words =['apple','orange','kiwi','watermelon','plum','banana','strawberry']
word = guess_word()
display_dash = ('_' * len(word))
print(display_dash)
print(hangman[0])

#main loop

while chances <= 5 and not is_win:
    user_choice = input()
    if len(user_choice)==1:
        #define function(arguement)
        check_letter(user_choice)
    else:
        is_win = check_word(user_choice)# another function(arguement user_choice)
        break

    if '_' not in display_dash:# inside the global string not any dashes
        is_win = True




if is_win:
    print("Win")
else:
    print("Lost")    