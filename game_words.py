class Session:
    def __init__(self, players_list=None):
        self.game_data = {"counter": 0,
                          "players_list": {key.name: [] for key in players_list},
                          "all_words": []}

    def register_player_step(self, player_name: str, word: str):
        self.game_data["counter"] += 1
        self.game_data["players_list"][player_name].append(word)
        self.game_data["all_words"].append(word)

    def save_session(self):
        pass

    def __str__(self):
        return self.game_data

    # @staticmethod
    # def load_session():
    #     session = Session()
    #     session.game_data = {}
    #     return session


class Player:
    def __init__(self, name: str):
        self.words = 0
        self.name = name

    def __str__(self):
        return self.name


class GameValidation:
    def __init__(self, to_check: str):
        self.to_check = to_check.lower()

    def check_name(self):
        bad_symb = {"'", '"', "/", ",", ">"}  # just example
        if not self.to_check or set(self.to_check) & bad_symb:
            return False
        return True

    def check_word(self, word_list: list):
        if self.to_check in word_list or self.to_check[0] != word_list[-1][-1]:
            return False
        return True


class GameOver(Exception):
    def __init__(self, loser):
        self.loser = loser

    def __str__(self):
        return f"Game is over. {self.loser} lost"


def players() -> list:
    players_list = []
    while True:
        name_inp = input("Input player name(start for game): ")
        if name_inp.lower() == "start":
            return players_list
        elif not GameValidation(name_inp).check_name():
            print("Bad player name. Try again")
        else:
            players_list.append(Player(name_inp))
            print(f"Player {name_inp} added. Input next or start")


def circle(session: Session):
    pl_list = list(session.game_data['players_list'].keys())
    word_list = session.game_data['all_words']
    for player in pl_list:
        word = input(f"{player}, input word: ").lower()
        if word == "stop game":
            raise GameOver(player)
        if word == "game later":
            session.save_session()
        if not word_list:
            session.register_player_step(player, word)
        else:
            word_isvalid = GameValidation(word).check_word(word_list)
            if word_isvalid:
                session.register_player_step(player, word)
            else:
                raise GameOver(player)
    return True


def game():
    start_game = input("Start new game(new), or load previous(prev):").lower()
    if start_game == "new":
        session = Session(players())
    elif start_game == "prev":
        session = Session.load_session()
    else:
        print("Try start again.")
        return
    while True:
        try:
            circle(session)
        except GameOver as e:
            print(e)
            return


if __name__ == '__main__':
    game()