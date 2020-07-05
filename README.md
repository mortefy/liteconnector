# liteconnector
Simple Sqlite3 synch connector for python


How to use:

from liteconnector import LiteConnector
db = LiteConnector("sqlite3.db")

# fetch example
result = db.fetchfrombase('select id from stats where date = ?', (time_now,))
# commit example
db.committobase('insert into stats (date, id) values (?,?)', (time_now, id))
