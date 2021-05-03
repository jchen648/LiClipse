# def print_hello_world():
#     print("Hello world!")
# 
# print_hello_world()


# def print_hello_yourname(name="Default User"):
#     print("Hello "+name+ "!")
# 
# name = input("What is your name?")    
# print_hello_yourname(name)

# def print_greeting_yourname(greeting,name):
#     print(greeting + " " +name+"!")
#     
# name = input("What is your name?")  
# greeting = input("What is your favorite way to say hello?")  
# 
# print_greeting_yourname(greeting,name)

def secret_code(number):
    number = number * 5
    number = number + 1111111
    number = number / 3
    number = number * 9
    return number

number = 122
secretNumber = secret_code(number)
second_SN = print(secretNumber+3)
print(secretNumber)
