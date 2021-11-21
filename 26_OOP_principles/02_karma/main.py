from random import randint, choice
from os import path


class RandomKarmaException(Exception):

    exceptions = [
        'KillError',
        'DrunkError',
        'CarCrashError',
        'GluttonyError',
        'DepressionError'
    ]

    def __init__(self):
        message = choice(RandomKarmaException.exceptions)
        super().__init__(message)


class Buddhist:
    insight = 500

    def __init__(self):
        self.__current_day = 0
        self.set_karma(0)

    def one_day(self):
        self.__current_day += 1
        if randint(0, 10) == 0:
            self.set_karma(0)
            raise RandomKarmaException()
        return randint(1, 8)

    def set_karma(self, value):
        self.__karma = value

    def add_karma(self, value):
        self.__karma += value

    def get_karma(self):
        return self.__karma

    def get_day(self):
        return self.__current_day


def main():
    buddhist = Buddhist()

    while True:
        try:
            add_karma = buddhist.one_day()
        except RandomKarmaException as err:
            with open('karma.log', 'a') as file:
                file.write("Day {day}: exception={err}\n".
                           format(day=buddhist.get_day(), err=err))
            file.close()

        buddhist.add_karma(add_karma)
        print('Day {}. Karma: '.format(buddhist.get_day()), buddhist.get_karma())
        if buddhist.get_karma() > Buddhist.insight:
            print('Now you are Buddha! You are {} years old. But it doesnt matter'.format(round(buddhist.get_day()/365)))
            return 1
    return 0


main()
