# models.py
class User:
    def __init__(self, name):
        self.name = name
        self.availability = []

class MeetingScheduler:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def find_common_slots(self):
        common_slots = {day: [] for day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']}
        
        for user in self.users:
            for day, slots in user.availability[0].items(): 
                if slots:
                    common_slots[day].extend(slots)

        
        for day in common_slots:
            common_slots[day] = list(set(common_slots[day]))  
            common_slots[day].sort()  

        return common_slots
