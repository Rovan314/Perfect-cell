import random
from enum import Enum, auto


class Move(Enum):
    ROCK = auto()
    PAPER = auto()
    SCISSORS = auto()

    @staticmethod
    def from_input(inp):
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
    def __init__(self, name):
        self.name = name
        self.wins = 0
        self.losses = 0
        self.draws = 0

    def record_result(self, outcome):
        if outcome == "win":
            self.wins += 1
        elif outcome == "loss":
            self.losses += 1
        else:
            self.draws += 1

    def __str__(self):
        return f"{self.name} | Wins: {self.wins}, Losses: {self.losses}, Draws: {self.draws}"


class Game:
    def __init__(self):
        self.player = None

    def start(self):
        name = input("Enter your name: ").strip()
        self.player = Player(name)
        self.play_loop()

    def get_computer_move(self):
        return random.choice(list(Move))

    def decide_winner(self, user_move, comp_move):
        outcomes = {
            (Move.ROCK, Move.SCISSORS): "win",
            (Move.PAPER, Move.ROCK): "win",
            (Move.SCISSORS, Move.PAPER): "win",
            (Move.ROCK, Move.PAPER): "loss",
            (Move.PAPER, Move.SCISSORS): "loss",
            (Move.SCISSORS, Move.ROCK): "loss",
        }
        return "draw" if user_move == comp_move else outcomes.get((user_move, comp_move), "loss")

    def play_loop(self):
        while True:
            print("\nChoose your move: 1) Rock  2) Paper  3) Scissors")
            user_input = input("Your move: ")
            move = Move.from_input(user_input)

            if not move:
                print("Invalid input. Please enter 1/2/3 or rock/paper/scissors.")
                continue

            comp_move = self.get_computer_move()
            result = self.decide_winner(move, comp_move)

            print(f"\nYou: {move.name}, Computer: {comp_move.name}. Result: {result.upper()}")
            self.player.record_result(result)

            print(f"Stats: {self.player}")

            again = input("\nPlay again? (y/n): ").strip().lower()
            if again not in ("y", "yes"):
                print("\nFinal Stats:")
                print(self.player)
                break


if __name__ == "__main__":
    Game().start()