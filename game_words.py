class Session:
    def __init__(self, players_list):
        self.game_data = {}
        self.pl_list = players_list


class Player:
    def __init__(self, name: str):
        self.words = 0
        self.name = name


def players() -> list:
    players_list = []
    while True:
        name_inp = input("Input player name(start for game): ")
        if name_inp.lower() == "start":
            return players_list
        elif not name_inp:
            print("Player's name can't be empty. Try again")
        else:
            players_list.append(Player(name_inp))
            print(f"Player {name_inp} added. Input next or start")


def circle(session: Session, first_word=False):
    for player in session.pl_list:
        if first_word:
            word = input(f"Okay, {player}, input first word: ")
        # else:


def game():
    session = Session(players())
    return "Game started!"


