'''
Enumerate method deals with iterators, for counting number of iteration. Enumerate method help us do easily.
The enumerate() method adds a counter to an iterables and returns it in the form of an enumerating object.
This enumerate object can then be used directly for loops or converted into a list of tuples using list() function.

Syntax 
enumerate(iterable, start=0)
parameters
iterables = any object that supports iteration
start: the index value from which the counter is to be started, by default it is 0

'''
# x = [1,2,4,56,7]
# print(list(enumerate(x)))


animals = [
    'cat', 'dog', 'elephant', 'horse'
]

# for en in enumerate(animals):
#     print(en)


# for count, an in enumerate(animals):
#     print(count)


fruits = ['apple', 'banana', 'cherry']

en_fruit = enumerate(fruits)
next_fruit = next(en_fruit)
print(next(next_fruit))