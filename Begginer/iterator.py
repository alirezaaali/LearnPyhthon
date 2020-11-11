'''
Here is some useful  methods
You can find more information in
https://www.w3schools.com/python/python_iterators.asp

Technically, in Python, an iterator is an object which implements the iterator protocol, 
which consist of the methods __iter__() and __next__().

Iterator vs Iterable
Lists, tuples, dictionaries, and sets are all iterable objects. 
They are iterable containers which you can get an iterator from.
All these objects have a iter() method which is used to get an iterator:
'''

mytuple = ('Ali', 'Alireza', 'Behnaz', 'Hananh', 'Charli')
myIterator = iter(mytuple)
print(next(myIterator))
print(next(myIterator))
print(next(myIterator))
print(next(myIterator))
print(next(myIterator))


myString = "I am from Tehran"
myIter = iter(myString)
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))


# The for loop actually creates an iterator object and executes the next() method for each loop.
for x in mytuple:
    print(x)

for y in myString:
    print(y)


class myclass:
    def __init__(self, bn, itn):
        self.bn = bn
        self.itn = itn

        pass

    def __iter__(self):
        self.a = self.bn
        return self

    def __next__(self):
        if self.a <= 1299:
            x = self.a
            self.a += self.itn
            return x
        else:
            raise StopIteration


z = myclass(1, 4)
myit = iter(z)

for x in myit:
    print(x)
