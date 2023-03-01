import mariadb
import sys

class connect:
        def dbconnect(self,command):
            try:
                conn = mariadb.connect(
                    user="",
                    password="",
                    host="",
                    port=3306,
                    database=""

                )
            except mariadb.Error as e:
                print(f"Error connecting to MariaDB Platform: {e}")
                sys.exit(1)

            # Get Cursor
            cur = conn.cursor()
            cur.execute(command)
            result = cur.fetchall()
            return result