import sys
import random
from tkinter import *


def vars_1():
    STR_MSG = 'Well, {0}, I am thinking of a number between 1 and 20.'.format(nameEntry.get())
    return STR_MSG


def verifyQtde():
    qtde = int(chancesEntry.get())
    return qtde


def guessentry():
    guess = popup()
    return guess


def popup():
    STR_MSG_internal = vars_1()
    toplevel = Toplevel()
    label1 = Label(toplevel, text=STR_MSG_internal, height=0, width=100)
    label1.pack()
    guessContainer = Frame(toplevel)
    guessLabel = Label(guessContainer, text="Take a guess?")
    guessLabel["font"] = ("Arial", "10")
    guessContainer.pack()
    guessLabel.pack(side=LEFT)

    guessEntryContainer = Frame(toplevel)
    guessEntry = Entry(guessEntryContainer, textvariable=IntVar())
    guessEntry["width"] = 30
    guessEntry["font"] = ("Arial", "10")
    guessEntry.pack(side=RIGHT)
    guessEntryContainer.pack()

    containerButton = Frame(toplevel)
    button1 = Button(containerButton, text="Check", width=20, command=clickAbout)
    button1.pack(side='bottom', padx=5, pady=5)
    containerButton.pack()

    return int(guessEntry.get())


def clickAbout():
        guesses_made = 0
        verifyqtde_internal = verifyQtde()
        guesses_wanted = int(chancesEntry.get())
        number = random.randint(1, 20)
        guess = guessentry()
        toplevel1 = Toplevel()
        print(guess)

        while guesses_made < guesses_wanted:
            guesses_made += 1

            if guess < number:
                replyContainer = Frame(toplevel1)
                replylabel = Label(replyContainer,"Your guess is too low.",height=0, width=100)
                replylabel.pack()
                replyContainer.pack()

            if guess > number:
                replyContainer1 = Frame(toplevel1)
                replylabel1 = Label(replyContainer1, "Your guess is too high.", height=0, width=100)
                replylabel1.pack()
                replyContainer1.pack()

            if guess == number:
                break


        if guess == number:
            replyFinalContainer = Frame(toplevel1)
            replyFinallabel = Label(replyFinalContainer, "Good job, {0}! You guessed my number in {1} guesses!".format(nameEntry.get(),guesses_made), height=0, width=100)
            replyFinallabel.pack()
            replyFinalContainer.pack()

        else:
            replyFinalContainer1 = Frame(toplevel1)
            replyFinallabel1 = Label(replyFinalContainer1,'Nope. The number I was thinking of was {0}'.format(number),height=0, width=100)
            replyFinallabel1.pack()
            replyFinalContainer1.pack()

def hide_me(event):
    event.widget.pack_forget()


def popup1():
    qtde_chances_entry = int(chancesEntry.get())


    if qtde_chances_entry >= 3 and qtde_chances_entry <= 5:
        guessContainer = Frame(app)
        guessLabel = Label(guessContainer, text="Take a guess?")
        guessLabel["font"] = ("Arial", "10")
        guessContainer.pack()
        guessLabel.pack(side=LEFT)

        guessEntryContainer = Frame(app)
        guessEntry = Entry(guessEntryContainer)
        guessEntry["width"] = 30
        guessEntry["font"] = ("Arial", "10")
        guessEntry.pack(side=RIGHT)
        guessEntryContainer.pack()

    else:
        guessContainer = Frame(app)
        guessLabel = Label(guessContainer, text="Don't try to Cheat at me")
        guessLabel["font"] = ("Arial", "10")
        guessContainer.pack()
        guessLabel.pack(side=LEFT)



app = Tk()
app.title("Jogo de Advinha")
app.geometry("500x300+200+200")
#variaveis
guesses_made = 0

nameContainer = Frame(app)
nameLabel = Label(nameContainer, text="What's your name?")
nameLabel["font"] = ("Arial", "10")
nameContainer.pack()
nameLabel.pack(side=LEFT)

nameEntryContainer = Frame(app)
nameEntry = Entry(nameEntryContainer)
nameEntry["width"] = 30
nameEntry["font"] = ("Arial", "10")
nameEntryContainer.pack()
nameEntry.pack(side=RIGHT)

chancesContainer = Frame(app)
chancesLabel = Label(chancesContainer, text="How many chances do you want? (Between 3 and 5)?")
chancesLabel["font"] = ("Arial", "10")
chancesContainer.pack()
chancesLabel.pack(side=LEFT)

chancesEntryContainer = Frame(app)
chancesEntry = Entry(chancesEntryContainer, textvariable=IntVar())
chancesEntry["width"] = 30
chancesEntry["font"] = ("Arial", "10")
chancesEntryContainer.pack()
chancesEntry.pack(side=RIGHT)

containerButton = Frame(app)
button1 = Button(containerButton, text="Prosseguir", width=20, command=popup1)
button1.pack(side='bottom',padx=5,pady=5)
containerButton.pack()


app.mainloop()
