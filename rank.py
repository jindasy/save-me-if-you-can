import json


class Rank:
    def __init__(self):
        self.__player_data = {}
        self.__score_list = []

    def player_rank(self):
        """ Open data and sort player's rank.

        :return: dict
        """
        with open("data.json", "r") as f:
            data = json.load(f)

        # sort all score from largest to smallest.
        for name in data:
            if data[name]["score"] not in self.__score_list:
                self.__score_list.append(data[name]["score"])
            self.__score_list.sort(reverse=True)

        # get rank from index of score list.
        for name in data.keys():
            score = data[name]["score"]
            rank = self.__score_list.index(score) + 1
            # add new key-value pair to player data, if key is already exist append player name to name list instead.
            if f'Rank{self.__score_list.index(score)+1}' not in self.__player_data:
                self.__player_data[f'Rank{rank}'] = [{'name': [name]}, {'score': score}]
            elif f'Rank{self.__score_list.index(score)+1}' in self.__player_data:
                py_name = self.__player_data[f'Rank{rank}'][0]['name']
                py_name.append(name)
        return self.__player_data

    def find_rank(self, name):
        """ Find rank of specified player name.

        :param name: string
        :return: string
        """
        self.player_rank()  # sort player before find rank
        for key, val in self.__player_data.items():
            if name in val[0]['name']:
                return key

    @property
    def player_data(self):
        return self.__player_data

    @property
    def score_list(self):
        return self.__score_list
