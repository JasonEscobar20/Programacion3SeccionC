import tkinter as tk
from tkinter import messagebox

import random

class TreeNode:
    def __init__(self, state, value=0.5):
        self.state = state
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, state, value=0.5):
        if not self.root:
            self.root = TreeNode(state, value)
        else:
            self._insert(self.root, state, value)

    def _insert(self, node, state, value):
        if state < node.state:
            if node.left is None:
                node.left = TreeNode(state, value)
            else:
                self._insert(node.left, state, value)
        else:
            if node.right is None:
                node.right = TreeNode(state, value)
            else:
                self._insert(node.right, state, value)

    def find(self, state):
        return self._find(self.root, state)

    def _find(self, node, state):
        if node is None:
            return None
        if state == node.state:
            return node
        elif state < node.state:
            return self._find(node.left, state)
        else:
            return self._find(node.right, state)

    def __iter__(self):
        return self.in_order_traversal(self.root)

    def in_order_traversal(self, node):
        if node:
            yield from self.in_order_traversal(node.left)
            yield node
            yield from self.in_order_traversal(node.right)


class LearningTicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe con Aprendizaje")
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_widgets()
        self.tree = BinaryTree()
        self.state_history = []  # Track states visited during a game
        self.epsilon = 0.2  # Probability for exploration
        self.alpha = 0.5  # Learning rate
        self.gamma = 0.9  # Discount factor
        self.initialize_tree()
        self.match_history = []  # Track match history

    def create_widgets(self):
        for row in range(3):
            for col in range(3):
                self.buttons[row][col] = tk.Button(self.master, text='', font=('normal', 40),
                                                   width=5, height=2,
                                                   command=lambda row=row, col=col: self.on_click(row, col))
                self.buttons[row][col].grid(row=row, column=col)

    def on_click(self, row, col):
        if self.board[row][col] == '' and not self.check_winner():
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            self.state_history.append(self.get_state())
            if self.check_winner():
                self.update_state_values(1)  # Win for current player
                self.match_history.append(f"Player {self.current_player} wins!")
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_game()
            elif self.is_board_full():
                self.update_state_values(0.5)  # Draw
                self.match_history.append("It's a draw!")
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_game()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'
                self.ai_move()

    def ai_move(self):
        best_move = None
        if random.random() < self.epsilon:
            # Exploration: choose a random move
            empty_cells = [(row, col) for row in range(3) for col in range(3) if self.board[row][col] == '']
            best_move = random.choice(empty_cells)
        else:
            # Exploitation: choose the best known move
            best_value = -float('inf')
            for row in range(3):
                for col in range(3):
                    if self.board[row][col] == '':
                        self.board[row][col] = self.current_player
                        state_value = self.get_state_value()
                        self.board[row][col] = ''
                        if state_value > best_value:
                            best_value = state_value
                            best_move = (row, col)

        if best_move:
            row, col = best_move
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            self.state_history.append(self.get_state())
            if self.check_winner():
                self.update_state_values(-1)  # Loss for human player
                self.match_history.append(f"Player {self.current_player} wins!")
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_game()
            elif self.is_board_full():
                self.update_state_values(0.5)  # Draw
                self.match_history.append("It's a draw!")
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_game()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def get_state_value(self):
        state = self.get_state()
        node = self.tree.find(state)
        if node is None:
            self.tree.insert(state)
            node = self.tree.find(state)
        return node.value

    def get_state(self):
        return ''.join([''.join(row) for row in self.board])

    def update_state_values(self, result):
        # Traverse the state history in reverse to propagate values
        next_value = result
        for state in reversed(self.state_history):
            node = self.tree.find(state)
            if node:
                node.value += self.alpha * (self.gamma * next_value - node.value)
                next_value = node.value

    def check_winner(self):
        for row in self.board:
            if row[0] == row[1] == row[2] != '':
                return True
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != '':
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != '':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != '':
            return True
        return False

    def is_board_full(self):
        for row in self.board:
            for cell in row:
                if cell == '':
                    return False
        return True

    def reset_game(self):
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.state_history = []
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text='')

    def initialize_tree(self):
        # Initial population of the tree can be done here if necessary
        pass

class MainMenu:
    def __init__(self, master):
        self.master = master
        self.master.title("Main Menu")
        self.frame = tk.Frame(self.master, pady=30, padx=100)
        self.frame.pack()
        
        self.new_game_button = tk.Button(self.frame, text="New Game", command=self.new_game)
        self.new_game_button.pack(pady=10)
        
        self.match_history_button = tk.Button(self.frame, text="Match History", command=self.show_match_history)
        self.match_history_button.pack(pady=10)
        
        self.learning_stats_button = tk.Button(self.frame, text="Learning Statistics", command=self.show_learning_statistics)
        self.learning_stats_button.pack(pady=10)
        
        self.group_members = tk.Button(self.frame, text="Group members", command=self.show_group_members)
        self.group_members.pack(pady=10)

    def new_game(self):
        game_window = tk.Toplevel(self.master)
        self.app = LearningTicTacToe(game_window)

    def show_match_history(self):
        history_window = tk.Toplevel(self.master)
        history_text = tk.Text(history_window)
        history_text.pack()
        history_text.insert(tk.END, "\n".join(self.app.match_history))

    def show_learning_statistics(self):
        stats_window = tk.Toplevel(self.master)
        stats_text = tk.Text(stats_window)
        stats_text.pack()
        stats = "\n".join([f"State: {node.state}, Value: {node.value}" for node in self.app.tree])
        stats_text.insert(tk.END, stats)
    
    def show_group_members(self):
        messagebox.showinfo("Group Members", "Name: Jason Javier Escobar Gomez\nCarnet: 9490-19-1725\nSeccion: C")


if __name__ == "__main__":
    root = tk.Tk()
    main_menu = MainMenu(root)
    root.mainloop()