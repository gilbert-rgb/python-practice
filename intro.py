# #name = "chebson"
# #is_employee = True
# #gpa = 20.4
# #age = 32


# #age = str(age)
# #print(age)

# #mylist = ['apple', 'banana', 'cherry']
# #print(len (mylist))

# #Print the second item in the fruits list.


# #fruits = ["apple", "banana", "cherry"]
# #print(len(fruits[1]))
# #print(1**21)

# def add_number(n1,n2):
#     results = n1 + n2
#     return results
# number1 = 5.7
# number2 = 6.4
# results = add_number(number1,number2)
# print("the sum is", results)



# def my_function():
    
#     print("Hello World")

# my_function()
 
# #Arguments and parameters
# def  my_function(fname,lname):
#     print(fname + " "+ lname)

# my_function("gilbert","cheboi")    

# #Arbitrary Arguments, *args


# def my_function(*kids):
#   print("The youngest child is " + kids[2])

# my_function("Emil", "Tobias", "Linus")

# #Keyword Arguments
# def my_function(child3, child2, child1):
#   print("The youngest child is " + child1)
#   print("The youngest child is " + child2)
#   print("The youngest child is " + child3)

# my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")


# # Arbitrary Keyword Arguments, **kwargs
# def my_function(**kid):
#   print(f"His last name is " + kid["lname"])

# my_function(fname = "Tobias", lname = "Refsnes")
# # Default Parameter Value
# def my_function(country = "Norway"):
#     print("i am from"+ " " +country)
# my_function("Brazil")
# my_function()   
# my_function("kenya")   
# my_function("Tanzania")       


# print( type(7//5))


#conditional
# age = 100
# if age >= 18 and age <= 100:
#     print("adult")

# elif age < 18:

#     print("minor")  

# elif age == 18:
#     print("just adult") 
# else:
#     print("invalid input")         



# # loops : for && while
# fruits = ["Apples","Mangoes", "Bananas"]
# for x in fruits:
#     print(x)

marks = 1
while marks < 100:
    if marks >= 0 and marks<40:
       print(marks,"fail")
    elif marks >=40 and marks<=49:
        print(marks,"D")
    elif marks >=50 and marks<=59:
        print(marks,"C")
    elif marks >=60 and marks<=69:
        print(marks,"B")
    
    marks = marks+ 1