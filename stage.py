import random
from turtle import Turtle, Screen
from coin import Coin
from coinbank import CoinBank


class Stage:
    def __init__(self):
        self.__painter = Turtle()
        self.__screen = Screen()
        self.__coin = []
        self.__debt = []
        self.__coinbank = CoinBank()

    def init_screen(self):
        """ Initialize a screen to display the game.

        """
        self.__painter.hideturtle()
        self.__painter.penup()
        self.__screen.setup(800, 600)
        self.__screen.bgpic("pic/BG.gif")
        self.__screen.tracer(0)
        self.__screen.listen()
        self.__screen.onkeypress(self.__coinbank.move_left, "Left")
        self.__screen.onkeypress(self.__coinbank.move_right, "Right")

    def add_coin(self):
        """ Add coins to the lists, number of coins will random.

        """
        for _ in range(random.randint(6, 10)):
            coin = Coin()
            coin.draw("Yellow")
            self.__coin.append(coin)

        for _ in range(random.randint(3, 5)):
            debt = Coin()
            debt.draw("Red")
            self.__debt.append(debt)

    def check_collision(self, player):
        """ Move all coins in lists

        :param player: a Player object
        """
        while True:
            x, y = self.__coinbank.pos()
            self.__painter.goto(-360, 230)
            self.__painter.write(f"collect: {player.score} $ lives: {player.lives}", font=("VT323", 30, "normal"),
                                 move=True)
            self.__screen.update()
            self.__painter.clear()
            for coin in self.__coin:
                coin.move(x, y, player, "pic/dollar.gif")

            for debt in self.__debt:
                debt.move(x, y, player, "pic/debt.gif")

            if player.lives <= -1:
                break

    @property
    def painter(self):
        return self.__painter

    @property
    def screen(self):
        return self.__screen
