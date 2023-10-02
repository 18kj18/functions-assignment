import random

def question118():
    '''Question 118'''
    def number():
        return int(input("Enter a number --> "))

    def countToNumber(x):
        count = 0
        while count <= x:
            print(count)
            count +=1
    
    countToNumber(number())
            


def question119():
    '''Question 119'''
    def randomNumber():
        comp_num = random.randint(int(input("Enter the first number --> ")), int(input("Enter the second number --> ")))

    def guessGame(num):
        inp = int(input("Guess whant number im thingink of -->"))
    
    guessGame(randomNumber())