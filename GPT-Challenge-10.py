class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def set_car(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def display_car_info(self):
        print(f'Make: {self.make}, Model: {self.model}, Year: {self.year}')
    def search_car(self, search_term, attribute):
        if attribute == 'make' and self.make.lower() == search_term.lower():  # Fixed comparison
            return True
        elif attribute == 'model' and self.model.lower() == search_term.lower():  # Fixed comparison
            return True
        elif attribute == 'year' and self.year == int(search_term):  # Fixed comparison
            return True
        return False

        

def main():

    car =Car('Unknown', 'Unknown', 0)

    while True:
        print("\nMenu")
        print('1. Set Car Info')
        print('2. Display Car Info')
        print('3. Exit Program')
        print('4. Search for Car')

        choice = input('Enter Choice: ')
        
        if choice == '1':
            make = input('Enter Make: ')
            model = input('Enter Model: ')
            year = int(input('Enter Year'))
            car.set_car(make, model, year)
        elif choice == '2':
            car.display_car_info()
        elif choice == '3':
            break
        elif choice == '4':
            search_term = input('Enter search term: ')
            attribute = input('Search by (make/model/year): ').lower()
            if car.search_car(search_term, attribute):
                car.display_car_info()
            else:
                print('Car not found.')

        else:
            print('Invalid Option. Goodbye.')

            

main()