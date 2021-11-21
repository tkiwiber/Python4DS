class Property:

    def __init__(self, worth):
        self.__worth = worth

    def tax(self):
        pass

    def get_worth(self):
        return self.__worth


class Apartment(Property):

    def __init__(self, worth):
        self.name = 'Apartment'
        Property.__init__(self, worth=worth)

    def tax(self):
        return self.get_worth() / 1000

    def __str__(self):
        return '-> {}: {}'.format(self.name, self.get_worth())


class Car(Property):

    def __init__(self, worth):
        self.name = 'Car'
        Property.__init__(self, worth=worth)

    def tax(self):
        return self.get_worth() / 200

    def __str__(self):
        return '-> {}: {}'.format(self.name, self.get_worth())


class CountryHouse(Property):

    def __init__(self, worth):
        self.name = 'CountryHouse'
        Property.__init__(self, worth=worth)

    def tax(self):
        return self.get_worth() / 200

    def __str__(self):
        return '-> {}: {}'.format(self.name, self.get_worth())


class Money(Property):

    def __init__(self, worth):
        self.name = 'Money'
        Property.__init__(self, worth=worth)

    def tax(self):
        return 0

    def __str__(self):
        return '-> {}: {}'.format(self.name, self.get_worth())


def create_property(obj_type, property_name):
    while True:
        print('Do you have {}?\n If yes, input cost otherwise input 0:'
              .format(property_name), end=' ')
        try:
            worth = float(input())
        except ValueError:
            print('Error! Must be float value.')
        if worth < 0:
            print('Error! Must be 0 or positive value.')
            continue
        elif worth == 0:
            return None
        else:
            new = obj_type(worth=worth)
            return new


def main():
    property_list = []
    print('Now please fill the form below.\n')
    property_list.append(create_property(obj_type=Apartment, property_name='apartment'))
    property_list.append(create_property(obj_type=Car, property_name='car'))
    property_list.append(create_property(obj_type=CountryHouse, property_name='country house'))
    property_list.append(create_property(obj_type=Money, property_name='money'))

    print('\nOk here is you property list. Lets see if you have enough money to pay all your taxes.')
    tax = 0
    money = 0
    for item in property_list:
        if item is not None:
            if item.name == 'Money':
                money = item.get_worth()
            print(item)
            tax += item.tax()
    print('Tax to be paid: ', tax)

    if money >= tax:
        print('\nIt seems you have enough money to pay taxes')
    else:
        print('\nUnfortunately, you dont have enough')


main()
