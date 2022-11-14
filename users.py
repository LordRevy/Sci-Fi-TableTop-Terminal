class User:

    def __init__(self, user):
        self.name = user[0]
        self.id_number = user[1]
        self.clearance_level = user[2]
        self.title = user[3]
        self.is_admin = user[4]


#-----------------------------------------------------CHECKING USER CLEARANCE

    def clearance_check(self, clearance):
        if self.clearance_level >= clearance:
            return True
        return False
