from songmethod import db,song
import sqlite3
conn=sqlite3.connect('./database/songs.db')
c=conn.cursor()
c.execute("""delete from song""")
c.execute("""drop table song""")
conn.commit()
conn.close()
db.create_all()
s=song(url="/static/BachnaAeHaseenoKhudaJaane.mp3",name="Bachna Ae Haseeno Khuda Jaane",image="/static/BachnaAeHaseenoKhudaJaane.jpg",priv="1",pub="2,3");db.session.add(s)
s=song(url="/static/Jannat2_06_SangHoonTere.mp3",name="Jannat2 06 Sang Hoon Tere",image="/static/Jannat2_06_SangHoonTere.jpg",priv="2",pub="3");db.session.add(s)
s=song(url="/static/unravelTG.mp3",name="Unravel Tokyo Ghoul",image="/static/kaneki.jpg",priv="1,2,3",pub="1,2,3");db.session.add(s)
s=song(url="/static/EkLadkiBhegiBhagiSi.mp3",name="Ek Ladki Bhegi Bhagi Si",image="/static/EkLadkiBhegiBhagiSi.jpg",priv="3",pub="1,3");db.session.add(s)
s=song(url="/static/TanuWedsManu_01_SadiGali.mp3",name="Tanu Weds Manu 01 Sadi Gali",image="/static/TanuWedsManu_01_SadiGali.jpg",priv="1,3",pub="1,2");db.session.add(s)
s=song(url="/static/AjabPremKiGhajabKahani01MainTeraDhadkanTeri.mp3",  name="Main Tera Dhadkaan Teri",    image="/static/AjabKahani.jpeg",   priv="",   pub="");db.session.add(s);
s=song(url="/static/AjabPremKiGhazabKahani02TuJaaneNa.mp3",  name="Tu Jaane Na",    image="/static/AjabKahani.jpeg",   priv="",   pub="");db.session.add(s);
s=song(url="/static/BandBaajaBaaraat01AinvayiAinvayi.mp3",  name="Ainvayi Ainvayi",    image="/static/BandBaaja.jpeg",   priv="",   pub="");db.session.add(s);
s=song(url="/static/BandBaajaBaaraat03AadhaIshq.mp3",  name="Aadha Ishq",    image="/static/BandBaaja.jpeg",   priv="",   pub="");db.session.add(s);
s=song(url="/static/GurennoYumiya-ShingekinoKyojinOP.mp3",  name="Guren no Yumiya",    image="/static/snk.jpg",   priv="",   pub="");db.session.add(s);
db.session.commit()
