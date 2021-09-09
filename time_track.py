class TimeTrack:

    days = {
            "monday": 1,
            "tuesday": 2,
            "wednesday": 3,
            "thursday": 4,
            "friday": 5,
            "saturday": 6,
            "sunday": 7,
        }

    def __init__(self, minutes, hours, amPm, day):
        self.__minutes = minutes
        self.__hours = hours
        self.__am_pm = amPm
        self.__daysPassed = 0
        self.__currentDay = day.lower()

    def increase_minutes(self, minutesToIncrease):
        totalMinutes = int(self.__minutes) + int(minutesToIncrease)
         
        if totalMinutes > 59:
            self.__minutes = totalMinutes % 60
            hoursToIncrease = totalMinutes / 60
            self.increase_hours(hoursToIncrease)
        else:
            self.__minutes = totalMinutes
            
        #if totalMinutes < 10:
            #totalMinutes = f"0{totalMinutes}"

    def increase_hours(self, hoursToIncrease):
        currentHour = int(self.__hours)
         
        while hoursToIncrease >= 1:
            currentHour += 1
            
            #If going from 11 to 12 switch am/pm
            if currentHour == 12:
                self.switch_am_pm()
            #If going from 12 to 13, reset current our to 1 (13:00)
            elif currentHour == 13:
                currentHour = 1
                            
            hoursToIncrease -= 1
        
        self.__hours = currentHour
    
    def next_day(self):
        currentDay = self.days[self.__currentDay]
        
        #If getting next day from Sunday -> reset to Monday
        if currentDay + 1 == 8:
            currentDay = 1
        else:
            currentDay += 1   
            
        self.__currentDay = list(self.days.keys())[list(self.days.values()).index(currentDay)]

    def switch_am_pm(self):
        if self.__am_pm.lower() == "am":
            self.__am_pm = "PM"
        else:
            self.__am_pm = "AM"            
            self.__daysPassed += 1
            
            if self.__currentDay != "":
                self.next_day()

    def get_days_passed(self):
        if self.__daysPassed == 1:
            return "(next day)"
        elif self.__daysPassed > 1:
            return f"({self.__daysPassed} days later)"
        else:
            return ""
        
    def get_formatted_time(self):
        
        if self.__minutes < 10:
            self.__minutes = f"0{self.__minutes}"
            
        daysPassed = self.get_days_passed()    
        
        time = f"{self.__hours}:{self.__minutes} {self.__am_pm}"
            
        if self.__currentDay != "":
            time = time + f", {self.__currentDay.capitalize()}"
            
        if daysPassed != None and daysPassed != "":
            time = time + f" {daysPassed}"
            
        return time            
