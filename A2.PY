class computer:
    def __init__(self):
        self.__maxprice=90000

    def sell(self):
        print("Selling Price:{}".format(self.__maxprice))

    def setmaxprice(self,price):
        self.__maxprice=price

c=computer()
c.sell()
c.__maxprice=50000
c.sell()
c.setmasprice(100000)
c.sell()