import time

# timer variables
starttime = time.time()
lasttime = starttime
lapnum = 1
value = ""

print("Press SPACEBAR for each lap. \nType P and SPACEBAR to stop.")

while value.lower() != "q":

    # Input for the SPACEBR key press
    value  = input()

    # The current lap time
    laptime = round((time.time() - lasttime), 2)

    # total time elapsed since the timer strted
    totaltime = round((time.time() - starttime), 2)

    # printing the lap number, lap-time, and total time
    print("Lap No. "+str(lapnum))
    print("Total time. "+str(totaltime))
    print("Lap Time: "+str(laptime))

    print("*"*20)

    #updating the previous total time and lap number
    lasttime = time.time()
    lapnum += 1

print("Exercise Complete")