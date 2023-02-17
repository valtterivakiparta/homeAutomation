import datetime
from classes.connectToDatabase import connect

date = datetime.datetime.now()
nextDayDate = date + datetime.timedelta(days=1)
getData = connect()
timer = 0

print("Connected and waiting nextday prices.")
while True: 
    rightTime = datetime.datetime.now().time().replace(microsecond=0)
    if __name__ == "__main__":
        if rightTime.hour == 14 and rightTime.minute == 00 and rightTime.second == 00:
            date = datetime.datetime.now()
            nextDayDate = date + datetime.timedelta(days=1)
            while timer < 24:
                getData.dbconnect(nextDayDate.date(), timer)
                timer = timer + 1




#cur.execute("CREATE TABLE pricesKWH ( kwhPrice float NOT NULL, timeOfDay TIME NOT NULL, dateTime DATE NOT NULL);")   CREATED TABLE
#cur.execute("INSERT INTO pricesKWH (kwhPrice, timeOfday, dateTime) VALUES (17,28, 2, 2023-02-17);")