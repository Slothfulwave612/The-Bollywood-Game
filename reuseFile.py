# this python file will contain function that are used frequently in the project

import moduleFile as mf              # importing moduleFile as mf
import exceptionFile as ef           # importing exceptionFile as ef
import movieNameFile as mn           # importing movieNameFile as mn


def lineTime(sec):
    # function to print a new line and stopping the time for sec seconds
    mf.time.sleep(sec)              # using time.sleep method
    print()                         # printing a new line
# end of lineTime()


def logException(msg):
    # function to see whether log file is there in the directory or not
    # if there append the message and if not there then create the log file and then append the message

    for files in mf.os.listdir():

        if(files == 'gameLogFile.log'):
            pass                                # pass when the log file is found

    else:
        mf.logging.basicConfig(filename='gameLogFile.log', level=logging.INFO, format='%(asctime)s : %(message)s')
        # using basicConfig method

    mf.logging.info(msg)                        # appending msg into the log file
# end of logException()


def enterException():
    # function to display error message if enter key is not pressed

    while True:

        try:
            # try-except block to catch EnterException

            key = input('Press Enter Key To Continue').strip()

            if(key != ''):
                raise(mf.EnterException)           # raising EnterException when enter key is not pressed

            break                                  # breaking the loop when the enter key is pressed

        except mf.EnterException:
            lineTime(sec=0.5)                      # lineTime function
# end of enterException()


def enterName():
    # function to ask the user to input the name

    while True:

        try:
            # try-except block to catch LessThanOne Exception

            key = input('Enter Your Name :- ').strip()

            if(len(key) == 0):
                raise(ef.LessThanOne)           # raising LessThanOne when nothing is entered in the name part

            break                               # breaking the loop when name is entered

        except ef.LessThanOne:
            lineTime(sec=0.5)                   # lineTime function

    return(key)
# end of enterName()


def enterChoice():
    # function to ask the user to input the choice

    while True:

        try:
            # try-except block to catch the value error

            key = int(input('Enter Your Choice :- '))

            break                               # breaking the loop if the input entered is valid

        except ValueError:
            lineTime(sec=0.5)                   # lineTime function
            print('Invalid Input')
            lineTime(sec=0.5)                   # lineTime function

    return(key)
# end of enterChoice()


def guessChar():
    # function to ask for the guess

    while True:

        try:
            # try-except block to catch MoreThanOne and LessThanOne error

            key = input('Enter Your Guess :- ').strip()

            if(len(key) > 1):
                raise(ef.MoreThanOne)           # raising MoreThanOne error

            if(len(key) < 1):
                raise(ef.LessThanOne)           # raising LessThanOne error

            break                               # breaking the loop if the valid input is entered

        except ef.MoreThanOne:
            pass

        except ef.LessThanOne:
            pass

    return(key)
# end of guessChar()


def genGuesses(key):
    # function for finding out vowels in the movie
    g = set()
    s = ''

    for i in key:
        if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == '-'):
            g.add(i)
    # adding the vowels and dashes to a set g

    for i in g:
        s += i
    # then appending them to a string

    return(s)
# end of genGuesses()


def suffleMovie():
    # function for shuffling the movies

    mf.random.shuffle(mn.movieList)            # shuffling the movie names
    l = mn.movieList
    return(l)
# end of suffleMovie()


def strikethrough(key):
    # function for striking through Bollywood as the guess are wrong

    result = ''
    text = 'BOLLYWOOD'
    # result is our final result and text is our Bollywood

    if(key == 0):
        # if no wrong guesses
        result = text

    else:
        # if wrong guesses
        c = 0

        for i in text:

            result += i + '\u0336'      # striking through the character
            c += 1

            if(c == key):
                break

        if(c != len(text)):
            for i in range(c, len(text)):
                result += ' ' + text[i]

    print(result)
# end of strikethrough()


def displayScore(username, totScore, rigthGuess, wrongGuess):
    # function to display the stats
    print(f'{username}\'s Stats'.center(30, ' '))
    print(f'Name :- {username}')
    print(f'Total Score :- {totScore}')
    print(f'Successful Guesses :- {rigthGuess}')
    print(f'Unsuccessful Guesses :- {wrongGuess}')
# end of displayScore()

# end of the program
# programmed by Slothfulwave612
