import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Крестики-нолики")

        self.player_wins = 0
        self.ai_wins = 0
        self.draws = 0

        self.current_player = None
        self.player_symbol = None
        self.ai_symbol = None
        self.board = [" "] * 9

        self.create_menu()
        self.create_scoreboard()
        self.create_board()

    def create_menu(self):
        menu_frame = tk.Frame(self.root)
        menu_frame.pack(pady=20)

        tk.Label(menu_frame, text="Выберите символ:").grid(row=0, column=0)

        tk.Button(menu_frame, text="X", command=lambda: self.start_game("X")).grid(row=0, column=1)
        tk.Button(menu_frame, text="O", command=lambda: self.start_game("O")).grid(row=0, column=2)

    def create_scoreboard(self):
        self.score_label = tk.Label(self.root, text=f"Игрок: {self.player_wins} | ИИ: {self.ai_wins} | Ничьи: {self.draws}")
        self.score_label.pack()

    def create_board(self):
        board_frame = tk.Frame(self.root)
        board_frame.pack()

        self.buttons = [tk.Button(board_frame, text=" ", width=5, height=2, font=('Arial', 40), command=lambda i=i: self.on_click(i)) for i in range(9)]
        for i, button in enumerate(self.buttons):
            button.grid(row=i//3, column=i%3)

        tk.Button(self.root, text="Перезапуск", command=self.reset_board).pack()

    def start_game(self, symbol):
        self.player_symbol = symbol
        self.ai_symbol = "O" if symbol == "X" else "X"
        self.current_player = "X"
        self.reset_board()
        if self.player_symbol == "O":
            self.ai_move()

    def on_click(self, index):
        if self.buttons[index]["text"] == " " and self.current_player == self.player_symbol:
            self.buttons[index]["text"] = self.player_symbol
            self.board[index] = self.player_symbol
            if not self.check_game_over():
                self.current_player = self.ai_symbol
                self.ai_move()

    def ai_move(self):
        best_move = self.find_best_move()
        if best_move is not None:
            self.buttons[best_move]["text"] = self.ai_symbol
            self.board[best_move] = self.ai_symbol
            if not self.check_game_over():
                self.current_player = self.player_symbol

    def find_best_move(self):
        for i in range(9):
            if self.board[i] == " ":
                self.board[i] = self.ai_symbol
                if self.check_winner(self.ai_symbol):
                    self.board[i] = " "
                    return i
                self.board[i] = " "

        for i in range(9):
            if self.board[i] == " ":
                self.board[i] = self.player_symbol
                if self.check_winner(self.player_symbol):
                    self.board[i] = " "
                    return i
                self.board[i] = " "

        for i in range(9):
            if self.board[i] == " ":
                return i
        return None

    def check_game_over(self):
        winner = self.check_winner(self.current_player) 
        if winner:
            self.root.update()

            if self.current_player == self.player_symbol:
                messagebox.showinfo("Игра окончена", "Игрок выиграл!")
                self.player_wins += 1
            else:
                messagebox.showinfo("Игра окончена", "ИИ выиграл!")
                self.ai_wins += 1
            self.update_scoreboard()
            return True
        elif all(self.board[i] != " " for i in range(9)):
            self.root.update()

            messagebox.showinfo("Игра окончена", "Ничья!")
            self.draws += 1
            self.update_scoreboard()
            return True
        return False


    def check_winner(self, symbol):
        combos = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        return any(all(self.board[i] == symbol for i in combo) for combo in combos)

    def update_scoreboard(self):
        self.score_label.config(text=f"Игрок: {self.player_wins} | ИИ: {self.ai_wins} | Ничьи: {self.draws}")

    def reset_board(self):
        self.board = [" "] * 9
        for button in self.buttons:
            button["text"] = " "
        self.current_player = "X"

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
