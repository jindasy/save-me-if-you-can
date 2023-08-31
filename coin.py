from turtle import Turtle
import random


class Coin:
    def __init__(self):
        self.__coin = Turtle()

    def __repr__(self):
        return f'Coin(x="{self.__coin.xcor()}", y="{self.__coin.ycor()}")'

    def draw(self, color):
        """ Draw coins in random position.

        :param color: string
        """
        self.__coin.screen.register_shape("pic/dollar.gif")
        self.__coin.screen.register_shape("pic/debt.gif")
        self.__coin.penup()
        self.__coin.speed(0)
        self.__coin.goto(random.randint(-370, 370), random.randint(300, 350))
        self.__coin.color(color)
        self.__coin.setheading(270)

    def move(self, x, y, player, shape):
        """ Move coin falling from the top of the screen.

        :param x: int
        :param y: int
        :param player: a Player object
        :param shape: string
        """
        self.__coin.shape(shape)
        self.__coin.forward(random.uniform(0.5, 1.5))
        if abs(self.__coin.xcor() - x) < 30 and abs(self.__coin.ycor() - y) < 30:
            if shape == "pic/dollar.gif":
                score = 10
                player.add_score(score)
                self.__coin.goto(random.randint(-380, 380), random.randint(230, 350))
            elif shape == "pic/debt.gif":
                lives = -1
                player.add_lives(lives)
                self.__coin.goto(random.randint(-380, 380), random.randint(230, 350))
        elif self.__coin.ycor() <= -300:
            self.__coin.goto(random.randint(-380, 380), random.randint(230, 350))

    @property
    def coin(self):
        return self.__coin
