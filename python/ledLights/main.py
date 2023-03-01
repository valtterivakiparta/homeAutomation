from gpiozero import LED
from time import sleep
from classes.connectTodatabase import connect
import datetime

getData = connect()

kwhLed = LED(17)
tempLed = LED(27)


print("leds are on or off....")
while True:
    date = datetime.datetime.now().date()
    rightTime = datetime.datetime.now().time().replace(microsecond=0).hour
    KWHcommand = "SELECT * FROM pricesKWH WHERE dateTime = '{}' AND timeOfday = '{}';".format(date, rightTime)
    kwhdata = getData.dbconnect(KWHcommand)

    tempCommand = "SELECT mittausarvo FROM tempSensor ORDER BY aikaleima DESC limit 1;"
    tempData = getData.dbconnect(tempCommand)

    if __name__ == "__main__":
        for x in kwhdata:
            prices = x[0]
            if prices < 20:
                kwhLed.on()
            else:
                kwhLed.off()
        for y in tempData:
            temp = y[0]
            if temp < 21.5:
                tempLed.on()
            else:
                tempLed.off()