'''
#NOTE:The concept of inheritance is same as in other programming language.But the syntax is 
      different
NOTE: There are total - 5 types of inheritance in Python :

    1) single inheritance : inheritance in which there is only one base class and derived class

            structurally : base ----> derived

    2)multiple inheritance : inheritance in which there is more than two base class and only one
                                derived class

            structurally : base1     base2
                            |          |
                            |          |
                            Derived class
                    
    3)multi-level inheritance : inheritance in which a class is derived from another derived class

            structually : Grandparent --> parent ---> child

    4)hierarchial inheritance : inheritance in which more than one derived class are derived from
                                a single base class.

            structually :            Base class
                                    |          |
                                    |          |
                                derived1    derived2           
                                    
            
    5)hybrid inheritance : inheritance which is mixture of hierarchial inheritance and multiple
                            inheritance.

            structually :             Base class                       -->also arise diamond problem
                                    |          |
                                    |          |
                   derived1/base class1      derived2/base class2

                                  |              |
                                  |              |
                                    Derived class

''' 



'''
NOTE:  Multiple Inheritance Conflict (Diamond Problem):

    1) C++ uses virtual inheritance to solve ambiguity.

    2)Python uses MRO (Method Resolution Order) and C3 linearization to resolve which parent is called first.

NOTE: Polymorphism with Inheritance:

    1)C++: requires virtual functions for runtime polymorphism.

    2)Python: all methods are virtual by default, so polymorphism is natural.

    
'''

