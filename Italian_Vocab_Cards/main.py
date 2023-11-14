from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}


try:
    data = pandas.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    original_data = pandas.read_csv('data/italian_words.csv')
    to_learn = original_data.to_dict(orient='records')
else:
    to_learn = data.to_dict(orient='records')


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text='Italian', fill='black')
    canvas.itemconfig(card_word, text=current_card['Italian'], fill='black')
    canvas.itemconfig(card_remaining, text=f'Left: {len(to_learn)}', fill='black')
    canvas.itemconfig(card_background, image=card_front)
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(card_title, text='English', fill='white')
    canvas.itemconfig(card_word, text=current_card['English'], fill='white')
    canvas.itemconfig(card_remaining, fill='white')
    canvas.itemconfig(card_background, image=card_back)


def is_known():
    to_learn.remove(current_card)
    learnt_data = pandas.DataFrame(to_learn)
    learnt_data.to_csv('data/words_to_learn.csv', index=False)
    next_card()


window = Tk()
window.title('Flashy')
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file='images/card_front.png')
card_back = PhotoImage(file='images/card_back.png')
card_background = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 150, text='', font=('Ariel', 40, 'italic'))
card_word = canvas.create_text(400, 263, text='', font=('Ariel', 60, 'bold'))
card_remaining = canvas.create_text(70, 50, text=f'Left: {len(to_learn) - 1}', font=('Ariel', 20, 'italic'))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

check_mark_img = PhotoImage(file='images/right.png')
check_mark = Button(image=check_mark_img, highlightbackground=BACKGROUND_COLOR, command=is_known)
check_mark.grid(column=0, row=1)

wrong_mark_img = PhotoImage(file='images/wrong.png')
wrong_mark = Button(image=wrong_mark_img, highlightbackground=BACKGROUND_COLOR, command=next_card)
wrong_mark.grid(column=1, row=1)

next_card()


window.mainloop()
