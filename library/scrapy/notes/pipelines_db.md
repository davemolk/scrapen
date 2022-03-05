# pipelines
import sqlite3

create an init and connect to db 
def __init__(self):
    self.con = sqlite3.connect('mtiles.db') 
    # cursor is what we use to execute commands into db
    self.cur = self.con.cursor()

