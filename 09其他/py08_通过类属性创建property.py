class Foo:
    def get_bar(self):
        return 'hello world'

    def set_bar(self, vlaue):
        print(vlaue)

    def del_bar(self):
        print('del')

    bar = property(get_bar, set_bar, del_bar, 'desc')


f = Foo()

print(f.bar)
f.bar = 'a'
del f.bar
print(f.bar.__doc__)


