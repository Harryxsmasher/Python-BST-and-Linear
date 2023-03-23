import dvdclass
import customerclass
import linklist
import bst

#main Function
def main():
    root = None

    DVDstock1 = linklist.Slinkedlist()

    try:

        input_file1 = open("List of DVDS.csv")

        for i in input_file1.readlines():
            temp = i.split(',')
            title = temp[0]
            star1 = temp[1]
            star2 = temp[2]
            director = temp[3]
            producer = temp[4]
            company = temp[5]
            copies = temp[6]
            # print(temp[0])
            DVD = dvdclass.dvdType(title, star1, star2, director, producer, company, copies)
            DVDstock1.AtEnd(DVD)

        DVDstock1.listprint()



    finally:
        input_file1.close()

    listDVDs = []
    listDVDs.append('DVD')

    try:

        
        input_file2 = open("List of Customer.csv")

        for n, i in enumerate(input_file2.readlines()):
            temp = i.split(',')
            firstname = temp[0]
            lastname = temp[1]
            accountno = temp[2]
            Customer = customerclass.customerType(firstname, lastname, accountno, listDVDs)
            if n == 0:
                root = bst.NodeBST(Customer)
            else:
                root.insert(Customer)

        root.PrintTree()




    finally:
        input_file1.close()
#Customer menu
    def get_menu_choice1():
        print()
        print('Menu for Customer')
        print('--------------------------')
        print('1. To Check if a DVD exists in the store')
        print('2. To Check out a DVD')
        print('3. To Check in a DVD')
        print('4. To check whether a particular DVD is available for renting')
        print('5. To List all the titles of the DVD')
        print('6. To list all details of the DVD')
        print('7. To Exit')
        print('--------------------------')
        print()
#Customer menu run
    def run_menu_options1():

        option1 = 0
        while option1 != 7:
            option1 = int(input("Enter 1-7 for your use: "))
            if option1 == 1:
                title = input("Enter the title you are searching for ")
                check_dvd_exists(title)

            elif option1 == 2:
                title = input("Enter the title you are searching for ")
                checkout_DVD(title)

            elif option1 == 3:
                title = input("Enter the title you are searching for")
                checkin_DVD(title)

            elif option1 == 4:
                title = input("Enter the title you are searching for ")
                checkforborrow_DVD(title)

            elif option1 == 5:
                list_all_titles()

            elif option1 == 6:
                list_all_DVD_Details()
#Admin menu
    def get_menu_option2():
        print()
        print('Menu for Admin')
        print('________________')
        print('1.Add the Customer')
        print('2. Search the Customer')
        print('3.view all customer')
      
        # print('5.')
        print('4.Add Dvds')
        print('5.Search DVD')
        print('6. View all DVDS')
       
        print('7. remove DVD Details')
        print('8. exit')
        print('_____________________')
        print()
#Admin menu run
    def run_menu_option2():
        option2 = 0
        while option2 != 11:
            option2 = int(input("Enter 1 - 11 for you use:  "))
            if option2 == 1:
                add_Customer()
            elif option2 == 2:
                search_Customer()
            elif option2 == 3:
                view_Customer_Details()
            elif option2 == 4:
                add_DVDs()
            elif option2 == 5:
                search = str(input('Enter title to search: '))
                search_DVDs(search)
            elif option2 == 6:
                details = str(input('Enter title to search: '))
                view_DVD_Details(details)
            elif option2 == 7:
                details = str(input('Enter title to search: '))
                update_DVD_Details(details)
                # update_DVD_Details()
            elif option2 == 10:
                pass
                # remove_DVD()
#Check DVD Function
    def check_dvd_exists(title):
        found = False

        for val in DVDstock1.iterate_item():
            if val.get_title() == title:
                return print("Item Found")

        return print("Sorry DVD Doesnt exist")
#Checkout DVD Function
    def checkout_DVD(title):
        found = False
        for val in DVDstock1.iterate_item():
            if val.get_title() == title:
                print("Item is Available")
                found = True

                if found == True:
                    y = val.get_nodvds()
                    print("Current no of DVDs Available for borrowing", y)
                    if int(y) > 0:
                        val.checkout()
                        x = val.get_nodvds()
                        print("updated no of DVDs: ", x)

                    else:
                        print("Not Enough DVDs for Borrowing, better luck next time")
        if found == False:
            print("This DVD Doesnt exist")
#Checkin DVD Function
    def checkin_DVD(title):
        for val in DVDstock1.iterate_item():
            if val.get_title() == title:
                print("Item is available in the library")
                found = True
                if found == True:
                    n = val.get_nodvds()
                    print("Current no of DVDs in stock: ", n)
                    val.checkin()
                    x = val.get_nodvds()
                    print("Updated no of DVDs after Checkin: ", x)
        if found == False:
            print("This DVD doesnt exist")
#Check fo borrow DVD Function
    def checkforborrow_DVD(title):
        found = False
        for val in DVDstock1.iterate_item():
            if val.get_title() == title:
                print("Item found")
                found = True
                if found == True:
                    n = val.get_nodvds()
                    if n > 0:
                        return print("No. of copies available: ", n)
                    else:
                        return print("Sorry but no copies available")
        return print("This DVd doesnt exist")
#List all DVD function
    def list_all_titles():
        for val in DVDstock1.iterate_item():
            print("Titles: ", val.get_title())

    def list_all_DVD_Details():
        for val in DVDstock1.iterate_item():
            print("Details of all Dvd")
            print(val)

    def add_Customer():
        fname = input("Enter the firstname: ")
        lname = input("Enter the lastname: ")
        acc1 = input("Enter the account_no: ")
        dvdrented = input("Enter rented DVD: ")
        customer_new = customerclass.customerType(fname, lname, acc1, dvdrented)
        root.insert(customer_new)
        customer_new.addTofile()
        root.PrintTree

    def search_Customer():
        search = input("Enter acc no: ")
        root.searchBst(search)
        print()

    def view_Customer_Details():
        listofcustomer = root.inorderTraversal(root)
        for val in listofcustomer:
            print()
            print(val)
            print()

    

    def add_DVDs():
        titlen1 = input("Enter the title")
        starn1 = input("Enter the first actor")
        starn2 = input("Enter the second actor")
        direcn1 = input("Enter the name of the director")
        prodn1 = input("enter the name of the producer")
        compn1 = input("enter the name of the production company")
        ncopn1 = int(input("Enter the number of copies"))
        DVD_new = dvdclass.dvdType(titlen1, starn1, starn2, direcn1, prodn1, compn1, ncopn1)
        DVDstock1.AtEnd(DVD_new)
        DVD_new.addTofile()

        # fname = input("Enter the firstname: ")
        # lname = input("Enter the lastname: ")
        # acc1 = input("Enter the account_no: ")
        # dvdrented = input("Enter rented DVD: ")
        # customer_new = customerclass.customerType(fname, lname, acc1, dvdrented)
        # root.insert(customer_new)
        # customer_new.addTofile()
        # root.PrintTree

    def search_DVDs(title):
        for std in DVDstock1.iterate_item():
            # print(std.get_title())
            if std.get_title().lower() == title.lower():
                # print('True')
                print("DVD found: ", std.get_title())

    def view_DVD_Details(title):
        for std in DVDstock1.iterate_item():
            if std.get_title().lower() == title.lower():
                print(std)

    def update_DVD_Details(title):
        for std in DVDstock1.iterate_item():
            if std.get_title() == title:
                print(std.get_nodvds())
                num = int(input('Enter copies number: '))
                std.upDateStock(num)
                print("updated no of copies", std.get_nodvds())

    def remove_DVD(title):
        for std in DVDstock1:
            if std.get_title() == title:
                DVDstock1.RemoveNode(std)
        DVDstock1.listprint()

    choice = int(input("Enter 1 to choose Customer menu and 2 to choose admin menu"))

    if choice == 1:
        get_menu_choice1()
        run_menu_options1()
    else:
        get_menu_option2()
        run_menu_option2()


if __name__ == '__main__':
    main()
