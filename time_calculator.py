from time_track import TimeTrack 

def add_time(start, duration, day=""):
        
    splitDuration = duration.split(":")
    durationHours = int(splitDuration[0])
    durationMinutes = int(splitDuration[1])

    splitStartTime = start.split(":")
    hours = int(splitStartTime[0])
    
    #Split minutes from AM/PM
    splitTimeFrame = splitStartTime[1].split()
    minutes = int(splitTimeFrame[0])    
    amPm = splitTimeFrame[1]

    timeTrack = TimeTrack(minutes, hours, amPm, day)
    timeTrack.increase_hours(durationHours)
    timeTrack.increase_minutes(durationMinutes)

    return timeTrack.get_formatted_time()

