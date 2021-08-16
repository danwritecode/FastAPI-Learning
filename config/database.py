import sqlite3

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

class DatabaseConnection(object):
    def __init__(self):
        self.con = None
        self.cur = None
    
    def __enter__(self):
        self.con = sqlite3.connect("test_app.db")
        self.con.row_factory = dict_factory
        self.cur = self.con.cursor()
        return self.cur
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.con.commit()
        self.con.close()
