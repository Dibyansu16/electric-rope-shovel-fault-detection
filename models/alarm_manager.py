class AlarmManager:
    def __init__(self):
        self.alarms=[]
        self.history=[]
    def raise_alarm(self,message):
        if message not in self.alarms:
            self.alarms.append(message)
            self.history.append(message)
    def clear(self):
        self.alarms.clear()