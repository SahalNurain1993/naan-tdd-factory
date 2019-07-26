##Function principles
#functions only do one job
#fucntions should be unitary
#fuctions should do the above so that they are testable
#do not print inside functions, you return
# functions need to be called

#unit test
#these are tests that test 1 function

# TDD - Test driven development
# write your tests, according to specs
# then follow the errors and iterate until test pass

def say_hello():
    return 'hello'

print(say_hello())

def say_hello_personal(name_arg):
    return 'hello ' + name_arg
print(say_hello_personal('Isabella Jones'))

##Testing
#has two main sections: setup and evaluation
#you give it controlled input and test for expected outcome

setup_result = say_hello()
print(setup_result=='hello')

#test 2 -testing say_hello_personalize function
# print("test say_hello_personal function, when called should take in one argument and return string 'hello ' + argument")
# print('testing with isabella')

#### test 3 -testing  fucntion full_name_hello
print("calling fuction full_name_hello () with isabella jones, expect 'hello Isabella Jones' to be printed")
print(full_name_hello ('isabella')



