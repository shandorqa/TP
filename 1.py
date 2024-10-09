import tkinter as tk

def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] != '':
            return True
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] != '':
            return True
    if board[0][0] == board[1][1] == board[2][2] != '':
        return True
    if board[0][2] == board[1][1] == board[2][0] != '':
        return True
    return False

def on_click(row, col):
    global player, board, buttons, label

    if board[row][col] == '':
        buttons[row][col].config(text=player)
        board[row][col] = player

        if check_winner(board):
            label.config(text=f"Player {player} wins!")
            for row in buttons:
                for button in row:
                    button.config(state=tk.DISABLED)
        else:
            player = 'O' if player == 'X' else 'X'
            label.config(text=f"Player {player}'s turn")

def restart_game():
    global player, board, buttons, label

    player = 'X'
    board = [['' for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text='', state=tk.NORMAL)
    label.config(text=f"Player {player}'s turn")

root = tk.Tk()
root.title("Krestiki-Noliki")

player = 'X'
board = [['' for _ in range(3)] for _ in range(3)]
buttons = [[None]*3 for _ in range(3)]

for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text='', font=('Arial', 20), width=5, height=2, command=lambda i=i, j=j: on_click(i, j))
        buttons[i][j].grid(row=i, column=j)

label = tk.Label(root, text=f"Player {player}'s turn", font=('Arial', 12))
label.grid(row=3, columnspan=3)

restart_button = tk.Button(root, text="New game", command=restart_game)
restart_button.grid(row=4, columnspan=3)

root.mainloop()
