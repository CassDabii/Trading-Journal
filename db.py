import sqlite3


class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS trades (id INTEGER PRIMARY KEY, date text, time text,"
                         " instrument text, direction text, lots text, entry_price text, exit_price text,"
                         " commissions text, notes text, trading_rating text)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute('SELECT * FROM trades')
        rows = self.cur.fetchall()
        return rows

    def insert(self, date, time, instrument, direction, lots, entry_price,
               exit_price, pnl, notes, outcome):
        self.cur.execute("INSERT INTO trades VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                         (date, time, instrument, direction, lots, entry_price,
                          exit_price, pnl, notes, outcome))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM trades WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, date, time, instrument, direction, lots, entry_price, exit_price,
               pnl, notes, outcome):
        self.cur.execute('UPDATE trades SET date = ?,time = ?,instrument = ?,'
                         'direction = ?,lots = ?,entry_price = ?,exit_price = ?'
                         ',commissions = ?,notes = ?,trading_rating = ? WHERE id = ?',
                         (date, time, instrument, direction, lots, entry_price,
                          exit_price, pnl, notes, outcome, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()


db = Database('tradelog.db')
