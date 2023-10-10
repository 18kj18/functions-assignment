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
    
    count_to_number(number())
            


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
    def get_input():
        inp = int(input("1) Addition\n2) Subtraction\n-->")) == 1
        if inp == 1:
            addition()
        elif inp == 2:
            subtraction()
        else:
            print("Please select one of the options listed\n\n")
            get_input()
            
    def addition():
        num1 = random.randint(5,20)
        num2 = random.randint(5,20)
        
        addedValue = num1 + num2
        
        if int(input(f"What is the value of {num1} + {num2}\n-->")) == addedValue:
            print("Congratulations, you got it!")
        else:
            print(f"Incorrect! The correct answer was {addedValue}")
            
    def subtraction():
        num1 = random.randint(25,50)
        num2 = random.randint(1,25)
        
        subtractValue = num1 - num2
        
        if int(input(f"What is the value of {num1} - {num2}\n-->")) == subtractValue:
            print("Congratulations, you got it!")
        else:
            print(f"Incorrect! The correct answer was {subtractValue}")
            
    get_input()
    
def q121():
    '''Question 121'''
    names = []
    
    def get_input():
        inp = int(input(f"1) Add a name to the list\n2) Change a name in the list\n3) Delete a name in the list\n4) View all names in the list -->"))
        match inp:
            case 1:
                add_name()
            case 2:
                change_name()
            case 3:
                delete_name()
            case 4:
                show_name()
            case _:
                print("Enter a valid input")
                get_input()
                
    def add_name():
        inp = str(input("Enter the name you would like to add -->"))
        names.append(inp)
        get_input()
    
    def change_name():
        inp = int(input("Which name would you like to edit (numbered from 0) -->"))
        inp2 = str(input("Make changes -->"))
        names[inp] = inp2
        get_input()
        
    def delete_name():
        inp = int(input("What owuld you like to ppopopo -->"))
        names.pop(inp)
        get_input()
        
    def show_name():
        print(names)
        get_input()
        
    get_input()
    
def q122():
    '''Question 122 and Question 123'''
    def get_input():
        inp = int(input(f"1) Add to file\n2) View all records\n3) Delete a record\n4) Quit program\n--> "))
        match inp:
            case 1:
                add_to_file()
            case 2:
                view_records()
            case 3:
                delete_record()
            case 4:
                quit()
            case _:
                print("Enter a valid input")
                get_input()
    
    def add_to_file():
        with open('salaries.csv', 'a') as file:
            name = input("Enter your name --> ")
            salary = int(input("Enter your salary -->"))
            file.write(f"{name}, {salary}\n")
        get_input()

    def view_records():
        with open('salaries.csv', 'r') as file:
            print(file.readlines())
        get_input()
        
    def delete_record():
        inp = int(input("Which record would you like to delete? -->"))
        with open('salaries.csv', 'r') as file:
            lines = []
            count = 0
            for line in file:
                print(count, inp)
                print(line)
                if inp != count:
                    print("hooray")
                    lines += line
                    
                    
                count += 1
        with open('salaries.csv', 'w') as file:
            for line in lines: 
                file.write(line)           
            
        get_input()
        
    get_input()
    