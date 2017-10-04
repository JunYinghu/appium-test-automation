from Game import game


class MyClass(object):
    gamenew = game()

    def executegame(self):
        self.gamenew.gamce()
        print 'test'


if __name__ == '__main__':
    a = MyClass()
    a.executegame()
