class customerType:

    def __init__(self, firstname, lastname, account_no, DVDlist):
        self.firstname = firstname
        self.lastname = lastname
        self.account_no = account_no
        self.DVDlist = DVDlist

    def set_firstname(self, firstname):
        self.firstname = firstname

    def set_lastname(self, lastname):
        self.lastname = lastname

    def set_account_no(self, account_no):
        self.account_no = account_no

    def set_DVDlist(self, DVDlist):
        self.DVDlist = DVDlist

    def get_firstname(self):
        return self.firstname

    def get_lastname(self):
        return self.lastname

    def get_account_no(self):
        return self.account_no

    def get_DVDlist(self):
        return self.DVDlist

    def __eq__(self, other):
        return self.account_no == other.account_no

    def __lt__(self, other):
        return self.account_no < other.account_no

    def __le__(self, other):
        return self.account_no <= other.account_no

    def __gt__(self, other):
        return self.account_no > other.account_no

    def __ge__(self, other):
        return self.account_no >= other.account_no

    def __str__(self):
        return f"Firstname: {self.firstname}\n " +\
               f"Lastname: {self.lastname}\n " +\
               f"Account No: {self.account_no}\n "
               

    def printDetails(self):
        print('Name of the Customer: ', self.firstname + '' + self.lastname)
        print('Customer Account number: ', self.account_no)
        for item in self.DVDlist:
            print(item)

    def addTofile(self):
        l = [self.get_firstname(),self.get_lastname(),self.get_account_no(),self.get_DVDlist()]
        with open('List of Customer.csv', 'a', newline='') as file:
            for i in l:
                file.write(f"{i}, ")
            file.write('\n')

