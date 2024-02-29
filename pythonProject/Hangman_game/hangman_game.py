from os import strerror
from tkinter import *
import random

def choose_word():
    try:
        with open('new.txt', 'r', encoding='utf-8') as file:
            text = file.read()
            list_words = text.replace(" ", "").lower().split(',')
            number = random.randint(0, len(list_words) - 1)
            return list_words[number]
    except IOError as e:
        print("Błąd IO", strerror(e.errno))

def submit_word(entry_word, submit_button, label, label_image):
    word1 = entry_word.get()
    if word1 == "":
        label.config(text="Podaj ponownie słowo! ")
    else:
        entry_word.destroy()
        submit_button.destroy()
        label.config(text="Podaj literę!")
        label_var = Label(new_window, text="", font=('Comic Sans MS', 14), bg="#D1C79A")
        label_word = Label(new_window, text="", font=('Comic Sans MS', 14), bg="#D1C79A")
        entry_letter = Entry(new_window, font=('Comic Sans MS', 14))
        check_letter(word1, entry_letter, label_var, label_word, label_image)

def check_letter(word, entry_letter, label_var, label_word, label_image, choose_mode=0):
    man_list = [PhotoImage(file=f"resources\man{num:d}.png") for num in range(1, 11)]
    count = 0
    label_image.config(image=man_list[count])
    label_loss_or_win=Label(new_window, text="Przegrałeś ", font=('Comic Sans MS', 30), bg="#D1C79A")

    word_n = ['_' for _ in range(len(word))]
    label_var.pack()
    label_word.pack()
    entry_letter.pack()

    def submit_letter():
        nonlocal count
        nonlocal word_n

        letter = entry_letter.get().lower()
        entry_letter.delete(0, END)

        found = False
        for index, char in enumerate(word):
            if char == letter:
                word_n[index] = letter
                found = True

        if not found:
            count += 1
            label_var.config(text=f"Błędna litera. Pozostało prób: {9 - count}")
            if count < 10:
                label_image.config(image=man_list[count])
        else:
            label_var.config(text=f"Poprawna litera!")

        label_word.config(text=' '.join(word_n))

        if "".join(word_n) == word:
            label_var.config(text="Gratulacje! Odnalazłeś słowo:")
        elif count >= 9:
            label_var.config(text=f"Przekroczyłeś limit prób. Prawidłowe słowo to: {word}")
            label_image.destroy()
            submit_button.config(state="disabled")
            label_loss_or_win.pack()
            new_game_button=Button(new_window, text="Nowa gra",width=10,height=1, font=('Comic Sans MS', 14), command=lambda: singleplayer_window(new_window) if choose_mode else multiplayer_window(new_window))
            new_game_button.pack()


    submit_button = Button(new_window, text="Zatwierdź",width=10,height=1,font=('Comic Sans MS', 14), command=submit_letter)
    submit_button.pack()

    label_image.pack()

def multiplayer_window(main_window):
    global new_window
    new_window = Toplevel(main_window)
    main_window.withdraw()  # Ukryj pierwotne okno
    new_window.geometry("800x600")
    new_window.title("Wisielec- Tryb Automatyczny")
    new_window.config(background='#D1C79A')

    label = Label(new_window,
                  text="Podaj słowo do odgadnięcia!",
                  font=('Comic Sans MS', 20, 'bold'),
                  bg="#8A8365",
                  relief="ridge",
                  bd=2,
                  padx=10,
                  pady=10,
                  )
    label.pack()

    label_image = Label(new_window, bg="#8A8365")
    entry_word = Entry(new_window, font=('Comic Sans MS', 14), show="*")
    submit_button = Button(new_window, text="Zatwierdź", command=lambda: submit_word(entry_word, submit_button, label, label_image))
    entry_word.pack()
    submit_button.pack()

    new_window.mainloop()

def singleplayer_window(main_window):
    global new_window
    choose_mode=1
    new_window = Toplevel(main_window)
    main_window.withdraw()  # Ukryj pierwotne okno
    new_window.geometry("800x600")
    new_window.title("Wisielec- Tryb Własne Słowo")
    new_window.config(background='#D1C79A')

    label = Label(new_window,
                  text="Wisielec- podaj literę!",
                  font=('Comic Sans MS', 20, 'bold'),
                  bg="#8A8365",
                  relief="ridge",
                  bd=2,
                  padx=10,
                  pady=10,
                  )
    label.pack()

    word = choose_word()
    label_var = Label(new_window, text="", font=('Comic Sans MS', 14), bg="#D1C79A")
    label_word = Label(new_window, text="", font=('Comic Sans MS', 14), bg="#D1C79A")
    entry_letter = Entry(new_window, font=('Comic Sans MS', 14))

    label_image = Label(new_window, bg="#8A8365")
    check_letter(word, entry_letter, label_var, label_word, label_image, choose_mode)

    new_window.mainloop()

def main_window():
    window = Tk()
    window.geometry("800x600")
    window.title("Wisielec")
    logo = PhotoImage(file="logo.png")
    window.iconphoto(True, logo)
    window.config(background='#D1C79A')

    label = Label(window,
                  text="Wisielec- wybierz tryb gry!",
                  font=('Comic Sans MS', 30, 'bold'),
                  bg="#8A8365",
                  relief="ridge",
                  bd=10,
                  padx=10,
                  pady=10,
                  )

    main_frame = Frame(window)
    main_frame.place(relx=0.5, rely=0.5, anchor="n")

    Button(main_frame,
           text="Tryb Automatyczny",
           command=lambda: singleplayer_window(window),
           font=('Comic Sans MS', 25, 'bold'),
           bg="#8A8365",
           relief="ridge",
           bd=10,
           padx=7,
           pady=7,
           width=15).pack(side=RIGHT)

    Button(main_frame,
           text="Tryb Własne Słowo",
           command=lambda: multiplayer_window(window),
           font=('Comic Sans MS', 25, 'bold'),
           bg="#8A8365",
           relief="ridge",
           bd=10,
           padx=7,
           pady=7,
           width=15).pack(side=RIGHT)

    label.place(relx=0.5, rely=0.02, anchor="n")
    window.mainloop()

if __name__ == "__main__":
    main_window()