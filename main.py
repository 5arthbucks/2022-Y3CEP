# this is an inventory management system for specialists and cadet officers in RINCC to keep track of the items that are in the RINCC armory,
# as well as what has been used for training sessions so as to keep track of all the items throughout the year.

class Item: #define the class and the properties that the item has
    def __init__(self, name, quantity, desc, dateAdded, loan):
        self.name = name
        self.quantity = quantity
        self.desc = desc
        self.dateAdded = dateAdded
        self.loan = loan

itemLog = [] #create an array to store all the items
months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'] #possible months for date input
days = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'] #possible days for date input

def addItem():
    name = str(input("Name of item to be added: "))
    quantity = int(input("Quantity of item to be added: "))
    for item in itemLog:
        if name == item.name:
            item.quantity += quantity #check whether item already exists and if so add on the quantity to that item
            return #if item already exists then exit function prematurely as nothing further has to be keyed in
    desc = str(input("Description of item to be added: "))
    dateAdded = str(input("Date on which item is added (dd/mm/yy): "))
    while len(dateAdded) != 8 or dateAdded[2] != '/' or dateAdded[5] != '/' or dateAdded[3:5] not in months or dateAdded[:2] not in days: #clear all exceptions to ensure date format is correct and date is valid. flaw: some months have less than 31 days; not accounted for
        dateAdded = str(input("Date invalid. Please try again.\nDate on which item is added (dd/mm/yy): "))
    itemLog.append(Item(name, quantity, desc, dateAdded, [])) #add the item to the item log

def itemList():
    print("Log of all items currently in NCC armory")
    print("Name | Quantity | Description | Date Added")
    for x in range(len(itemLog)): #iterate through item log and display relevant info about each item
        print("{} | {} | {} | {}".format(itemLog[x].name, itemLog[x].quantity, itemLog[x].desc, itemLog[x].dateAdded))

def loanItem():
    name = str(input("Name of item to be loaned: "))
    names = [] #create a temporary array to store the names of all the items
    for item in itemLog:
        names.append(item.name) #append all names to the temp array
    while name not in names: #check to ensure that item exists
        name = str(input("Item not found. Please try again.\nName of item to be loaned: ")) #ask user to repeat item name if item does not exist
    loanquantity = int(input("Quantity of item to be loaned: "))
    for item in itemLog:
        while loanquantity > item.quantity: #ensure that quantity being loaned is less than that of the number of total items there are
            loanquantity = int(input("Quantity of item to be loaned greater than quantity of items. Please try again.\nQuantity of item to be loaned: "))
    loandate = str(input("Date on which item is loaned (dd/mm/yy): "))
    while len(loandate) != 8 or loandate[2] != '/' or loandate[5] != '/' or int(loandate[3:5]) < int(item.dateAdded[3:5]) or int(loandate[:2]) < int(item.dateAdded[:2]): #clear all exceptions to ensure date format is correct and date is valid. flaw: if day or month keyed in is not numerical, returns an error and quits function
        loandate = str(input("Date invalid. Please try again.\nDate on which item is loaned (dd/mm/yy): "))
    for item in itemLog:
        if item.name == name:
            item.loan.append([loanquantity, loandate]) #add the quantity of items loaned and the date it is loaned under the loan property of the item

def loanLog():
    name = str(input("Name of item loaned: ")) #ask for item that user wants to check loan log for
    names = [] #create a temporary array to store the names of all the items
    for item in itemLog:
        names.append(item.name) #append all names to the temp array
    while name not in names: #check to ensure that item exists
        name = str(input("Item not found. Please try again.\nName of item loaned: ")) #ask user to repeat item name if item does not exist
    for item in itemLog:
        if item.name == name:
            loaneditem = item #assign the item to a variable for ease of access later
    print("Log of", name,  "loaned from NCC armory")
    print("Name | Quantity | Loan Date")
    for x in range(len(loaneditem.loan)):
        print("{} | {} | {}".format(loaneditem.name, loaneditem.loan[x][0], loaneditem.loan[x][1])) #list all previous loans on the specified item

def removeItem():
    name = str(input("Name of item to be removed: "))
    names = [] #create a temporary array to store the names of all the items
    for item in itemLog: 
        names.append(item.name) #append all names to the temp array
    while name not in names: #check to ensure that item exists
        name = str(input("Item not found. Please try again.\nName of item to be removed: ")) #ask user to repeat item name if item does not exist
    removequantity = int(input("Quantity of item to be removed: "))
    for item in itemLog:
        while removequantity > item.quantity: #ensure that quantity being removed is less or equal to quantity of total items
            removequantity = int(input("Quantity of item to be removed greater than quantity of items. Please try again.\nQuantity of item to be removed: "))
    for item in itemLog:
        if item.name == name:
            item.quantity = item.quantity - removequantity #remove the quantity of items that are specified
        if item.quantity == 0: #if the quantity of an item is 0, meaning there are none of that item left, remove it from the item log
            itemLog.remove(item)
