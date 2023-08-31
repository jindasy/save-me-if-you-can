from turtle import Turtle


class CoinBank:
    def __init__(self):
        """ Initialize coin bank from turtle.

        """
        self.__bank = Turtle()
        self.__bank.speed(0)
        self.__bank.screen.register_shape("pic/bank.gif")
        self.__bank.shape("pic/bank.gif")
        self.__bank.penup()
        self.__bank.goto(0, -260)

    def move_left(self):
        """ Move coin bank to left.

        """
        self.__bank.setheading(180)
        self.__bank.setx(self.__bank.xcor() - 20)
        # check screen collision.
        if self.__bank.xcor() <= -380:
            self.__bank.setx(-380)

    def move_right(self):
        """ Move coin bank to right

        """
        self.__bank.setheading(0)
        self.__bank.setx(self.__bank.xcor() + 20)
        # check screen collision.
        if self.__bank.xcor() >= 380:
            self.__bank.setx(380)

    def pos(self):
        """ Get position of coin bank.

        :return: tuple
        """
        return self.__bank.xcor(), self.__bank.ycor()

    @property
    def bank(self):
        return self.__bank
