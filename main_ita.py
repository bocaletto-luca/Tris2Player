# Software Name: Tris 2 Player
# Author: Bocaletto Luca
# Language: Italian

# Importa la libreria Tkinter per la GUI e messagebox per i popup di messaggi.
import tkinter as tk
from tkinter import messagebox

# Classe principale per il gioco del Tris.
class TrisGame:
    # Variabili di classe per tenere traccia delle vittorie dei giocatori.
    player1_wins = 0
    player2_wins = 0

    def __init__(self):
        # Inizializza il gioco.
        self.current_player = "X"  # Inizia con il giocatore X.
        self.board = [" " for _ in range(9)]  # Inizializza una lista per la griglia vuota.
        self.buttons = []  # Lista di pulsanti sulla griglia.

    def setup_window(self):
        # Configura la finestra del gioco.
        self.window = tk.Tk()  # Crea una finestra Tkinter.
        self.window.title("Tris")  # Imposta il titolo della finestra.

        # Etichette per visualizzare il punteggio dei giocatori.
        self.label_player1 = tk.Label(self.window, text=f"Player 1 (X) Vittorie: {TrisGame.player1_wins}")
        self.label_player1.grid(row=3, column=0, columnspan=3)

        self.label_player2 = tk.Label(self.window, text=f"Player 2 (O) Vittorie: {TrisGame.player2_wins}")
        self.label_player2.grid(row=4, column=0, columnspan=3)

        # Crea la griglia di bottoni 3x3 per il gioco.
        for i in range(3):
            row = []
            for j in range(3):
                # Crea un pulsante con testo vuoto.
                button = tk.Button(self.window, text=" ", font=("normal", 20), width=10, height=2,
                                   command=lambda row=i, col=j: self.on_button_click(row, col))
                button.grid(row=i, column=j)  # Posiziona il pulsante sulla griglia.
                row.append(button)  # Aggiunge il pulsante alla lista dei pulsanti.
            self.buttons.append(row)  # Aggiunge la riga di pulsanti alla lista dei pulsanti.

    def on_button_click(self, row, col):
        # Gestisce l'evento di clic su un pulsante.
        if self.board[row * 3 + col] == " ":
            self.board[row * 3 + col] = self.current_player  # Aggiorna la griglia con il simbolo del giocatore corrente.
            text_color = "red" if self.current_player == "X" else "blue"  # Imposta il colore del testo.
            self.buttons[row][col].config(text=self.current_player, fg=text_color)  # Aggiorna il pulsante.

            if self.check_winner(row, col):
                # Verifica se il giocatore ha vinto.
                messagebox.showinfo("Vittoria!", f"Il giocatore {self.current_player} ha vinto!")
                if self.current_player == "X":
                    TrisGame.player1_wins += 1  # Aggiorna il punteggio del giocatore X.
                else:
                    TrisGame.player2_wins += 1  # Aggiorna il punteggio del giocatore O.
                self.label_player1.config(text=f"Player 1 (X) Vittorie: {TrisGame.player1_wins}")
                self.label_player2.config(text=f"Player 2 (O) Vittorie: {TrisGame.player2_wins}")
                self.reset_board()  # Riavvia il gioco.
            else:
                if " " not in self.board:
                    # Se non ci sono spazi vuoti sulla griglia, il gioco è un pareggio.
                    messagebox.showinfo("Pareggio", "Il gioco è finito in pareggio.")
                    self.reset_board()  # Riavvia il gioco.
                else:
                    self.current_player = "O" if self.current_player == "X" else "X"  # Passa al prossimo giocatore.

    def check_winner(self, row, col):
        # Controlla se il giocatore corrente ha vinto.
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
                return True  # Il giocatore ha vinto.

        return False  # Il giocatore non ha vinto.

    def reset_board(self):
        # Riavvia il gioco chiudendo la finestra attuale e creandone una nuova istanza.
        self.window.destroy()  # Chiude la finestra attuale.
        game = TrisGame()  # Crea una nuova istanza di TrisGame.
        game.run()  # Avvia il nuovo gioco.

    def run(self):
        # Avvia il gioco.
        self.setup_window()  # Configura la finestra.
        self.window.mainloop()  # Avvia il ciclo principale Tkinter.

if __name__ == "__main__":
    # Esegue il gioco quando il modulo viene eseguito come script principale.
    game = TrisGame()  # Crea un'istanza del gioco.
    game.run()  # Avvia il gioco.
