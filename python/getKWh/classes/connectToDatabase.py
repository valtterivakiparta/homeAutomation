import mariadb
import sys
import requests
import datetime

date = datetime.datetime.now()
nextDayDate = date + datetime.timedelta(days=1)
nextHour = date + datetime.timedelta(hours=1)

class connect:
        def dbconnect(self, nextDayDate, nextHour):
            try:
                conn = mariadb.connect(
                    user="valtteri",
                    password="MiinuspallO03",
                    host="localhost",
                    port=3306,
                    database="homeAutomation"

                )
            except mariadb.Error as e:
                print(f"Error connecting to MariaDB Platform: {e}")
                sys.exit(1)

            # Get Cursor
            cur = conn.cursor()
            self.insertIntoDatabase(cur, conn, nextDayDate, nextHour)
 
        def insertIntoDatabase(self, cur, conn, nextDayDate, nextHour):
            kwhPrice = self.getPrice(nextDayDate, nextHour)
            data = [kwhPrice, nextHour, nextDayDate]
            #cur.execute("CREATE TABLE pricesKWH ( kwhPrice float NOT NULL, timeOfDay INT NOT NULL, dateTime DATE NOT NULL);")
            #cur.execute("DROP TABLE pricesKWH;")
            cur.execute("INSERT INTO pricesKWH (kwhPrice, timeOfday, dateTime) VALUES (?,?,?);",data)
            conn.commit()


        def getPrice(self, nextDayDate, nextHour):
            url = 'https://api.porssisahko.net/v1/price.json?date={}&hour={}'.format(nextDayDate, nextHour)
            response = requests.get(url)
            rawData = response.json()
            data = rawData["price"]
            return data