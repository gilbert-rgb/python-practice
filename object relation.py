# class GroceryItem:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

# class Shopper:
#     def __init__(self, name):
#         self.name = name
#         self.grocery_items = []
# shopper = Shopper("Alice")
# item1 = GroceryItem("apple", 1)
# item2 = GroceryItem("orange", 2)

# # Add the grocery items to the shopper's list
# shopper.grocery_items.append(item1)
# shopper.grocery_items.append(item2)

# # Print the shopper's grocery list
# for item in shopper.grocery_items:
#     print(item.name, item.price)

# => apple 1
# => orange 2


# class passport:
#     def __init__(self,passport_No):

#       self.passport_No = passport_No
#       self.owner = None
#     def assign(self,person):
#       self.owner = person
#       person.passport = self

#     def passInfo(self):
#       print(f"passport_No:{self.passport_No} owner:{self.owner}")

# class person:
#     def __init__(self,name):
#       self.name = name
#       self.passport = None
    

class Student:

  all = []
  def __init__(self,name,age):
    self.name = name
    self.age = age
    self._teacher = None
    Student.all.append(self)

  @property
  def teacher(self):
    return self._teacher
  @teacher.setter
  def teacher(self,value):
    if not isinstance(value, Teacher):
            raise TypeError("Teacher must be an instance of Teacher class")
    self._teacher = value

class Teacher:
    def __init__(self, name):
        self.name = name

    def students(self):
        return [student for student in Student.all if student.teacher == self]

    def add_student(self, student):
        if not isinstance(student, Student):
            raise TypeError("Student must be an instance of Student class")
        student.teacher = self

 