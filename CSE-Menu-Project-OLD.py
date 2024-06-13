import tkinter as tk
from tkinter import *


#functions for tracing!
def EntreShow(var, indx, mode):
    global EntreSelect
    EntreSelect = EntreClicked.get()


def SideShow(var, indx, mode):
    global SideSelect
    SideSelect = SideClicked.get()


def DrinkShow(var, indx, mode):
    global DrinkSelect
    DrinkSelect = DrinkClicked.get()


def CondShow(var, indx, mode):
    global CondSelect
    CondSelect = CondClicked.get()


#Defining Vars!


EntreSelect = ""
SideSelect = ""
DrinkSelect = ""
CondSelect = ""
PriceLabel = ""
DiscLabel = ""
FinalLabel = ""
final_summary = ""


EntCheck = 0
DrinkCheck = 0
SideCheck = 0
Discount = 0


Eprice1 = 0
Eprice2 = 0
Eprice3 = 0
Eprice4 = 0


Sprice1 = 0
Sprice2 = 0
Sprice3 = 0
Sprice4 = 0
Sprice5 = 0
Sprice6 = 0
Sprice7 = 0


Dprice1 = 0
Dprice2 = 0
Dprice3 = 0
Dprice4 = 0
Dprice5 = 0
Dprice6 = 0
Dprice7 = 0
Dprice8 = 0
Dprice9 = 0
Dprice10 = 0


Cprice1 = 0
Cprice2 = 0
Cprice3 = 0


#Root Widget


root = tk.Tk()
root.title("Order Screen")
root.geometry("300x200")


#Lists with menu options!


EntreOpt = [
    "Chicken Sandwich: $3.99",
    "Cajun Filet Sandwich: $4.19",
    "Chicken Tenders 4pc: $4.55",
    "None"
]
SideOpt = [
    "Dirty Rice Single: $1.49",
    "Dirt Rice Picnic: $2.99",
    "Seasoned Fries Medium: $1.99",
    "Seasoned Fries Large: $2.99",
    "Mac N' Cheese Single: $1.49",
    "Mac N' Cheese Picnic: $2.99",
    "None"
]
DrinkOpt = [
    "Soft Drink Small: $1.59",
    "Soft Drink Medium: $1.89",
    "Soft Drink Large: $2.09",
    "Coffee Small: $1.29",
    "Coffee Regular: $1.49",
    "Coffee Large: $2.09",
    "Iced Tea Medium: $1.49",
    "Iced Tea Large: $2.09",
    "Iced Tea 1/2 Gallon: $3.39",
    "None"
]


copt = [
    "Ketchup Packet (3): $0.75",
    "Ranch Cup (3): 0.75",
    "None"
]


#function for the no button on root widget!
def No():
    root.destroy()


#Function to create and organize order widget!


def open_new_window():
    global EntreClicked, SideClicked, DrinkClicked
    ord_window = tk.Toplevel(root)
    ord_window.title("Meal Select")
    SelectLabel = tk.Label(ord_window, text="Select Your Meal!")
    SelectLabel.pack()
    Drop(ord_window)
     
#Function to order and create The DropDown menus and Submit Button, also traces the current selection!


def Drop(ord_window):
    global EntreClicked, SideClicked, DrinkClicked, CondClicked, EntCheck, SideCheck, DrinkCheck, Discount


    EntreClicked = StringVar()
    EntreClicked.trace('w', EntreShow)
    EntreClicked.set("Select Entree!")
    EntreDrop = OptionMenu(ord_window, EntreClicked, *EntreOpt)
    EntreDrop.pack()


    SideClicked = StringVar()
    SideClicked.trace('w', SideShow)
    SideClicked.set("Select Side!")
    SideDrop = OptionMenu(ord_window, SideClicked, *SideOpt)
    SideDrop.pack()


    DrinkClicked = StringVar()
    DrinkClicked.trace('w', DrinkShow)
    DrinkClicked.set("Select Drink!")
    DrinkDrop = OptionMenu(ord_window, DrinkClicked, *DrinkOpt)
    DrinkDrop.pack()


    CondClicked = StringVar()
    CondClicked.trace('w', CondShow)
    CondClicked.set("Select Condiment(s)!")
    CondDrop = OptionMenu(ord_window, CondClicked, *copt)
    CondDrop.pack()


    SubButton = tk.Button(ord_window, text="Finish Order!", command=open_total_window)
    SubButton.pack(pady=10)


#Function to create total order/final widget!


#Also has dictionary containing the str and float values for each selection, used to apply the combo discount!


def open_total_window():
    global EntreSelect, SideSelect, DrinkSelect, CondSelect, Discount
   
    total_window = tk.Toplevel(root)
    total_window.title("Total Order!")
    order_summary = f"Entree: {EntreSelect}\nSide: {SideSelect}\nDrink: {DrinkSelect}\nCondiment: {CondSelect}"
    TotalLabel = tk.Label(total_window, text=order_summary)
    TotalLabel.pack()


    price_dict = {
        "Chicken Sandwich: $3.99": 3.99,
        "Cajun Filet Sandwich: $4.19": 4.19,
        "Chicken Tenders 4pc: $4.55": 4.55,
        "Dirty Rice Single: $1.49": 1.49,
        "Dirt Rice Picnic: $2.99": 2.99,
        "Seasoned Fries Medium: $1.99": 1.99,
        "Seasoned Fries Large: $2.99": 2.99,
        "Soft Drink Small: $1.59": 1.59,
        "Soft Drink Medium: $1.89": 1.89,
        "Soft Drink Large: $2.09": 2.09,
        "Coffee Small: $1.29": 1.29,
        "Coffee Regular: $1.49": 1.49,
        "Coffee Large: $2.09": 2.09,
        "Iced Tea Medium: $1.49": 1.49,
        "Iced Tea Large: $2.09": 2.09,
        "Iced Tea 1/2 Gallon: $3.39": 3.39,
        "Ketchup Packet (3): $0.75": 0.75,
        "Ranch Cup (3): 0.75": 0.75
    }
   
    total_price = price_dict.get(EntreSelect, 0) + price_dict.get(SideSelect, 0) + price_dict.get(DrinkSelect, 0) + price_dict.get(CondSelect, 0)
   
    Discount = 0


    # Apply combo discount!


    if EntreSelect in ["Chicken Sandwich: $3.99", "Cajun Filet Sandwich: $4.19", "Chicken Tenders 4pc: $4.55"]:
        if SideSelect in ["Dirt Rice Picnic: $2.99", "Seasoned Fries Large: $2.99"] and DrinkSelect == "Iced Tea 1/2 Gallon: $3.39":
            Discount = 2
            DiscLabel = tk.Label(total_window, text="Combo Discount Applied!")
            DiscLabel.pack()


    total_price -= Discount
   
#Final price, thank you message, end button, and restart button!


    PriceLabel = tk.Label(total_window, text=f"Total Price: ${total_price:.2f}\nThank you for your order!")
    PriceLabel.pack(pady=10)


    FinishButton = tk.Button(total_window, text="Would you like to order again?", command=open_new_window)
    FinishButton.pack(pady=10)


    EndButton = tk.Button(total_window, text="End Program:(", command=root.destroy)
    EndButton.pack(pady=10)


#Objects for root widget!


TitleLabel = tk.Label(root, text="Welcome to Bojangles! May I Take Your Order?")
TitleLabel.pack(pady=10)


button = tk.Button(root, text="Yes!", command=open_new_window)
button.pack(pady=10)
nobutton = tk.Button(root, text="No :(", command=No)
nobutton.pack(pady=10)


#another function to quit the program... REDUNDANCY!!!!!!!!!!!!!!!!


def Quit():
    root.destroy


root.mainloop()


