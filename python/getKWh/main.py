import datetime
from classes.connectToDatabase import connect
from classes.classes import sendSMS
import os

date = datetime.datetime.now()
nextDayDate = date + datetime.timedelta(days=1)
getData = connect()
timer = 0
SMS = sendSMS()

print("Connected and waiting nextday prices.")
while True: 
    if __name__ == "__main__":
        rightTime = datetime.datetime.now().time().replace(microsecond=0)
        if rightTime.hour == 17 and rightTime.minute == 00 and rightTime.second == 00:
            os.system("clear")
            print("Connected and waiting nextday prices.")
            timer = 0
            try:
                date = datetime.datetime.now()
                nextDayDate = date + datetime.timedelta(days=1)
                print("Hinta tunnilta", timer)
                while timer < 24:
                    print(timer)
                    getData.dbconnect(nextDayDate.date(), timer)
                    timer = timer + 1
            except: 
                SMS.sendSMS()



#cur.execute("CREATE TABLE pricesKWH ( kwhPrice float NOT NULL, timeOfDay TIME NOT NULL, dateTime DATE NOT NULL);")   CREATED TABLE
#cur.execute("INSERT INTO pricesKWH (kwhPrice, timeOfday, dateTime) VALUES (17,28, 2, 2023-02-17);")