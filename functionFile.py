# this python file will contain the main code require for the execution of the program

import moduleFile as mf                 # importing moduleFile as mf
import exceptionFile as ef              # importing exceptionFile as ef
import reuseFile as rf                  # importing reuseFile as rf
import movieNameFile as mn              # importing movieNameFile as mn


class GameCode(object):
    # class named GameCode - parent class
    # data members(4) :- name, totScore, success, failure
    # member functions(3) :- startGame, displayTable, displayInstruction

    def __init__(self, name, totScore, success, failure):
        # constructor
        self.name = name            # for user name - string
        self.totScore = totScore    # for total score - integer
        self.success = success      # for successful attempts - integer
        self.failure = failure      # for unsuccessful attempts - integer

    def startGame(self):
        # code for option one

        username = rf.enterName()           # enterName function

        rf.lineTime(sec=0.5)                # lineTime function

        totChance = 3
        # totChance for total chances to play the game

        movieList = rf.suffleMovie()        # shuffleMovie function
        # movieList will contain all the shuffled movie names

        rigthGuess = 0
        wrongGuess = 0
        # rigthGuess for all the rigth guesses and wrong guesses for all the wrong guesses

        while(totChance > 0):

            c = 0

            for i in movieList:
                movie = i
                totGuess = 9                # totGuess for total guesses to guess the movie

                guesses = rf.genGuesses(key=movie)      # genGuesses function

                wrong = 0

                while(totGuess > 0):
                    win = 0

                    rf.lineTime(sec=0.5)               # lineTime function
                    rf.strikethrough(key=wrong)        # strikethrough function

                    for j in movie:
                        if j in guesses:
                            print(j, end=' ')
                        else:
                            print('_', end=' ')
                            win += 1
                    print()
                    # printing the movie name to be guessed

                    if(win == 0):
                        rf.lineTime(sec=0.5)            # lineTime function
                        print(f'{username}, you have guessed the movie correctly')

                        rigthGuess += 1

                        c += 1

                        if(c == 3):
                            c = 0
                            rf.lineTime(sec=0.5)        # lineTime funciton
                            print(f'{username}, you have guessed three consecutive movie correctly')
                            print(f'So, your total chances will be incremented by one')
                            totChance += 1

                        rf.lineTime(sec=0.5)            # lineTime function

                        totScore = (rigthGuess * 5) - (wrongGuess * 2)

                        rf.displayScore(username, totScore, rigthGuess, wrongGuess)               # displayScore function
                        print(f'Total Chances Remaining :- {totChance}')
                        rf.lineTime(sec=0.5)            # lineTime function

                        rf.enterException()             # enterException function

                        rf.lineTime(sec=0.5)            # lineTime function

                        break

                    rf.lineTime(sec=0.5)                # lineTime function

                    guess = rf.guessChar()              # guessChar function

                    if guess in guesses and guess not in movie:
                        pass

                    if guess not in guesses and guess not in movie:
                        totGuess -= 1
                        wrong += 1

                    guesses += guess

                    if(totGuess == 0):
                        rf.lineTime(sec=0.5)            # lineTime function
                        print(f'{username}, you failed to guess the movie')
                        totChance -= 1
                        c = 0
                        wrongGuess += 1

                        rf.lineTime(sec=0.5)            # lineTime function
                        print(f'Movie Name :- {movie}')

                        totScore = (rigthGuess * 5) - (wrongGuess * 2)

                        if(totChance != 0):
                            rf.lineTime(sec=0.5)            # lineTime function

                            rf.displayScore(username, totScore, rigthGuess, wrongGuess)               # displayScore function
                            print(f'Total Chances Remaining :- {totChance}')
                            rf.lineTime(sec=0.5)            # lineTime function

                            rf.enterException()             # enterException function

                            rf.lineTime(sec=0.5)            # lineTime function

                if(totChance == 0):
                    break

        rf.lineTime(sec=0.5)        # lineTime function
        print(f'{username} your all the chances are gone. So, your game ends here')

        rf.lineTime(sec=0.5)        # lineTime function
        rf.displayScore(username, totScore, rigthGuess, wrongGuess)               # displayScore function

        self.appendInfo(username, totScore, rigthGuess, wrongGuess)       # appendInfo function

        self.sortScore()            # sortScore function

        rf.lineTime(sec=0.5)        # lineTime function
        rf.enterException()         # enterException

    def displayTable(self):
        # function to display score in a table

        try:
            # try-except block

            with open('gameInfo.txt', 'rb') as my_file:
                file_loader = mf.pickle.load(my_file)       # loading the content

                maxName = max(len(i.name) for i in file_loader)

                maxScore = max(len(str(i.totScore)) for i in file_loader)

                maxSuccess = max(len(str(i.success)) for i in file_loader)

                maxFailure = max(len(str(i.failure)) for i in file_loader)

                columnTitle = ['Position', 'Name', 'Total Score', 'Successful Attempts', 'Unsuccessful Attempts']

                # calculating the maximum length present in each column element
                maxLength = [max(len(file_loader), len(columnTitle[0])), max(maxName, len(columnTitle[1])),
                             max(maxScore, len(columnTitle[2])), max(maxSuccess, len(columnTitle[3])), max(maxFailure, len(columnTitle[4]))]

                num_dashes = 0

                for i in range(len(maxLength)):
                    num_dashes += len('| ' + columnTitle[i] + ' ' * (maxLength[i] - len(columnTitle[i])) + ' |')
                    print('| ' + columnTitle[i] + ' ' * (maxLength[i] - len(columnTitle[i])) + ' |', end='')
                print(end='\n')

                print('=' * num_dashes)

                rowInfo, pos = [], 1

                for i in file_loader:
                    rowInfo.append(str(pos))
                    rowInfo.append(i.name)
                    rowInfo.append(str(i.totScore))
                    rowInfo.append(str(i.success))
                    rowInfo.append(str(i.failure))
                    pos += 1

                c = 0

                for i in rowInfo:
                    print('| ' + i + ' ' * (maxLength[c] - len(i)) + ' |', end='')
                    c += 1

                    if(c == len(columnTitle)):
                        c = 0
                        print(end='\n')

                rf.lineTime(sec=0.5)            # lineTime function
                rf.enterException()             # enterException function

        except FileNotFoundError:
            rf.lineTime(sec=0.5)        # lineTime function
            print('No user has played the game yet')

    def displayInstruction(self):
        # function to display the instruction of the game

        rf.lineTime(sec=0.5)                              # lineTime function

        print('You will be given a total of 3 chances to play the game.')
        input()
        print('A movie will be given to you only the vowels in the movie will be displayed and other characters are displayed as dashes.')
        input()
        print('You you have to guess those character in those dashes.')
        input()
        print('e.g. for movie dhoom 3 , _ _ o o _ - _ will be shown where _ are to be guesses and - is the space')
        input()
        print('A total of 9 chances(Bollywood) will be given to guess the movie.')
        input()
        print('On guessing the movie correctly 5 points will be given and if the guess is not correct then 2 points will be deducted.')
        input()
        print('On three correct guesses your total chance will be incremented by 1')

        rf.lineTime(sec=0.5)                            # lineTime function

        rf.enterException()                             # enterException function

# end of class GameCode


class Insert_list(GameCode):
    # derived class Insert_list of parent class GameCode
    # data members (1) :- user_info (Array of Objects)
    # member function (2) :- appendInfo, sortScore

    def __init__(self, name, totScore, success, failure, user_info):
        # constructor
        super(GameCode, self).__init__()         # super method
        self.user_info = user_info

    def appendInfo(self, username, totScore, rigthGuess, wrongGuess):
        # function to append the info as object in an array

        try:
            # try-exception clause
            with open('gameInfo.txt', 'rb') as my_file:
                self.user_info = mf.pickle.load(my_file)    # loading the content of the file

        except FileNotFoundError:
            # pass when File not found error is caught
            pass

        with open('newfile.txt', 'wb') as new_file:
            self.user_info.append(GameCode(username, totScore, rigthGuess, wrongGuess))
            # appending the info as object into the list user_info
            # which is actually is a list of objects
            mf.pickle.dump(self.user_info, new_file)
            # dumping the info to the file

        try:
            # try-exception clause
            mf.os.remove('gameInfo.txt')   # removing the file
        except FileNotFoundError:
            # passing when the program encounters File not found error
            pass

        mf.os.rename('newfile.txt', 'gameInfo.txt')
        # gameInfo.txt is the file where we are going to dump evey information of the user

    def sortScore(self):
        # function for sorting the score in desending order

        try:
            # try-except block
            with open('gameInfo.txt', 'rb') as my_file:
                x = mf.pickle.load(my_file)
                # loading the content of the file

        except FileNotFoundError:
            # pass when the error is caught
            pass

        with open('newfile.txt', 'wb') as new_file:
            x.sort(key=mf.operator.attrgetter('totScore'), reverse=True)
            # sorting our array of objects
            self.user_info = x
            mf.pickle.dump(self.user_info, new_file)
            # dumping the array of object into file

        try:
            # try-except clause
            mf.os.remove('gameInfo.txt')
        except FileNotFoundError:
            # pass when error is caught
            pass

        mf.os.rename('newfile.txt', 'gameInfo.txt')        # renaming the file

# end of class Insert_list

# end of the program
# programmed by Slothfulwave612
