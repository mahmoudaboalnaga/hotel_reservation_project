class Tester(object):
    """docstring for Tester."""

    hotels=[[20,"Rotana","Abu Dhabi",200,40],[21,"Sheraton","Abu Dhabi",300,100],[22,"Winter balace","Luxor",100,50]]
    reservation=[["Rotana","Ahmed mohamed","+201060333567"],["Rotana","youssef mohamed","+1000000"],["Winter balace","mohamed moustafa","+1000000"]]
    account_sid="" #enter your twilio SID
    auth_token  = "" #enter your twilio auth_token
    twilio_mobile=""#enter your twilio mobile_number

    def __init__(self, arg):
        super(Tester, self).__init__()
        self.arg = arg
