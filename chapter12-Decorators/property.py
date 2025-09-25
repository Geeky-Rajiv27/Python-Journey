'''
NOTE: getter is a method like type of property that allows us to read the private data 

NOTE: setter is method like type of property that allows us to set value (update) of the private 
      data

NOTE: Setter must be same as getter
'''



'''------------------------------------------------------------------------------------------
3️⃣ With getter and setter

We make the variable private (self.__balance) and provide methods to access or change it safely.

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # private variable

    # Getter (to read value)
    def get_balance(self):
        return self.__balance

    # Setter (to update value safely)
    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("❌ Balance cannot be negative")

acc = BankAccount(1000)
print(acc.get_balance())   # ✅ 1000
acc.set_balance(2000)      # ✅ updated
print(acc.get_balance())   # ✅ 2000
acc.set_balance(-500)      # ❌ invalid

4️⃣ Python shortcut: @property

Python has a neat feature → we can write getters/setters like normal attributes using @property.

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    @property
    def balance(self):   # Getter
        return self.__balance

    @balance.setter
    def balance(self, amount):  # Setter
        if amount >= 0:
            self.__balance = amount
        else:
            print("❌ Balance cannot be negative")

acc = BankAccount(1000)
print(acc.balance)     # looks like attribute but calls getter      #no need to use as methods like ()
acc.balance = 2000     # looks like attribute but calls setter      #no need to set as method() = value (no use of ())
print(acc.balance)     # 2000
acc.balance = -500     # ❌ invalid

5️⃣ Simple definition

Getter → Method that lets you read a private variable.

Setter → Method that lets you update a private variable safely.

Importance → Protects data, adds rules/validations, hides internal details.
------------------------------------------------------------------------------------------
'''

'''
------------------------------------------practice question no. 1 --------------------------------------------------
Create a class Student with a private attribute __age.
1) Use a getter to fetch the age .
2) Use a setter to set the age, but make sure age cannot be less than 5.
3) Test it by creating a student object and trying to set valid and invalid ages.
----------------------------------------------------------------------------------------------------------------
'''


class Student:
    def __init__(self, age):
        self.__age = age

    @property       # this make this method a getter attribute
    def age(self):
        return self.__age 

    @age.setter
    def age(self, a):
        if(a >= 18):
            self.__age = a
        else:
            print("Please enter age above or equal to 18")

s1 = Student(17)    # This is like setting age using class constructor so no need to check conditions
                    #accessing private data using class objects
print(s1.age)


#now setting new data using (setter) attribute like method
s1.age = 15     #-->❌. not allowd since condition is not satisfied. Hence shows same output : 17
print(s1.age)

#NOTE : CASE : when we set correct age it will update output to 19
s1.age = 19
print(s1.age)

 

'''------------------------------------------practice question no. 2 --------------------------------------------------
    Create a class BankAccount with a private attribute __balance
    1) Provide a getter to see the balance
    2) Provide a setter that only allows balance to be updated if the amount is non-negative
    3) Try to set balance to -1000 and check if your setter prevents it.
----------------------------------------------------------------------------------------------------------------
'''

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    @property   #getter
    def balance(self):
        return self.__balance
    
    @balance.setter     #setter
    def balance(self, amount):
        if(amount > 0):
            self.__balance = amount
        
        else:
            print("Please enter amount greater than Rs 0 ")

b = BankAccount(1000)
print(b.balance)    #private member through setter can be accessed by using own class object

b.balance = 100
print(b.balance)

b.balance = -1  #This is not allowd since setter's condition is not satisfied
print(b.balance)    #so this will show last output that is (100)



'''------------------------------------------practice question no. 3 --------------------------------------------------
Create a class laptop with private attributes __brand and __price.
    1) Use getters to fetch brand and price.
    2) Use setters to update price, but ensure.
        a) Price cannot be less than 200
        b) Once brand is set, it cannot be changed(read-only after initialization)

    3) Create an object, set its brand and price, then try updating both values to test your getter & setter logic.
----------------------------------------------------------------------------------------------------------------
'''

class laptop:
    def __init__(self, brand, price):
        self.__brand = brand
        self.__price = price

    @property
    def brand_price(self):
        return (self.__brand, self.__price)
    
    @brand_price.setter
    def brand_price(self, amount):
        if(amount >= 200):
            self.__price = amount

        else:
            print("Price must be greater than or equal to 200")

l = laptop("Hp", 250000)
print(l.brand_price)
print("\n")

l.brand_price = 3000000
l.__brand = "ASUS"  #This is not allwod since it is private and can only be done via setter attribute like methods
print(l.brand_price)    #output = Hp, 300000

