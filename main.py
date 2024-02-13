import tkinter as tk
import random

class MineSwipIT:
    def __init__(self,master):
        self.master = master
        self.board= []
        self.buttons = []
        self.mines = []
        self.num_mines = 15
        self.generate_board()
        self.create_buttons()
        self.num_discovered = 0
        self.game_over = False

    def generate_board(self):
        # Generate a 8x8 board
        for i in range(8):
            self.board.append([0] * 8)
        # Place 15 mines randomly on the board
        while len(self.mines) < self.num_mines:
            x = random.randint(0, 7)
            y = random.randint(0, 7)
            if [x, y] not in self.mines:
                self.mines.append([x, y])
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if 0 <= x + i < 8 and 0 <= y + j < 8:
                            self.board[x + i][y + j] += 1

    def create_buttons(self):
        # Create buttons for the board
        for i in range(8):
            button_row = []
            for j in range(8):
                button = tk.Button(self.master, text="", width=3, height=1,
                                   command=lambda x=i, y=j: self.click(x, y))
                button.grid(row=i, column=j)
                button_row.append(button)
            self.buttons.append(button_row)

    def click(self, x, y):
        if self.game_over:
            return
        # Handle the button click event
        if [x, y] in self.mines:
            self.game_over = True
            self.show_result("Perdu!")
        else:
            self.buttons[x][y].config(text=str(self.board[x][y]),bg='white', state='disabled')
            self.num_discovered += 1
            if self.num_discovered == 64 - self.num_mines:
                self.show_result("Gagné!")

    def show_result(self, message):
        for i in range(8):
            for j in range(8):
                if [i, j] in self.mines:
                    self.buttons[i][j].config(text="*", bg='red',state="disabled")
                else:
                    self.buttons[i][j].config(text=str(self.board[i][j]), bg='white',state="disabled")
        result = tk.Label(self.master, text=message)
        result.grid(row=9, column=0, columnspan=8, pady=10)

root = tk.Tk()
root.title("MineSwipIT")
game = MineSwipIT(root)
root.mainloop()
