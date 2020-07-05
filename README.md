# liteconnector
Simple and easy to use Sqlite3 connector for python3. Also can be used in sync apps.


How to use:
```python
from liteconnector import LiteConnector
db = LiteConnector("sqlite3.db")

# fetch example
result = db.fetchfrombase('SELECT id FROM stats WHERE date = ?', (time_now,))
# commit example
db.committobase('INSERT INTO stats (date, id) VALUES (?,?)', (time_now, id))
```
