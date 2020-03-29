# coding=utf-8
# 'Guess the number' game with a graphical interface

import random
from tkinter import *

class Application(Frame):
    """GUI application, 'Guess the Number' game with graphical interface"""
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
        self.random_number()
        self.counter = 6

    def create_widgets(self):
        """Creates controls with which the user will enter the source data"""
        # label with text instruction
        Label(self, text = "  "
              ).grid(row = 0, column = 0, columnspan = 1, sticky = W)

        Label(self, text = "The program makes a number in the range from 0 to 100."
              ).grid(row = 1, column = 0, columnspan = 1, sticky = W)

        Label(self, text = "You must guess!"
              ).grid(row = 2, column = 0, columnspan = 1, sticky = W)

        Label(self, text = "  "
              ).grid(row = 3, column = 0, columnspan = 1, sticky = W)

        Label(self, text = "CONCLUSION OF RESULTS: "
              ).grid(row = 11, column = 0, columnspan = 1, sticky = S)

        # label and input field for person name
        Label(self, text = "INTRODUCE YOURESELF: ").grid(row = 4, column = 0, sticky = W)
        self.person_ent = Entry(self)
        self.person_ent.grid(row = 5, column = 0, sticky = W)

        # label and input field for number
        Label(self, text = "ENTER YOUR NUMBER: ").grid(row = 6, column = 0, sticky = W)
        self.number = Entry(self)
        self.number.grid(row = 7, column = 0, sticky = W)

        # data send button
        Button(self, text = "Check!", command = self.check_number).grid(row = 10, column = 0, sticky = W)

        # clean button
        Button(self, text = "Clear screen!", command = self.clear).grid(row = 9, column = 0, sticky = S)

        # hint button
        Button(self, text = "Take a hint!", command = self.help).grid(row = 10, column = 0, sticky = E)

        # display result
        self.result = Text(self, width = 75, height = 10, wrap = WORD)
        self.result.grid(row = 12, column = 0, columnspan = 1)

    def random_number(self):
        """number generation"""
        self.number_random = str(random.randint(0, 100))
        self.const_number = self.number_random

    def clear(self):
        """clear results screen"""
        self.result.delete(0.0, END)

    def help(self):
        """hint"""
        # display random number on request
        self.result.insert(0.0, "\nThe guessed number: " + self.const_number)

    def check_number(self):
        """based on user input"""
        # get values from the GUI
        person = self.person_ent.get()
        number = int(self.number.get())
        number2 = int(self.const_number)
        self.counter -= 1
        if number2 > number:
            message = "\n==> MYSTERIOUS NUMBER MORE... YOUR NUMBER: " + str(number) + \
                      " / ATTEMPT REMAINED: " + str(self.counter)
            self.result.insert(0.0, message)
        elif number2 < number:
            message = "\n==> MYSTERIOUS NUMBER LESS ... YOUR NUMBER: " + str(number) + \
                      " / ATTEMPT REMAINED: " + str(self.counter)
            self.result.insert(0.0, message)
        elif number2 == number:
            message = person + ", YOU WIN. COMPUTER-ASKED NUMBER: " + str(number2) + "\n"
            self.result.insert(0.0, message)

        if self.counter == 0:
            message2 = person + ", YOU LOST! THE GAME IS OVER! " \
                                "COMPUTER-ASKED NUMBER: " + str(number2) + "\n"
            self.result.insert(0.0, message2)

# main part
root = Tk()
root.title("Guess the number!")
app = Application(root)
root.mainloop()

