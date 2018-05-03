#from flask import Flask,render_template, url_for,request,redirect
from flask import *
from songmethod import db,song
import sqlite3

conn=sqlite3.connect('./database/songs.db')
c=conn.cursor()
app = Flask(__name__)
app.secret_key='1@zhKzq7uCQ9nHX1Srde3sl95cH7yww87XJzOmW'
# @app.before_first_request
# def setup():
#     funct()
@app.route('/my playlists/static/<path:songggg>/<foreign>',methods=['GET','POST'])#create/delete playlists
def playlist(songggg,foreign):
    pn='@@@'
    dl='@@@'
    newlonglist=[]
    newlonglist1=[]
    newlonglist2=[]
    vbg=[]
    if 'logged_in' not in session:
        return redirect(url_for('login'))
    userid=session['logged_in']
    if request.method=='POST':
        if request.form['playlist_name']:
            pn=request.form['playlist_name']
        if request.form['tobedel']:
            dl=request.form['tobedel']
    conn=sqlite3.connect('./database/users.db')
    c=conn.cursor()
    userid=str(userid)
    allusers=[];uname=0
    c.execute('select following from user where name=?',(session['logged_in'],))
    alluser2=c.fetchone()[0];alluser2=alluser2.split(',')
    for x in alluser2:
        # x=str(x)
        if x !='':
            c.execute('select name from user where id=?',(x,))
            uname=c.fetchone()
            if uname[0] != session['logged_in']:
                allusers.append(uname)
    flag=None;flagi='None'
    if foreign == ',':
        flag='None'
        flagi=None
    for x in allusers:
        if x[0] == foreign:
            if x[0]!=session['logged_in']:
                flag='None'
            userid=foreign
    c.execute('select public from user where name=?',(userid,))
    longstring=c.fetchone()[0]
    c.execute('select private from user where name=?',(userid,))
    longpl=c.fetchone()[0];longpl=longpl.split(',')
    longlist=[]
    smalllist=[]
    longlist=longstring.split('|')
    isok=1
    for strn in longlist:
        smalllist=strn.split(',')
        if pn in smalllist:
            isok=0
    if isok == 1 and pn!='@@@':
        longlist.append(pn);
    for strn in longlist:
        smalllist=strn.split(',')
        if dl in smalllist:
            longlist.remove(strn)
    longstring='|'.join(longlist)
    c.execute('select name from user')
    alluser=c.fetchall();
    c.execute('select following from user where name=?',(session['logged_in'],))
    followingusers=c.fetchall();
    c.execute('update user set public=? where name=?',(longstring,userid,))
    conn2=sqlite3.connect('./database/songs.db');c2=conn2.cursor()
    longlist=longstring.split('|')
    privatesongs=[];sm=0;
    for x in longpl:
        if x != '':
            c2.execute('select name,url,image from song where id=?',(x,))
            sm=c2.fetchall()
            privatesongs.append(sm)
    for x in longlist:
        if x != '':
            smalllist=x.split(',')
            newlonglist1=[];newlonglist=[];newlonglist2=[]
            if '' not in smalllist:
                newlonglist1.append(smalllist[0])
                newlonglist.append(newlonglist1)
            for sm in smalllist:
                if '' != sm and sm != smalllist[0]:
                    c2.execute('select name,url,image from song where id=?',(sm,))
                    sm=c2.fetchall()[0]
                    newlonglist2.append(sm)
            newlonglist.append(newlonglist2)
            vbg.append(newlonglist)
    SS='/static/'+songggg
    c2.execute('select name,image from song where url=?',(SS,))
    douu=c2.fetchall()
    c.execute('select log from user where name=?',(session['logged_in'],))
    log=c.fetchone()[0];log=log.split(',');log.reverse()
    c.execute('select followedBy from user where name=?',(session['logged_in'],))
    followers=c.fetchone()[0];followers=followers.split(',');
    allfol=[]
    for x in followers:
        if x != '':
            c.execute('select name from user where id=?',(x,));nam=c.fetchone()[0]
            allfol.append(nam)
    conn.commit()
    conn.close()
    conn2.commit()
    conn2.close()
    return render_template('hello1.html',pnempty=pn,name=userid,display=vbg,songggg=songggg,douu=douu,ps=privatesongs,flag=flag,alluser=alluser,followingusers=allusers,flagi=flagi,namefix=session['logged_in'],notifications=log,allfol=allfol)
@app.route('/my playlists/follow/<user>/<song>/<pom>')
def fol(user,song,pom):
    conn=sqlite3.connect('./database/users.db')
    c=conn.cursor()
    c.execute('select following from user where name=?',(session['logged_in'],))
    alluser=c.fetchone()[0];alluser1=alluser.split(',')
    c.execute('select id from user where name=?',(user,))
    user1=c.fetchone()[0];user1=str(user1);
    c.execute('select followedBy from user where id=?',(user1,))
    folby=c.fetchone()[0];folby=folby.split(',')
    c.execute('select id from user where name=?',(session['logged_in'],))
    curid=c.fetchone()[0];curid=str(curid)
    if pom == '+':
        if user1 not in alluser1:
            alluser1.append(user1);
            alluser=','.join(alluser1)
            if curid not in folby:
                folby.append(curid)
    else:
        if user1 in alluser1:
            alluser1.remove(user1)
            alluser=','.join(alluser1)
            if curid in folby:
                folby.remove(curid)
    folby=','.join(folby)
    c.execute('update user set followedBy=? where id=?',(folby,user1,))
    c.execute('update user set following=? where name=?',(alluser,session['logged_in'],))
    conn.commit()
    conn.close()
    return redirect (url_for('playlist',songggg=song,foreign=','))
@app.route('/clear')
def clear():
    import sqlite3
    conn=sqlite3.connect('./database/users.db')
    c=conn.cursor()
    c.execute('update user set log="" where name=?',(session['logged_in'],))
    conn.commit()
    conn.close()
    return redirect(url_for('playlist',songggg='mod',foreign=','))
@app.route('/<Song>')
def hello(Song=None):
    if 'logged_in' not in session:
        return redirect(url_for('login'))
    input=session['logged_in']
    conn=sqlite3.connect('./database/songs.db');c=conn.cursor()
    c.execute("select url from song where name=?",(Song,));al=c.fetchone()[0]
    c.execute("select priv from song where name=?",(Song,));bl=c.fetchone()[0]
    c.execute("select id from song where name=?",(Song,));cl=c.fetchone()[0]
    c.execute("select image from song where name=?",(Song,));imgg=c.fetchone()[0]
    ad=None;rem=None
    conn.commit()
    c.execute('select count(*) from song');count=c.fetchone()[0]
    tupl=[];table=[]
    for i in range(1,1+count):
        c.execute('select url,name,image from song where id=?',(i,))
        tupl=c.fetchall();
        table.append(tupl)
    conn.close()
    conn=sqlite3.connect('./database/users.db');c=conn.cursor()
    c.execute('select id from user where name=?',(session['logged_in'],));ID=c.fetchone()[0]
    c.execute('select public from user where name=?',(session['logged_in'],));
    allpl=c.fetchone()[0];
    # print(allpl)
    lis=allpl.split('|')
    pub=[]
    for x in lis:
        if x == None:x='1'
        else:
            lislis=x.split(',')
            pub.append(lislis[0])
    pub.remove('')
    print(pub)
    #if session['logged_in']==input:
    return render_template('hello.html',name=session['logged_in'],nameId=cl,song=al,songindex=bl,songname=Song,table=table,image=imgg,ad=ad,rem=rem,pub=pub)

@app.route('/+or-/<pP>/<pname>/<songname>/<name>')
def addordel(pP,songname,name,pname=None):
    conn=sqlite3.connect('./database/users.db')
    c=conn.cursor()
    conn2=sqlite3.connect('./database/songs.db')
    c2=conn2.cursor()
    c.execute('select * from user')
    full=c.fetchall()
    c.execute('select followedBy from user where name=?',(session['logged_in'],))
    followerlist=c.fetchone()[0];followerlist=followerlist.split(',');toup=0;temp=0;
    if pP == 'public+':
        c.execute('select public from user where name=?',(name,))
        longstring=c.fetchone()[0]
        longlist=longstring.split('|')
        isok=1;
        newlonglist=[]
        for smallstring in longlist:
            smalllist=smallstring.split(',')
            if pname in smalllist and songname not in smalllist:
                smalllist.append(songname)
                for record in full:
                    num=record[0];num=str(num)
                    if num in followerlist:
                        c.execute('select log from user where id=?',num)
                        toup=c.fetchone()[0];toup=toup.split(',')
                        c2.execute('select name from song where id=?',(songname,))
                        r=c2.fetchone()[0]
                        temp=session['logged_in']+" added "+r+" to public playlist: "+pname
                        toup.append(temp);toup=','.join(toup)
                        c.execute('update user set log=? where id=?',(toup,num))
            smallstring=','.join(smalllist)
            newlonglist.append(smallstring)
        newlongstring=('|').join(newlonglist)
        c.execute('update user set public=? where name=?',(newlongstring,name,))
    if pP == 'public-':
        c.execute('select public from user where name=?',(name,))
        longstring=c.fetchone()[0]
        longlist=longstring.split('|')
        isok=1;
        newlonglist=[]
        for smallstring in longlist:
            smalllist=smallstring.split(',')
            if pname in smalllist and songname in smalllist:
                smalllist.remove(songname)
                for record in full:
                    num=record[0];num=str(num)
                    if num in followerlist:
                        c.execute('select log from user where id=?',num)
                        toup=c.fetchone()[0];toup=toup.split(',')
                        c2.execute('select name from song where id=?',(songname,))
                        r=c2.fetchone()[0]
                        temp=session['logged_in']+" removed "+r+" from public playlist: "+pname
                        toup.append(temp);toup=','.join(toup)
                        c.execute('update user set log=? where id=?',(toup,num))
            smallstring=','.join(smalllist)
            newlonglist.append(smallstring)
        newlongstring=('|').join(newlonglist)
        c.execute('update user set public=? where name=?',(newlongstring,name,))
    if pP == 'private-':
        c.execute('select private from user where name=?',(name,))
        string=c.fetchone()[0];listt=string.split(',')
        newlist=[]
        for x in listt:
            if songname == x:
                for record in full:
                    num=record[0];num=str(num)
                    if num in followerlist:
                        c.execute('select log from user where id=?',num)
                        toup=c.fetchone()[0];toup=toup.split(',')
                        c2.execute('select name from song where id=?',(songname,))
                        r=c2.fetchone()[0]
                        temp=session['logged_in']+" removed "+r+" from private playlist"
                        toup.append(temp);toup=','.join(toup)
                        c.execute('update user set log=? where id=?',(toup,num))
            else:
                newlist.append(x)
        string=','.join(newlist)
        c.execute('update user set private=? where name=?',(string,name,))
    if pP =='private+':
        c.execute('select private from user where name=?',(name,))
        string=c.fetchone()[0];listt=string.split(',')
        isok=1;
        for x in listt:
            if x == songname:
                isok=0
        if isok == 1:
            listt.append(songname)
            for record in full:
                num=record[0];num=str(num)
                if num in followerlist:
                    c.execute('select log from user where id=?',num)
                    toup=c.fetchone()[0];toup=toup.split(',')
                    c2.execute('select name from song where id=?',(songname,))
                    r=c2.fetchone()[0]
                    temp=session['logged_in']+" added "+r+" to private playlist "
                    toup.append(temp);toup=','.join(toup)
                    c.execute('update user set log=? where id=?',(toup,num))
        string=','.join(listt)
        c.execute('update user set private=? where name=?',(string,name,))
    conn.commit()
    conn.close()
    conn=sqlite3.connect('./database/songs.db')
    c=conn.cursor()
    c.execute('select name from song where id =?',(songname,))
    songname=c.fetchone()[0]
    return redirect(url_for('hello',Song=songname))
@app.route('/prelogin')
def pre():
    session.pop('logged_in',None)
    return redirect(url_for('login'))
@app.route('/login',methods=['GET','POST'])
def login():
    if 'logged_in' in session:
        return redirect(url_for('hello',input=session['logged_in'],Song='Tu Jaanen Na'))
    import sqlite3
    error = None
    Uempty=0;
    Pempty=0;
    JJ=None
    if request.method=='POST':
        u=request.form['username'];p=request.form['password'];
        print(u)
        conn=sqlite3.connect('./database/users.db')
        c=conn.cursor()
        c.execute('select id from user where username=(?) AND password=(?)',(u,p,))
        JJ=c.fetchone();
        print(JJ)
        if JJ !=None:
            JJ=str(JJ[0])
            c.execute('select name from user where username=? AND password=?',(u,p,))
            name=c.fetchone()[0];
        conn.close()
#        if request.form['username'] == 'correct' and request.form['password'] == 'correct':
        if JJ!=None:
            error = 'log in successful'
            session['logged_in']=name;
            return redirect(url_for('hello',input=name,Song='Tu Jaane Na'))
        else:
            if request.form['username'] == '':
                Uempty='1'
            else:
                Uempty=None
            if request.form['password'] == '':
                Pempty='1'
            else:
                Pempty=None
            error = 'log in failed'
    return render_template('login.html',error=error,uempty=Uempty,pempty=Pempty)
@app.route('/register',methods=['GET','POST'])
def reg():
    import sqlite3
    validp='Y';validu='Y';validn='Y';post=None;already=None
    if request.method=='POST':
        post='ok'
        u=request.form['username'];p=request.form['password'];cp=request.form['confirmPassword'];n=request.form['name'];
        if p!=cp or p=='':
            validp=None
        if u == '':
            validu=None
        if n == '':
            validn=None
        conn=sqlite3.connect('./database/users.db')
        c=conn.cursor()
        c.execute('select * from user');alll=c.fetchall()
        for tupl in alll:
            if tupl[1]==n and tupl[2]==u and tupl[3]==p:
                already='1'
        if already!='1':
            if validp=='Y' and validu=='Y' and validn=='Y':
                c.execute('select count(*) from user');num=c.fetchone()[0];num=num+1;
                c.execute("insert into user values(?,?,?,?,'','','','','')",(num,n,u,p,))
        conn.commit()
        conn.close()
    return render_template('register.html',u=validu,p=validp,n=validn,post=post,already=already)
@app.errorhandler(404)
def page_error(therror):
        return "<h1 style=color:blue>SOME ERROR OCCURRED SOMEWHERE SOMEHOW :( </h1>"
if __name__=='__main__':
    app.run(host='0.0.0.0',port=8080)
