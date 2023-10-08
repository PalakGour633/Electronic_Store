#!D:\Program Files\Python311\python
import cgi
import pymysql

print('content-type:text/html')
print()

req=cgi.FieldStorage()
id=req.getvalue("uid")
ps=req.getvalue("psw")
nm=req.getvalue("unm")
gn=req.getvalue("gen")
ct=req.getvalue("ct")
mo=req.getvalue("mob")
em=req.getvalue("eml")

# print(id+ps+nm+gn+ct+mo+em)
try:
    con=pymysql.connect(host="bzcbn4d2uhxhhyxbnv5b-mysql.services.clever-cloud.com",user="ur7bqqkes8frnewz",password="L98WyChUoKE5b76u7COK",database="bzcbn4d2uhxhhyxbnv5b")
    curs=con.cursor()
    curs.execute("insert into totaluserp1 values('%s','%s','%s','%s','%s','%s','%s')" %(id,ps,nm,gn,ct,mo,em))
    con.commit()
    con.close()
    print("<h2> User Registered Sucessfully!</h2>")
except:
    print("<h2> Registration failed</h2>")

print("<a href='index.html'> HOME</a>")
