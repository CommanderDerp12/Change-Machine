class change:
    
    def __init__(self):
        self.twenty = 1
        self.ten = 1
        self.five = 1
        self.toonie = 1
        self.loonie = 1
        self.quarter = 1
        self.dime = 1
        self.nickel = 1
    
    def settings(self):
        if self.twenty == 1:
            print "Twenties will be used"
        else:
            print "Twenties will not be used"
        if self.ten == 1:
            print "Tens will be used"
        else:
            print "Tens will not be used"
        if self.five == 1:
            print "Fives will be used"
        else:
            print "Fives will not be used"
        if self.toonie == 1:
            print "Toonies will be used"
        else:
            print "Toonies will not be used"
        if self.loonie == 1:
            print "Loonies will be used"
        else:
            print "Loonies will not be used"
        if self.quarter == 1:
            print "Quarters will be used"
        else:
            print "Quarter will not be used"
        if self.dime == 1:
            print "Dimes will be used"
        else:
            print "Dimes will not be used"
        if self.nickel == 1:
            print "Nickels will be used"
        
    def changeuse(self, change, coin):
        if change == "use":
            if self.coin == 1:
                print "No change occured, " + coin + " is still in use"
            else:
                print "Change occured," + coin + " is no longer in use"
                self.coin == self.coin*-1
        elif change == "don't use":
            if self.coin == 1:
                print "Change occured," + coin + " is no longer in use"
                self.coin == self.coin*-1
            else:
                print "No change occured, " + coin + " is still in use"
                
