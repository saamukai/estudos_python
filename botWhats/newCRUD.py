import sqlite3

    
class CRUD:
    def __init__(self):
        self.CreateDB()

    def Search(exec,where=[],fet=1)->tuple:
        try:
            with sqlite3.connect('db/FreelaDB.db') as db:
                cur = db.cursor()
                if where!=[]: cur.execute(exec,where) 
                else: cur.execute(exec) 
                
                r = cur.fetchall() if fet else cur.fetchone()
                return r 
        except Exception:
            return None

    def Insert(exec:str,insert:tuple)->None:
        
        try:
            with sqlite3.connect('db/FreelaDB.db') as db:
                cur = db.cursor()
                cur.execute(exec,insert)
                db.commit()

        except Exception:
            return None
            
    def Delete(exec,where=False)->None:
        try:
            with sqlite3.connect('db/FreelaDB.db') as db:
                cur = db.cursor()
                if where != False: cur.execute(exec,where) 
                else: cur.execute(exec) 
                db.commit()

        except Exception:
            return None

    def CreateDB(self)->None:
        try:
            with sqlite3.connect("db/FreelaDB.db") as db:
                query = """CREATE TABLE IF NOT EXISTS freelancers(
                    Number text PRIMARY KEY,
                    Name text DEFAULT ''
                    );"""
                db.execute(query)
                db.commit()

        except Exception:
            pass
