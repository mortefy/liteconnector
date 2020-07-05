# liteconnector
Simple and easy to use Sqlite3 connector for python3. Also can be used in sync apps.


How to use:
```python
from liteconnector import LiteConnector
db = LiteConnector("sqlite3.db")

# commit example
db.committobase('CREATE TABLE stats (date DATETIME, id INTEGER)', ())
db.committobase('INSERT INTO stats (date, id) VALUES (?,?)', (time_now, id))
# fetch example
result = db.fetchfrombase('SELECT id FROM stats WHERE date = ?', (time_now,))
)
```
