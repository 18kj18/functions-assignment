import random

def q118():
    '''Question 118'''
    def number():
        return int(input("Enter a number --> "))

    def count_to_number(x):
        count = 0
        while count <= x:
            print(count)
            count +=1
    
    countToNumber(number())
            


def Q119():
    '''Question 119'''
    def random_number():
        return random.randint(int(input("Enter the first number --> ")), int(input("Enter the second number --> ")))
    
    def guess_number():
        return int(input("Guess whant number im thingink of -->"))
    
    def check_number(comp_num, inp):
        if comp_num == inp:
            print("Correct, you win!")
        else:
            print("Incorrect, try again")
            self.check_number(comp_num, guess_number())

    check_number(self.random_number(), guess_number())

def q120():
    '''Question 120'''
    
    
    