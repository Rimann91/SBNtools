

class BaseData():
    """Base polymorphic class for Job info
    """
    def __init__(self, markup, l, w, h):

        self.l = 0
        self.w = 0
        self.d = 0
        self.h = 0

        self.l = l
        self.w = w
        self.d = h
        self.h = h
        self.markup = markup

    def perimeter(self):
        return self.l * 2 + self.w * 2

    def area(self):
        return self.l * self.h

    def volume(self):
        return self.l * self.w * self.h

    def Markup(self, items_method):
        """mark p SBN cost for sale

        """
        cost = items_method[0] 
        return cost * self.markup 
 
    def getPrices(self):
        target = open("/home/riley/SBNtools/prices.csv", 'r')
        price_string = target.readlines() 
        price_list = []
        price_dict = {}
        for item in price_string:
            price_list.append(item.split(','))

        for item in price_list:
            if len(item) == 3:
                price_dict[item[0]] = float(item[1]),item[2]

        return(price_dict)


class CustomerInfo():
    """Take info for customer, put in DB"""

    def __inti__(self, customer, email, phone, lead):
        self.m = markup
        self.customer = customer
        self.email = email
        self.phone = phone

