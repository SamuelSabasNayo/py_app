import utils

arr = [10, 3, 4, 12, 9, 8]

result = utils.find_max(arr)

print(result)


# from converters import kg_to_lbs

# my_weight = kg_to_lbs(80)

# print(my_weight)


# import converters

# my_weight = converters.kg_to_lbs(80)

# print(my_weight)

#######################################################################

# class Mammal:
#   def walk(self):
#     print("walk")


# class Dog(Mammal):
#   pass

# class Cat(Mammal):
#   def mao(self):
#     print('mao mao')
    
    
# cat1 = Cat()
# cat1.walk()


# class Person:
#   def __init__(self, name):
#     self.name = name
    
#   def talk(self):
#     print(f"Hi, I am {self.name}")


# person1 = Person("Sam Nayo")
# person1.talk()


# class Person:
#   def __init(self, name):
#     self.name = name
    
#   def talk(self):
#     print(f"Hi, I am {self.name}")
################################################## not working


# person1 = Person()
# person1.talk("Sam Nayo")


# class Person:
#   def __init(self, name):
#     self.name = name
    
#   def talk(self):
#     print('talk')


# person1 = Person()
# person1.name = 'Sam Nayo'
# print(person1.name)
# person1.talk()


# class Point:
#   def __init__(self, x, y):
#     self.x = x
#     self.y = y


# point = Point(10, 12) 
# print(point.x)

# class Point:
#   def move(self):
#     print('move')

#   def draw(self):
#     print('draw')


# point1 = Point()
# point1.move()
# point1.draw()
# -------------------------------

# try:
#   age = int(input('Age: '))
#   income = 10
#   risk = income / age
#   print(risk)
# except ZeroDivisionError:
#   print('Age cannot be 0.')
# except ValueError:
#   print('Invalid value')

  
# try:
#   age = int(input('Age: '))
#   print(age)
# except ValueError:
#   print('Invalid value')


# def greet_user(name):
#   print(f"Hi {name}!")
#   print('Welcome aboard.')
  
# greet_user("Sam")


# nums = [2,2,4,5,6,5,4,6,3]
# uniques = []

# for num in nums:
#   if num not in uniques:
#     uniques.append(num)
# print(uniques)


# nums = [3, 5, 6, 1, 10, 8, 6]
# max_num = nums[0]

# for num in nums:
#   if num > max_num:
#     max_num = num
# print(max_num)


# names = ['mimi', 'momo', 'mama', 'nana', 'nono', 'nunu']
# print(names[2: 4])


# names = ['mimi', 'momo', 'mama', 'nana', 'nono', 'nunu']
# print(names[2:])


# nums = [5, 2, 5, 2, 2]

# for i in nums:
#   print('X' * i)


# for x in range(4):
#   for y in range(3):
#     if x == y:
#       print(f"({x}, {y})")


# for x in range(4):
#   for y in range(3):
#     print(f"({x}, {y})")      


# prices = [10, 20, 40]
# total = 0

# for price in prices:
#   total = total + price
# print(f"The total: {total}")

# for item in range(4, 10, 2):
#   print(item)

  
# for item in range(5, 10):
#   print(item)

  
# for item in range(10):
#   print(item)

  
# for item in ['Python', 'Java', 'JavaScript', 'Ruby', 'C++']:
#   print(item)

  
# for item in 'Python':
#   print(item)


# command =  ""
# started = False

# while True:
#   command = input("> ").lower()
#   if command == "start":
#     if started:
#       print("Car is already started!")
#     else:
#       started = True
#       print("Car started ... Ready to go.")
#   elif command == "stop":
#     if not started:
#       print("Car is already stopped!")
#     else:
#       started = False
#       print("Car stopped.")
#   elif command == "help":
#     print(
#       '''
#       start - to start the car.
#       stop - to stop the car.
#       exit - to exit.
#       '''
#     )
#   elif command == "exit":
#     break
#   else:
#     print("I don't understand that...")


# secret_number = 9
# guess_count = 0
# guess_limit = 3

# while guess_count < guess_limit:
#   guess = int(input('Guess: '))
#   guess_count += 1
#   if guess == secret_number:
#     print('You won!')
#     break
# else:
#     print('Sorry, you failed!')

    
# secret_number = 9
# guess_count = 0
# guess_limit = 3

# while guess_count < guess_limit:
#   guess = int(input('Guess: '))
#   guess_count += 1
#   if guess == secret_number:
#     print('You won!')
#     break
#   else:
#     print('Sorry, you failed!')


# i = 1
# while i <= 5:
#   print(i)
#   i +=1


# weight = int(input('Weight: '))
# unit = input('(L)bs or (K)g: ')

# if unit.upper() == 'L':
#   converted = weight * 0.45
#   print(f"You are {converted} Kg")
# else:
#   converted = weight / 0.45
#   print(f"You are {converted} Lbs")

# name = 'Samuel'

# if len(name) < 3:
#   print('Name must be at least 3 characters')
# elif len(name) > 20:
#   print('Name must be a maximum of 20 characters')
# else:
#   print('Name looks good')


# temp = 35

# if temp != 30:
#   print("it's a hot day")
# else:
#   print("it's not a hot day")

# temp = 35

# if temp == 30:
#   print("it's a hot day")
# else:
#   print("it's not a hot day")

  
# temp = 35

# if temp >= 30:
#   print("it's a hot day")
# else:
#   print("it's not a hot day")

# has_high_income = True
# has_criminal_record = False

# if has_high_income and not has_criminal_record:
#   print('Eligible for loan')

  
# has_high_income = True
# has_good_credit = False

# if has_high_income or has_good_credit:
#   print('Eligible for loan')

  
# has_high_income = True
# has_good_credit = True

# if has_high_income and has_good_credit:
#   print('Eligible for loan')

# price = 100
# has_good_credit = False

# if has_good_credit:
#   down_payment = 0.1 * price
# else:
#   down_payment = 0.2 * price
# print(f"Down Payment: {down_payment}")


# is_hot = False
# is_cold = False

# if is_hot:
#   print("It's a hot day.")
#   print("Drink plenty of water")
# elif is_hot:
#   print("It's a cold day")
#   print("Wear warm clothes")
# else:
#   print("It's a lovely day.")
# print("Enjoy your day.")


# is_hot = False

# if is_hot:
#   print("It's a hot day.")
# print("Enjoy your day.")


# is_hot = True

# if is_hot:
#   print("It's a hot day.")
# print("Enjoy your day.")


# import math

# print(math.pow(4, 3))


# import math

# print(math.factorial(4))


# import math

# print(math.floor(2.9))


# import math

# print(math.ceil(2.9))

# x = - 2.9
# print(abs(x))


# x = 2.9
# print(round(x))


# x = 10
# x -=3

# print(x)


# x = 10
# x +=3

# print(x)


# powers
# print(10 ** 3)


# print(10 % 3)

#  to get integer
# print(10 // 3)

# print(10 / 3)


# course = 'Python for Beginners'
# print('python' in course)


# course = 'Python for Beginners'
# print('Python' in course)


# course = 'Python for Beginners'
# print(course.replace('Beginners', 'Absolute Beginners'))


# course = 'Python for Beginners'
# print(course.title())


# course = 'Python for Beginners'
# print(course.find('f'))


# course = 'Python for Beginners'
# print(course.upper())


# course = 'Python for Beginners'
# print(len(course))


# first = 'John'
# last = 'Smith'

# msg = f'{first} [{last}] is a coder'

# print(msg)

# course = 'Python for Beginners'
# another = course[:]

# print(another)

# course = '''
#   Hi John,
#   Here is our first email to you.
#   Thank you!!
# '''

# print(course)

# weight_kg = input('Weight (kg): ')
# weight_lbs = int(weight_kg) / 0.45

# print(weight_lbs)

# year = input('Birth year: ')
# print(type(year))
# age = 2021 - int(year)
# print(type(age))
# print(age)

# name = input('What is your name? ')
# color = input('What is your favorite color? ')
# print(name + ' likes ' + color)


# name = input('What is your name? ')
# print('Hello ' + name + '!')

# price = 100
# print(price)

# print('Hello Sam')

# Beignner thing
