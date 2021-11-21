from random import randint


class Warrior:
    name = 'Воин'
    health = 100
    hit = 20

    def __init__(self, index):
        self.index = index

    def is_alive(self):
        if self.health <= 0:
            return False
        return True


class WarriorsRaw:

    def __init__(self, count):
        self.warriors = [Warrior(index) for index in range(1, count + 1)]
        self.count = count

    def show_warriors(self):
        print('Current raw of warriors:')
        for warrior in self.warriors:
            print(warrior.name, warrior.index)

    def random_attack(self):
        unit_index = randint(1, self.count)
        print('random index = {}'.format(unit_index))
        for warrior in self.warriors:
            if warrior.index != unit_index:
                warrior.health -= Warrior.hit
                print('[Warrior {}] hits [Warrior {}].'.
                      format(unit_index, warrior.index), end=' ')
                print('[Warrior {}] has {} HP\n'.
                      format(warrior.index, warrior.health))

    def show_winners(self):
        print('The winner(s): ', end='')
        print(', '.join(' '.join([warrior.name, str(warrior.index)])
                      for warrior in self.warriors if warrior.health > 0))

    def someone_dead(self):
        if not all([i_warrior.is_alive() for i_warrior in self.warriors]):
            return True
        return False
