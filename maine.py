import csv
import random
import os
from enum import Enum, auto
import getpass
from typing import Optional, Tuple

CSV_FILE = "players.csv"

class Move(Enum):
    ROCK = auto()
    PAPER = auto()
    SCISSORS = auto()

    @staticmethod
    def from_input(inp: str) -> Optional['Move']:
        inp = inp.strip().lower()
        mapping = {
            '1': Move.ROCK,
            '2': Move.PAPER,
            '3': Move.SCISSORS,
            'rock': Move.ROCK,
            'paper': Move.PAPER,
            'scissors': Move.SCISSORS
        }
        return mapping.get(inp)

class Player:
    def __init__(self, username: str, password: str, wins: int = 0, losses: int = 0, draws: int = 0):
        self.username = username
        self.password = password
        self.wins = int(wins)
        self.losses = int(losses)
        self.draws = int(draws)

    def record_result(self, outcome: str) -> None:
        for x in outcome:
            if outcome == x:
                if x == "win":
                    self.wins += 1
                elif x == "loss":
                    self.losses += 1
                else:
                    self.draws += 1

    def get_feedback(self) -> str:
        if self.wins > self.losses:
            return 'Looks like you are in the lead\n'
        elif self.losses > self.wins:
            return 'The Computer is in the lead\n'
        return 'Even scores, so far a tie\n'

    def reset_stats(self) -> None:
        self.wins = self.losses = self.draws = 0

    def __str__(self) -> str:
        return f"{self.username} | W: {self.wins} | L: {self.losses} | D: {self.draws}"

class AuthSystem:
    def __init__(self, filepath: str):
        self.filepath = filepath
        self._initialize_csv()

    def _initialize_csv(self) -> None:
        try:
            with open(self.filepath, mode='x', newline='') as f:
                csv.writer(f).writerow(['username', 'password', 'wins', 'losses', 'draws'])
        except FileExistsError:
            pass

    def find_user(self, username: str) -> Optional[Player]:
        username = username.lower()
        try:
            with open(self.filepath, newline='') as f:
                for row in csv.DictReader(f):
                    if row['username'].lower() == username:
                        return Player(**row)
        except FileNotFoundError:
            print('Player database not found. Please restart the application.')
            raise
        return None

    def register_user(self, username: str, password: str) -> Optional[Player]:
        if self.find_user(username):
            print("Username already exists.")
            return None
        
        try:
            with open(self.filepath, 'a', newline='') as f:
                csv.writer(f).writerow([username, password, 0, 0, 0])
            return Player(username, password)
        except Exception as e:
            print(f"Error registering user: {e}")
            return None

    def authenticate_user(self, username: str, password: str) -> Optional[Player]:
        user = self.find_user(username)
        return user if user and user.password == password else None

    def save_user(self, player: Player) -> None:
        try:
            rows = []
            with open(self.filepath, newline='') as f:
                reader = csv.DictReader(f)
                fieldnames = reader.fieldnames
                for row in reader:
                    if row['username'].lower() == player.username.lower():
                        row.update({
                            'wins': player.wins,
                            'losses': player.losses,
                            'draws': player.draws
                        })
                    rows.append(row)
            with open(self.filepath, 'w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(rows)
        except Exception as e:
            print(f"Error saving player data: {e}")
            raise

class Game:
    def __init__(self):
        self.auth = AuthSystem(CSV_FILE)
        self.player = None

    def _get_user_credentials(self) -> Tuple[str, str]:
        while True:
            username = input('Username: ').strip()
            if username:
                break
            print('Username can\'t be empty')
        password = getpass.getpass('Password: ')
        return username, password

    def login_or_register(self) -> None:
        print('Welcome to Ridwan\'s Rock Paper Scissors game')
        while True:
            choice = input("Type 'login' or 'register': ").lower()
            if choice not in ('login', 'register'):
                print("Invalid input, type completely or try again\n")
                continue
            username, password = self._get_user_credentials()
            if choice == 'login':
                self.player = self.auth.authenticate_user(username, password)
                if self.player:
                    print(f"\nWelcome back, {username}!\n")
                    return
                print('Invalid login. Please try again.\n')
            else:
                self.player = self.auth.register_user(username, password)
                if self.player:
                    print(f'\nWelcome, {username}, you are now in the system\n')
                    return

    def get_computer_move(self) -> Move:
        return random.choice(list(Move))

    def decide_winner(self, user_move: Move, comp_move: Move) -> str:
        win_cases = {
            (Move.ROCK, Move.SCISSORS),
            (Move.PAPER, Move.ROCK),
            (Move.SCISSORS, Move.PAPER)
        }
        return "draw" if user_move == comp_move else "win" if (user_move, comp_move) in win_cases else "loss"

    def _get_user_move(self) -> Move:
        while True:
            choice = input('Pick (1)Rock, (2)Paper, or (3)Scissors. You can also put in numbers if you are lazy: ').strip()
            move = Move.from_input(choice)
            if move:
                return move
            print("Invalid input, follow the instructions and try again")

    def _handle_post_game(self) -> bool:
        while True:
            choice = input('\nWant to play again? \nYes \nNo \n(reset) my stats\n').strip().lower()
            if choice == 'reset':
                self.player.reset_stats()
                self.auth.save_user(self.player)
                print("Stats reset.")
                return True
            elif choice in ('y', 'yes'):
                return True
            elif choice in ('n', 'no'):
                return False
            print("Invalid input, follow the instructions")

    def game_loop(self) -> None:
        while True:
            user_move = self._get_user_move()
            comp_move = self.get_computer_move()
            result = self.decide_winner(user_move, comp_move)

            self.player.record_result(result)
            print(f"\nYou: {user_move.name} | Computer: {comp_move.name} => {result.upper()}")
            print(self.player)
            print(self.player.get_feedback())

            if not self._handle_post_game():
                break

        self.auth.save_user(self.player)
        print("\nFinal stats saved... Bye")

if __name__ == "__main__":
    game = Game()
    game.login_or_register()
    game.game_loop()
