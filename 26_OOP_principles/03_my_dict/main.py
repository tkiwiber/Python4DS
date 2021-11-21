class MyDict(dict):

    def __init__(self, *arg, **kw):
        super(MyDict, self).__init__(*arg, **kw)

    def get(self, key):
        try:
            result = self.__getitem__(key)
            return result
        except KeyError:
            return 0


a = MyDict()

a['1'] = 1
a['2'] = 2
a['3'] = 3

for key, value in a.items():
    print(key, value)

print()
print(a.get('4'))
