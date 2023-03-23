import customerclass

def main():
    fname = input("Enter Firstname: ")
    lname = input("Enter Lastname: ")
    acno = input("Enter account no: ")
    dvdlist = input("Enter DVD name: ")

    obj = customerclass.customerType(fname, lname, acno, dvdlist)
    print(obj.get_firstname(), obj.get_lastname(), obj.get_account_no(), obj.get_DVDlist())

if __name__ == '__main__':
        main()