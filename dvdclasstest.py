import dvdclass

def main():
    t = input("Enter title: ")
    s1 = input("Enter Star1: ")
    s2 = input("Enter Star2: ")
    d = input("Enter Director name: ")
    p = input("Enter Producer name: ")
    pc = input("Enter Production company name: ")
    nodvd = input("Enter noof dvds: ")

    obj = dvdclass.dvdType(t,s1,s2,d,p,pc,nodvd)
    print(obj.get_title(),obj.get_star1(),obj.get_star2(),obj.get_producer(),obj.get_prodco(),obj.get_nodvds())


if __name__ == '__main__':
        main()