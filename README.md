# liteconnector
Simple and easy to use Sqlite3 connector for python3. Also can be used in sync apps.


How to use:
```python
from liteconnector import LiteConnector
db = LiteConnector("sqlite3.db")

# fetch example
result = db.fetchfrombase('select id from stats where date = ?', (time_now,))
# commit example
db.committobase('insert into stats (date, id) values (?,?)', (time_now, id))
```
