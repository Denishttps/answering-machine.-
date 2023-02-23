import sqlite3

class DB:
  def __init__(self):
    self.conn = sqlite3.connect("ub.db")
    self.cursor = self.conn.cursor()
    self.cursor.execute("CREATE TABLE IF NOT EXISTS status(id PRIMARY KEY, status, text)")
    self.conn.commit()
    self.cursor.execute("CREATE TABLE IF NOT EXISTS processed(first_id)")
    self.conn.commit()

  def status(self, id, status, text):
    self.cursor.execute("INSERT INTO status VALUES(?,?,?)", (id, status, text))
    self.conn.commit()

  def processed(self, first_id):
    self.cursor.execute("INSERT INTO processed VALUES(?)", (first_id,))
    self.conn.commit() 

  def del_process(self):
    self.cursor.execute("DELETE FROM processed")
    self.conn.commit()

  def update_r(self, status, text, id):
    self.cursor.execute("UPDATE status SET status=? text=? WHERE id=?", (status, text, id))
    self.conn.commit()

  def get_status(self, id):
    return self.cursor.execute("SELECT * FROM status WHERE id=?", (id,)).fetchone()

  def get_proc(self, first_id):
    return self.cursor.execute("SELECT first_id FROM processed WHERE first_id=?", (first_id,)).fetchone()

  def del_status(self, status):
    self.cursor.execute("DELETE FROM status WHERE status=?", (status,))
    self.conn.commit()