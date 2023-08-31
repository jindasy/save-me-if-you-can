import json


class PlayerData:
    def __init__(self, name):
        """ Initialize data of the player with the given name.

        :param name: string
        """
        self.__name = name

    def __repr__(self):
        return f'PlayerData(name="{self.__name}")'

    def save_data(self, player):
        """ Open, read and write new data to data file.

        :param player: a Player object
        """
        new_data = {
            player.player_name: {
                "score": player.score,
                "lives": player.lives
            }
        }
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

    def save_score(self, player, score):
        """ Update player's score with the new score.

        :param player: a Player object
        :param score: int
        """
        player.score += score
        self.save_data(player)

    def save_lives(self, player, lives):
        """ Update player's lives with the new lives.

        :param player: a Player object
        :param lives: int
        """
        player.lives += lives
        self.save_data(player)

    @property
    def name(self):
        return self.__name
