from tkinter import *
import random
import tkinter.font as font

game_window = Tk()
game_window.title("Rock Paper Scissor Game")
app_font = font.Font(size = 12)

#Displaiyng Game title
game_title = Label(text = "Rock Paper Scissors", font=font.Font(size = 20), fg = "grey")
game_title.pack()

#Labels to display
winner_label = Label(text = "Let's play!", fg = 'blue', font = font.Font(size=15))
winner_label.pack()

input_frame = Frame(game_window)
input_frame.pack()

#Player Options
player_option = Label(input_frame, text = " Your Choices are : ",  font = app_font, fg = 'grey')
player_option.grid(row=0,column=1,pady =15)

#rockbtn
rock_btn =Button(input_frame, text = "ROCK" , width = 15,pady= 5 ,fg = 'white',bg='black',command= lambda: rpsls('rock'))
rock_btn.grid(row =1,column=2, padx = 8, pady =5)
#paperbtn
paper_btn =Button(input_frame, text = "PAPER" , width = 15,pady= 5 ,fg = 'black',bg='white',command= lambda: rpsls('paper'))
paper_btn.grid(row =1,column=1, padx= 8 ,pady=5)
#spock
spock_btn =Button(input_frame, text = "SPOCK" , width = 15,pady= 5 ,fg = 'black',bg='light green',command= lambda: rpsls('spock'))
spock_btn.grid(row =1,column=3,padx= 8 ,pady=5)

#scissor
scissor_btn =Button(input_frame, text = "SCISSOR" , width = 15,pady= 5 ,fg = 'black',bg='light blue',command= lambda: rpsls('scissor'))
scissor_btn.grid(row =1,column=4,padx= 8 ,pady=5)
#lizard
lizard_btn =Button(input_frame, text = "LIZARD" , width = 15,pady= 5 ,fg = 'white',bg='dark green',command= lambda: rpsls('lizard'))
lizard_btn.grid(row =1,column=5,padx= 8 ,pady=5)

#Scoreboard
score_label = Label(input_frame, text = "***Scoreboard***" , font = app_font, fg= "black")
score_label.grid(row = 3, columnspan = 6)

#Player and Computer Score , choices
player_choice_label = Label(input_frame, text = 'You Selected : ', font = app_font)
player_choice_label.grid(row = 4, column = 2, pady = 5)
player_choice_display = Label(input_frame, text = " ", font = app_font)
player_choice_display.grid(row=5,column =2, pady = 5)

comp_choice_label = Label(input_frame, text = 'Computer Selected : ', font = app_font)
comp_choice_label.grid(row = 4, column = 4, pady = 5)
comp_choice_display = Label(input_frame, text = " ", font = app_font)
comp_choice_display.grid(row=5,column =4, pady = 5)


#Gamelogic
def name_to_number(name):
  name = name.lower()
  if name == 'rock':
    return 0
  elif name == 'spock':
    return 1
  elif name == 'paper':
    return 2
  elif name =='lizard':
    return 3
  else:
    return 4  

def number_to_name(number):
  if number in range(5):
    if number == 0:
      return 'rock'
    elif number == 1:
      return 'Spock'
    elif number == 2:
      return 'paper'
    elif number == 3:
      return 'lizard'
    else:
      return 'scissors'
  else:
    return('Number out of range')

def rpsls(player_choice):
  print(" ")
  
  player_number = name_to_number(player_choice)
  player_choice_display.config(text = player_choice.upper(),fg = 'dark blue')
  
  comp_number = random.randrange(5)
  comp_choice = number_to_name(comp_number)
  comp_choice_display.config(text = comp_choice.upper(), fg = 'red')

  diff = player_number - comp_number
  if (diff % 5 == 3) or(diff % 5 == 4):
    winner_label.config(text = "Computer Wins! :(")
  elif diff == 0:
    winner_label.config(text = "Tie Game :|")
  else:
    winner_label.config(text = "You win! :) ")

game_window.geometry('700x300')
game_window.mainloop()
