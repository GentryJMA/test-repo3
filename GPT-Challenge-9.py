#rectangle area/perimeter calculator
leng = 0
widt = 0

#class which defines the rectangle itself, and the operations of area and distance
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

def inputs(leng, widt):


    leng = int(input('Enter Length: '))
    widt = int(input('Enter Width: '))
    return Rectangle(leng, widt)


def operations(rect):
    user_choice = input('Would you like to calculate Area or Perimeter? ')
    user_choice = user_choice.lower()
    if user_choice == 'area':
       print(f'Area: {rect.area()}')
       user_restart = input('Would you like to go again? (Yes/No)')
       user_restart = user_restart.lower()
       if user_restart == 'yes':
            rect = inputs(leng,widt)
            operations(rect)
       else:
           print('Thank You!')
    else:
        if user_choice == "perimeter":
            print(f'Perimeter: {rect.perimeter()}')
            user_restart = input('Would you like to go again? (Yes/No)')
            user_restart = user_restart.lower()
            if user_restart == 'yes':
                rect = inputs(leng,widt)
                operations(rect)
            else:
                print('Thank You!')
        else:
            print('Invalid Option') 


#calls the functions to start the loop
rect = inputs(leng, widt)
operations(rect)




