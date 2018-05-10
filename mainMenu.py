# this python file will contain main menu layout

from functionFile import *              # from functionFile importing everything
import reuseFile as rf                  # imoprting reuseFile as rf

obj = Insert_list('', 0, 0, 0, [])      # object of class Insert_list from functionFile

choice = 0

while(choice != 4):
    # the main menu

    rf.lineTime(sec=0.5)                # lineTime function

    print('The Bollywood Game'.center(50, ' '))

    rf.lineTime(sec=0.5)                # lineTime function

    print('1. Start The Game')
    print('2. View Scores')
    print('3. Instruction')
    print('4. Quit')

    choice = rf.enterChoice()          # enterChoice function for entering the name

    rf.lineTime(sec=0.5)               # lineTime function

    if(choice == 1):
        # for option 1
        obj.startGame()                # startGame function

    elif(choice == 2):
        # for option 2
        obj.displayTable()              # displayScore function

    elif(choice == 3):
        # for option 3
        obj.displayInstruction()        # displayInstruction function

    elif(choice == 4):
        # for option 3
        break                          # breaking the loop(exiting the game)

    else:
        # if any other input is entered
        rf.lineTime(sec=0.5)           # lineTime function
        print('Option Not Present')
        continue                       # using continue

# end of the program
# programmed by Slothfulwave612
