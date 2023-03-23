class dvdType:
    def __init__(self, title, star1, star2, director, producer, prodco, nodvds):
        self.title = title
        self.star1 = star1
        self.star2 = star2
        self.director = director
        self.producer = producer
        self.prodco = prodco
        self.nodvds = int(nodvds)

    def set_title(self, title):
        self.title = title

    def set_star1(self, star1):
        self.star1 = star1

    def set_star2(self, star2):
        self.star2 = star2

    def set_director(self, director):
        self.director = director

    def set_producer(self, producer):
        self.producer = producer

    def set_prodco(self, prodco):
        self.prodco = prodco

    def set_nodvds(self, nodvds):
        self.nodvds = int(nodvds)

    def get_title(self):
        return self.title

    def get_star1(self):
        return self.star1

    def get_star2(self):
        return self.star2

    def get_director(self):
        return self.director

    def get_producer(self):
        return self.producer

    def get_prodco(self):
        return self.prodco

    def get_nodvds(self):
        return self.nodvds

    def __str__(self):
        return f'title: {self.title}\n' + \
               f'starring: {self.star1}\n' + \
               f'and: {self.star2}\n' + \
               f'director: {self.director}\n' + \
               f'producer: {self.producer}\n' + \
               f'company: {self.prodco}\n' + \
               f'stock: {self.nodvds}\n'

    def checkout(self):
        if int(self.nodvds) > 0:
            self.nodvds = int(self.nodvds) - 1
        else:
            print("currently out of stocks")

    def checkin(self):
        self.nodvds = self.nodvds + 1

    def printDVDtile(self):
        print("DVD Title: ", self.title)

    def checkTitle(self, title):
        return (self.title == title)

    def upDateStock(self, num):
        self.nodvds = self.nodvds + num


    def addTofile(self):
        l = [self.get_title(), self.get_star1(), self.get_star2(), self.get_director(), self.get_producer(),self.get_prodco(),self.get_nodvds()]
        with open('List of DVDS.csv', 'a', newline='') as file:
            for i in l:
                file.write(f"{i}, ")
            file.write('\n')
