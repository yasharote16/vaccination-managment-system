import pymysql as p
def getconnection():
    return p.connect(host="localhost",user="root",password="",database="flask")
def adddata(t):
    con=getconnection()
    cur=con.cursor()
    query="insert into vaccine(name,adhar_no,phone,city,vaccine,center)values(%s,%s,%s,%s,%s,%s)"  
    cur.execute(query,t)
    con.commit()
    con.close()

