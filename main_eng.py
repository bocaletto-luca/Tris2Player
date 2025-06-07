# Software Name: Tris 2 Player
# Author: Luca Bocaletto
# Language: English

# Import the Tkinter library for GUI and messagebox for message pop-ups.
import tkinter as tk
from tkinter import messagebox

# Main class for the Tic-Tac-Toe game.
class TrisGame:
    # Class variables to keep track of player wins.
    player1_wins = 0
    player2_wins = 0

    def __init__(self):
        # Initialize the game.
        self.current_player = "X"  # Start with player X.
        self.board = [" " for _ in range(9)]  # Initialize a list for the empty grid.
        self.buttons = []  # List of buttons on the grid.

    def setup_window(self):
        # Set up the game window.
        self.window = tk.Tk()  # Create a Tkinter window.
        self.window.title("Tic-Tac-Toe")  # Set the window title.

        # Labels to display player scores.
        self.label_player1 = tk.Label(self.window, text=f"Player 1 (X) Wins: {TrisGame.player1_wins}")
        self.label_player1.grid(row=3, column=0, columnspan=3)

        self.label_player2 = tk.Label(self.window, text=f"Player 2 (O) Wins: {TrisGame.player2_wins}")
        self.label_player2.grid(row=4, column=0, columnspan=3)

        # Create the 3x3 grid of buttons for the game.
        for i in range(3):
            row = []
            for j in range(3):
                # Create a button with empty text.
                button = tk.Button(self.window, text=" ", font=("normal", 20), width=10, height=2,
                                   command=lambda row=i, col=j: self.on_button_click(row, col))
                button.grid(row=i, column=j)  # Place the button on the grid.
                row.append(button)  # Add the button to the list of buttons.
            self.buttons.append(row)  # Add the row of buttons to the list of buttons.

    def on_button_click(self, row, col):
        # Handle the button click event.
        if self.board[row * 3 + col] == " ":
            self.board[row * 3 + col] = self.current_player  # Update the grid with the current player's symbol.
            text_color = "red" if self.current_player == "X" else "blue"  # Set text color.
            self.buttons[row][col].config(text=self.current_player, fg=text_color)  # Update the button.

            if self.check_winner(row, col):
                # Check if the player has won.
                messagebox.showinfo("Win!", f"Player {self.current_player} has won!")
                if self.current_player == "X":
                    TrisGame.player1_wins += 1  # Update the score for player X.
                else:
                    TrisGame.player2_wins += 1  # Update the score for player O.
                self.label_player1.config(text=f"Player 1 (X) Wins: {TrisGame.player1_wins}")
                self.label_player2.config(text=f"Player 2 (O) Wins: {TrisGame.player2_wins}")
                self.reset_board()  # Restart the game.
            else:
                if " " not in self.board:
                    # If there are no empty spaces on the grid, the game is a tie.
                    messagebox.showinfo("Tie", "The game ended in a tie.")
                    self.reset_board()  # Restart the game.
                else:
                    self.current_player = "O" if self.current_player == "X" else "X"  # Switch to the next player.

    def check_winner(self, row, col):
        # Check if the current player has won.
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
        for dr, dc in directions:
            count = 1
            for i in range(1, 3):
                r = row + dr * i
                c = col + dc * i
                if 0 <= r < 3 and 0 <= c < 3 and self.board[r * 3 + c] == self.current_player:
                    count += 1
                else:
                    break
            for i in range(1, 3):
                r = row - dr * i
                c = col - dc * i
                if 0 <= r < 3 and 0 <= c < 3 and self.board[r * 3 + c] == self.current_player:
                    count += 1
                else:
                    break
            if count >= 3:
                return True  # The player has won.

        return False  # The player has not won.

    def reset_board(self):
        # Restart the game by closing the current window and creating a new instance.
        self.window.destroy()  # Close the current window.
        game = TrisGame()  # Create a new instance of TrisGame.
        game.run()  # Start the new game.

    def run(self):
        # Start the game.
        self.setup_window()  # Set up the window.
        self.window.mainloop()  # Start the main Tkinter loop.

if __name__ == "__main__":
    # Run the game when the module is executed as the main script.
    game = TrisGame()  # Create an instance of the game.
    game.run()  # Start the game.
