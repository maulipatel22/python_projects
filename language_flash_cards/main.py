BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import random
import pandas

current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/korean_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")



def new_word():
    global current_card
    current_card = random.choice(to_learn)
    current_korean_word = current_card["Korean"]
    word_label["text"] = current_korean_word
    window.after(3000, flip_card)


def flip_card():
    korean_label.config(text="English")
    korean_label.config(fg="white", bg=BACKGROUND_COLOR)
    word_label.config(text=current_card["English"])
    word_label.config(fg="white", bg=BACKGROUND_COLOR, anchor="w")
    canvas.itemconfig(canvas_image, image=card_back_img)


def reset_c():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("words_to_learn.csv", index=False)
    canvas.itemconfig(canvas_image, image=card_front_img)
    korean_label.config(text="Korean", fg="black", bg="white")
    word_label.config(text="word", fg="black", bg="white", anchor="w")
    new_word()


def reset_w():
    canvas.itemconfig(canvas_image, image=card_front_img)
    korean_label.config(text="Korean", fg="black", bg="white")
    word_label.config(text="word", fg="black", bg="white", anchor="w")
    new_word()


window = Tk()
window.title("flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

window.after(3000, flip_card)

canvas = Canvas(height=526, width=800, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_img = PhotoImage(file="C:/Users/mauli/Downloads/flash-card-project-start_unzipped/images/card_front.png")
card_back_img = PhotoImage(file="C:/Users/mauli/Downloads/flash-card-project-start_unzipped/images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front_img)
canvas.grid(column=0, row=0, columnspan=2)

korean_label = Label(text="Korean", bg="white", font=("Ariel", 45, "italic"))
korean_label.place(x=320, y=100)
word_label = Label(text="word", bg="white", anchor="w", font=("Ariel", 35, "bold"))
word_label.place(x=320, y=253)

correct_image = PhotoImage(file="C:/Users/mauli/Downloads/flash-card-project-start_unzipped/images/right.png")
wrong_image = PhotoImage(file="C:/Users/mauli/Downloads/flash-card-project-start_unzipped/images/wrong.png")

correct_button = Button(image=correct_image, highlightthickness=0, command=reset_c)
correct_button.grid(column=1, row=1)
wrong_button = Button(image=wrong_image, highlightthickness=0, command=reset_w)
wrong_button.grid(column=0, row=1)

new_word()
window.mainloop()
