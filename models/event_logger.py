class EventLogger:
    def __init__(self):
        self.events=[]

    def log(self,message):
        self.events.append(message)

        if len(self.events)>50:
            self.events.pop(0)