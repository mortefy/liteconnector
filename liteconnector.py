import traceback, sys
import sqlite3, threading


class LiteConnector:
    def __init__(self, BASE_URI):
        self.conn = sqlite3.connect(BASE_URI, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.lock = threading.Lock()

    def committobase(self, query, args=0):
        """Запись в базу данных"""

        try:
            self.lock.acquire(True)
            if args != 0:
                self.cursor.execute(query, args)
            else:
                self.cursor.execute(query)
            self.conn.commit()


        except Exception:
            print(''.join(traceback.format_exception(*sys.exc_info())))
            print('Commit Error')
            print(query, args)
        finally:
            self.lock.release()

    def fetchfrombase(self, query, args=0):
        """Запрос из базы данных"""

        try:
            self.lock.acquire(True)
            if args != 0:
                self.cursor.execute(query, args)
            else:
                self.cursor.execute(query)

            return self.cursor.fetchall()


        except Exception:
            print(''.join(traceback.format_exception(*sys.exc_info())))
            print('Fetch Error')
            print(query, args)
        finally:
            self.lock.release()
