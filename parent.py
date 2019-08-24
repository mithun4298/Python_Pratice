# class Parent:
#     def __init__(self,name):
#         print("constructor of the Parents class",name)
# class Child(Parent):
#     def __init__(self):
#         print("This is the child class constructor")
#         super().__init__("mithun")    #super is the function called the
#                                         #parents class method to the child classs
# child=Child()
# print(Child.__mro__) #how it calling to in the class

#...........................................................................................
                #.............Multiple Inheritance concept
class Parent1:
    def __init__(self,name):
        print("constructor of the Parents 1 class",name)
                                                                # class Parent4:
                                                                #     def __init__(self,name):
                                                                #         print("constructor of the Parents 4 class",name)
                                                                # class Parent5:
                                                                #     def __init__(self,name):
                                                                #         print("constructor of the Parents 5 class",name)
                                                                # class Parent3(Parent5,Parent4):
                                                                #     def __init__(self,name):
                                                                #         print("constructor of the Parents 3 class",name)

class Parent2:
    def __init__(self,name):
        self.name = name
        print("constructor of the Parents 2 class",self.name)
    def name1(self):
        print(self.name)
class Child(Parent1, Parent2):  #first will be called first2
    def __init__(self):
        print("This is the child class constructor")
        Parent2.__init__(self,'mummy')
        Parent1.__init__(self,'papa ')
        # super().__init__("mithun")
        # super().__init__("ram")
        # super().__init__("shyam")
        # '''this will called only one parents class constructor
        #if waant to claa the both the class constructor or method then we have to call by the parents
        # class name and there have to call
         #super is the function called the
                                        #parents class method to the child classs
child=Child()
child.name1()
print(child.name)
print(Child.__mro__) #method resolution ordr how it calling to in the class