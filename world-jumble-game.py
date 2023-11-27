from tkinter import *
from random import choice
from random import shuffle
from tkinter import ttk
import time

root = Tk()
root.title('timers')
root.geometry('500x500')
root.config(bg='deep pink')

my_progress = ttk.Progressbar(
    root, orient=HORIZONTAL, length=400, mode='determinate', maximum=101)
my_progress.pack(pady=20)


my_label = Label(root, text='', font=('Helvetica', 48), bg='deep pink')
my_label.pack(pady=20)


def shufler():
    # deleting the hint label

    hint_label.config(text='')

    # reset hint count
    global hint_counter
    hint_counter = 0

    # deleting entry
    entry_answer.delete(0, END)

    # deleting answer label
    answer_label.config(text='')

    # deleting progress label

    # creating a list
    words = ['brewery', 'anathema', 'cavalry', 'defibrillattor',
             'asterisk', 'dogma', 'homogenous', 'engender', 'laconic', 'quiescence', 'laconic', 'anomalouss']

    # pick random word from the list
    global word
    word = choice(words)

    # break appart chosen word
    break_word = list(word)
    shuffle(break_word)

    # turn shuffked word into a word
    global shuffled_word
    shuffled_word = ''
    for W in break_word:
        shuffled_word += W

  # qprinting the shuffled_word

    my_label.config(text=shuffled_word)


def endin():
    shufler()

# create answer function


def answer():
    if word == entry_answer.get():
        answer_label.config(text='Correct!! ')
        if my_progress['value'] == 100:
            answer_label.config(
                text='congratulations you get to the next level! ')

            progress_label.config(text=my_progress['value'])

        else:
            my_progress.step(20)
            progress_label.config(text=my_progress['value'])
            endin()

    else:
        answer_label.config(text='Incorrect!!')
        entry_answer.delete(0, END)
        answer_label.config(text='try again')


# creating hint counter
global hint_counter
hint_counter = 0

#  create hint function


def hint(count):
    global hint_counter
    hint_counter = count
    # to get length of the word
    word_length = len(word)
    # shoew int
    if count < word_length:
        hint_label.config(text=F'{hint_label["text"]} {word[count]}')
        hint_counter += 1


entry_answer = Entry(root, font=('Helvetica', 14))
entry_answer.pack(pady=20)
# entry_answer.insert(0, 'Enter the answer')

button_frame = Frame(root, bg='deep pink')
button_frame.pack(pady=20)

answer_button = Button(button_frame, text='Answer',
                       bg='deep pink', command=answer, font=('Arial', 16))
answer_button.grid(row=0, column=0, padx=10)

my_button = Button(button_frame, text='pick another word',
                   bg='deep pink', command=shufler, font=('Arial', 16))
my_button.grid(row=0, column=1, pady=10)


hint_button = Button(button_frame, text='Hint',
                     bg='deep pink', command=lambda: hint(hint_counter), font=('Arial', 16))
hint_button.grid(row=0, column=2, padx=10)


answer_label = Label(root, text='', font=('Helvetica', 18), bg='deep pink')
answer_label.pack(pady=10)
hint_label = Label(root, text='', font=('Helvetica', 20), bg='deep pink')
hint_label.pack(pady=10)

progress_label = Label(root, text='', font=('Helvetica', 18), bg='deep pink')
progress_label.pack(pady=10)
# to run the shufler when program starts so that it starts it a name
shufler()
root.mainloop()
