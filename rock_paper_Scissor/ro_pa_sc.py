#make rock paper scissor game.....

# 1. we need to give player name as input..
# 2. we will ask how many rounds would you likke to play ?
  # 3 rounds/ 5 /7/ 9(This should be an odd number )
  # So we can derieve a winner...

# 3. Make a function to generate random computer input, Rock Paper Scissor...

# 4. Make a function to take player input out of , R= Rock, P= Paper , S= Scissor....
# 5. Check who is winning in a specific round
# 6. Somehow record the score of the game..
# 7. Repeat everything until there is a winner..
#-------------------------------------------------------
# name = input("Please enter your name: ")
# text_promt ="Hey "+ name + " How maney rounds would you like to play ? :"
# Rule no 1 is the input should be an ODD number..
# rule no 2 is it should be greater than 2 and less than 10..
#if these two rules are not satisfied than ask again...
flag = True
# The flag will true the loop will run again & again &again ....etc
def take_rounds_input(name):
    text_promt ="Hey "+ name + " How maney rounds would you like to play ? :"
    while True:
      rounds = int(input(text_promt))
                                        #Rule 1
      if rounds%2 == 1:
        
                                         #Rule 2
        if rounds > 2 and rounds < 10:
          return rounds
          
                                         # If we get perfect number the flag will false..
          break
        else:
          print("Your number is not the range of 3 to 9, please enter again")    
      else:
        print(" No its a even number , Please enter again : ")   

#step 3 -generate a random selection R/P/S
import random
def give_me_a_computer_choice():
  option_list =('rock','paper','scissor')
  return random.choice(option_list)
give_me_a_computer_choice()
# step 4-  Take player input out of Rock paper scissor
def give_me_a_player_option():
  option = input("R=Rock, P=Paper, S = scissor")
  if option == 'R' or option == 'r':
    return 'rock'
  elif option == 'P' or option == 'p':
    return 'paper'
  elif option == 'S' or option == 's':
    return 'scissor'
  else:
    return give_me_a_player_option()
def check_who_is_winning(computer_input, player_input):
  if player_input == 'scissor' and computer_input == 'scissor':
    return 'draw'
  elif player_input == 'rock' and computer_input == 'scissor':
    return 'player'
  elif player_input == 'paper' and computer_input == 'scissor':
    return 'computer'
  elif player_input == 'scissor' and computer_input == 'rock':
    return 'computer'
  elif player_input == 'rock' and computer_input == 'rock':
    return 'draw'
  elif player_input == 'paper' and computer_input == 'rock':
    return 'player'
  elif player_input == 'scissor' and computer_input == 'paper':
    return 'player'
  elif player_input == 'rock' and computer_input == 'paper':
    return 'computer'
  elif player_input == 'paper' and computer_input == 'paper':
    return 'draw' 
  else:
    return "Some error is there in spelling" 
check_who_is_winning('rock','paper')  
list =[]
list.append('draw')
list.append('player')
list.append('player')
def check_ultimate_winner(round_list):
  player = round_list.count('player')
  computer = round_list.count('computer')
  draw = round_list.count('draw')
  if player > computer:
    return "player"
  elif computer > player:
    return "computer"
  else:
    return "draw" 
check_ultimate_winner(['player','player','player'])  
name = input("Please enter your name: ")  
rounds =take_rounds_input(name)
sub_round_winning_lst=[]
for i in range(rounds): 
  #Take player input first
  player_choice = give_me_a_player_option()
  print('Player choice is:  ',player_choice)  
   #Take ccomputer input..
  com_choice = give_me_a_computer_choice()
  print('Computer choice is:  ',com_choice) 
  #Check who is the winner..of the sub round
  sub_round_winner = check_who_is_winning(com_choice, player_choice)
  #Storre it for later use..
  sub_round_winning_lst.append(sub_round_winner)
print("Winner of sub_round ",sub_round_winning_lst)
print(check_ultimate_winner(sub_round_winning_lst), "is won the Game !!!" )
