'''
Garbage collection(GC) is a memory recovery feature built into programming lanuage such as c# and java.
A GC enabled programming language includes one or more garbage collector(GC engines) that automatically
free up memory space that has been allocated to objects no longer needed by the program. The reclaimed memory space can then be used for future object allocations within 
that program.
Garbage collection ensures that a program doesnot exceed its memory quota or reach a point that it can no longer function. It also frees up developers from having manuall manage to program memory, which in turn
reduces the potential for memory-related bugs.

In older programming languages such as c and c++ the developer should manually delete objects and free up memory. Relying manual processes made it easy to 
introduce bugs in code, some of which have some serious consiquences.
It leads to memory leakage that quickly consumes the available RAM. 
It is also a ungoing process which requires CPU resources. so, some developer debate that GC benifits. believing that they can better control memory deallocation than an automated process.
'''

obj1= {"name": "tyagi"}
obj2 = obj1
del obj1
obj2 = 'hello' # here even obj2 is referenced to obj1. which is not needed to so it is garbage collected and deleted as nothing is pointing to it.
print(obj2)
print(obj1)
# 


# Here in the above program the obj1 is deleted but we can get obj2 referenced to the obj1