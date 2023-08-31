class Player:
    def __init__(self, player_name, data, score=0, lives=3):
        """ Initialize Player.

        :param player_name: string
        :param data: a PlayerData object
        :param score: int
        :param lives: int
        """
        self.__player_name = player_name
        self.data = data
        self.score = score
        self.lives = lives
        data.save_data(self)

    def __repr__(self):
        return f"Player(name={self.player_name}, score={self.score})"

    def add_score(self, score):
        """ Record player's score

        :param score: int
        """
        self.data.save_score(self, score)

    def add_lives(self, lives):
        """ Record player's lives

        :param lives: int
        """
        self.data.save_lives(self, lives)

    @property
    def player_name(self):
        return self.__player_name

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, s):
        if not isinstance(s, (int, float)):
            raise TypeError("score must be a number")
        self.__score = s

    @property
    def lives(self):
        return self.__lives

    @lives.setter
    def lives(self, l):
        if not isinstance(l, int):
            raise TypeError("lives must be a number")
        self.__lives = l
