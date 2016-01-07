import time, winsound, ctypes
from os import system

freq1 = 2500 #default 2500
freq2 = 3750 #default 3750
freq3 = 3125 #default 3125
dur = 200 #default 200
dur2 = 400


def userWorkout():
    workout = []
    description = []
    count = 1
    while True:
        if len(workout) == 0:
            system("cls")
            print 'Interval segment #', count
            descript = raw_input('\nEnter a brief description for the first segment\nExample: 6x45sec fast, 60sec recovery\n\n>>')
            times = raw_input('Number of Repeats\n\n>>')
            lengthOn = raw_input('Interval Time HH:MM:SS\n\n>>')
            lengthOff = raw_input('Recovery Time HH:MM:SS\n\n>>')
        else:
            system("cls")
            print 'Interval segment #', count
            descript = raw_input('\nEnter a brief description for the next segment, or <ENTER> to continue:\n\n>>')
            times = raw_input('Number of Repeats (Hit <ENTER> to Start Workout)\n\n>>')
            if len(times) == 0:
                break
            lengthOn = raw_input('Interval Time HH:MM:SS\n\n>>')
            lengthOff = raw_input('Recovery Time HH:MM:SS\n\n>>')
        times = int(times)
        interval = []
        lengthOn = lengthOn.strip().split(":")
        lengthOff = lengthOff.strip().split(":")

        timeOn = 0
        pos = 0
        x = 3600
        for i in lengthOn:
            timeOn += int (i) *x
            pos += 1
            x /= 60

        timeOff = 0
        pos = 0
        x = 3600
        for i in lengthOff:
            timeOff += int(i) * x
            pos += 1
            x /= 60

        interval.append(times)
        interval.append(timeOn)
        interval.append(timeOff)
        description.append(str(descript))
        workout.append(interval)
        count += 1

    return description, workout

def startCount(totalIntervals):
    count = 5
    time.sleep(1)
    for i in range(count):
        system("cls")
        print 'Start interval 1 of', totalIntervals, 'in:', time.strftime('%H:%M:%S', time.gmtime(count))
        if count < 4:
            winsound.Beep(freq1,dur)
            time.sleep(.8)
        else:
            time.sleep(1)
        count -= 1

def intervalCount(repeat, currInterval, totalIntervals):
    count = repeat
    system("cls")
    print 'Interval', currInterval, 'of', totalIntervals, '*****'
    winsound.Beep(freq2,dur2)
    time.sleep(.8)

    for i in range(count):
        system("cls")
        print 'interval', currInterval, 'of', totalIntervals, ':', time.strftime('%H:%M:%S', time.gmtime(count))

        if count < 4:
            winsound.Beep(freq1,dur)
            time.sleep(.8)
        else:
            time.sleep(1)
        count -= 1

def restCount(rest):
    count = rest
    system("cls")
    print 'Rest! *****'
    winsound.Beep(freq2,dur2)
    time.sleep(.8)
    for i in range(count):
        system("cls")
        print 'Rest for', time.strftime('%H:%M:%S', time.gmtime(count))
        if count < 4:
            winsound.Beep(freq1,dur)
            time.sleep(.8)
        else:
            time.sleep(1)
        count -= 1

def intervalLoop(workout, descriptions):
    for segment in range(len(workout)):
        if segment > 0:
            system("cls")
            print 'Up next:', descriptions[segment]
            execute = raw_input('Hit <ENTER> to start next segment')
            startCount(workout[0][0])
        count = 1
        for i in range(workout[segment][0]):
            intervalCount(workout[segment][1], count, workout[segment][0])
            if i == workout[segment][0]-1:
                system("cls")
                print '***** Segment Complete! *****'
                winsound.Beep(freq1,dur)
                winsound.Beep(freq3,dur)
                winsound.Beep(freq2,dur)
                winsound.Beep(freq1,dur)
                winsound.Beep(freq3,dur)
                winsound.Beep(freq2,dur)
                winsound.Beep(freq1,dur)
                winsound.Beep(freq3,dur)
                winsound.Beep(freq2,dur)
            else:
                restCount(workout[segment][2])
            count += 1


if __name__ == '__main__':
    
    
    system("mode con cols=50 lines=10")
    ctypes.windll.kernel32.SetConsoleTitleA("Interval Keeper")


    stuff = userWorkout()
    descriptions = stuff [0]
    workout = stuff [1]

    system("cls")
    system("mode con cols=50 lines=2")
    print 'Up next:', descriptions[0]
    execute = raw_input('Hit <ENTER> to start workout:')

    startCount(workout[0][0])

    intervalLoop(workout, descriptions)

