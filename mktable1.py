from usermethod import db,user
import sqlite3
conn=sqlite3.connect('./database/users.db')
c=conn.cursor()
c.execute("""delete from user""")
c.execute("""drop table user""")
conn.commit()
conn.close()
db.create_all()
s=user(name='visvesh',username='visvesh',password='usr_vis',private='',public='');db.session.add(s)
s=user(name='subra',username='visvesh1',password='usr_vis1',private='',public='');db.session.add(s)
s=user(name='manian',username='visvesh2',password='usr_vis2',private='',public='');db.session.add(s)
s=user(name='batman',username='bruce@wayne.bat',password='arthur',private='',public='');db.session.add(s)
db.session.commit()
