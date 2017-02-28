import estimaters.demensions
from estimaters.demensions import *

class Frenchdrain(BaseData):

    def __init__(self, corregated, y_fit, coupling,
            square_grate, trench_grate, pop_up,
            spout_adapt, customer, email, phone, lead, m, l, w, h):

        """
        customer = ''
        email = ''
        phone = ''
        lead = ''
        m = 0
        l = 0
        w = 0
        h = 0
        """

        super().__init__(customer, email,
                phone, lead, m, l, w ,h)


        self.sbncost = 0
        self.corregated = 0
        self.y_fit = 0
        self.coupling = 0
        self.square_grate = 0
        self.trench_grate = 0
        self.pop_up = 0
        self.spout_adapt = 0


        self.corregated   = corregated
        self.y_fit        = y_fit
        self.coupling     = coupling
        self.square_grate = square_grate
        self.trench_grate = trench_grate
        self.pop_up       = pop_up
        self.spout_adapt  = spout_adapt

    def __str__(self):
        target = open("/home/riley/SBNtools/fd_output.txt", 'w')

        volume = self.volume()
        #amt_gravel = str(self.gravel(volume))
        #gravel_cost = self.cost(amt_gravel, gravel)

        gravel = self.gravel(volume)
        mgravel = BaseData.Markup(self, gravel)
        mgravel = str(round(mgravel))

        barrier = self.barrier()
        mbarrier = BaseData.Markup(self, barrier)
        mbarrier = str(round(mbarrier))

        corregated = self.amt_corregated()
        mcorregated = BaseData.Markup(self, corregated)
        mcorregated = str(round(mcorregated))

        label1 = "=" * 26 +'\n'+  '-' * 8 + " ESTIMATE " + '-' * 8 +'\n'+  '=' * 26
        label2 = "=" * 24 +'\n'+  '-' * 8 + " BUDGET " + '-' * 8 +'\n'+  '=' * 24

        text =  label1\
                +"\ngravel: ${} for {} {} ".format(mgravel, gravel[1], gravel[2])\
                +"\ncorregated: ${} for {} {} ".format(
                        mcorregated, corregated[1], corregated[2])\
                +"\nbarrier: ${} for {} {} ".format(mbarrier, barrier[1], barrier[2])\
                +"\ntractor: "\
                +"\nfittings: "\
                +"\nlabor : "\
                +"\n"*2\
                +label2\
                +"\ngravel: ${} for {} {} ".format(gravel[0], gravel[1], gravel[2])\
                +"\ncorregated: ${} for {} {} ".format(
                        corregated[0], corregated[1], corregated[2])\
                +"\nbarrier: ${} for {} {} ".format(barrier[0], barrier[1], barrier[2])\
                +"\ntractor days: "\
                +"\nfittings: "\
                +"\nlabor hours: "\

        refresh = target.write(text)
        target.close()

        target = open("/home/riley/SBNtools/fd_output.txt", 'r')
        new = target.read()
        target.close()


        return new


    def set_size(self):
        """set all fittings to corregated size
        """
        pass

    def cost(self, amount, item):
        """calculate cost of material

        """
        for info in BaseData.getPrices(self)[item]:
            price = info
            break
        sbncost = amount * price 
        return sbncost 
 

    def gravel(self, volume):
        """calculate gravel cost by tons

        :returns: amount in tons 

        """
        amt =  round(BaseData.volume(self)/18.0) 
        cost = self.cost(amt, 'gravel')
        unit = BaseData.getPrices(self)['gravel'][1]
        return cost, amt, unit

    def amt_corregated(self):
        amt = round(self.l)
        cost = round(self.cost(amt, 'corregated pipe'))
        unit = self.getPrices()['corregated pipe'][1]
        return cost, amt, unit

    def barrier(self):
        """calculate weed barrier

        """
        amt = round((self.w * 2 + self.d * 2)*self.l)
        cost = round(self.cost(amt, 'fabric barrier'))
        unit = self.getPrices()['fabric barrier'][1]
        return cost, amt, unit 

    def  tractor(self):
        """caluculate tractor cost for days rented
        """
        pass

    def fittings(self):
        """Return dictionary of fittings with tup (amt, cost)
        """
        pass

    def labor(self, hr_price, workers):
        """calculate total cost of labor
        """


