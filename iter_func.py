'''
python iter()
The iter() method returns an iterator for the argument.
'''
# phones = ["apple", "samsung", "oneplus"]
# phones_iter = iter(phones) #This is a object which can be accessed with next method
# print(next(phones_iter))

class PrintNumber:
    def __init__(self, max):
        self.max = max
    
    def __iter__(self):
        self.num = 0
        return self
    
    def __next__(self):
        if(self.num>=self.max):
            raise StopIteration
        self.num+=1
        return self.num
    

print_num=PrintNumber(3)
print_num_iter = iter(print_num)
print(next(print_num_iter))