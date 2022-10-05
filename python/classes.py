import time
import glob
import mariadb
import sys

class sensor:
    #Määritetään tiedostopolut josta lämpötilat haetaan
    baseDir = '/sys/bus/w1/devices/'
    deviceFolder = glob.glob(baseDir + '28*')[0]
    deviceFile = deviceFolder + '/w1_slave'

    # Muodostetaan yhteys tietokantaan
    def connectToDatabase(self):
        try:
            conn = mariadb.connect(
                user="valtteri",
                password="MiinuspallO03",
                host="localhost",
                port=3308,
                database=""

            )
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
            sys.exit(1)

        # Get Cursor
        cur = conn.cursor()
        self.insertIntoTable(cur)
            
    #Funktio jonka avulla lisätään informaatio tietokantaan.
    def insertIntoTable(self, cur):
        cur.execute("")

    #luetaan kaikki data jota löytyy tiedostopolkujen päästä. 
    def readRawData(self):
        r = open(self.deviceFile, 'r')
        lines = r.readlines()
        r.close
        return lines
    
    #Haetaan tarkka sijainti lämpötilasta.
    def readTemperature(self):
        lines = self.readRawData()
        while lines[0].strip()[-3:] != 'YES':
            time.sleep(0.2)
            lines = self.readRawData()
        equalsPos = lines[1].find('t=')
        if equalsPos != -1:
            tempString = lines[1][equalsPos+2:]
            tempC = float(tempString) / 1000.0
            return tempC