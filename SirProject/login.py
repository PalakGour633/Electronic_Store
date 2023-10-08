#!D:\Program Files\Python311\python
import cgi
import pymysql

print('content-type:text/html')
print()

req=cgi.FieldStorage()
id=req.getvalue("uid")
ps=req.getvalue("pass")
# print(id+ps)

#hupd
con=pymysql.connect(host="bzcbn4d2uhxhhyxbnv5b-mysql.services.clever-cloud.com",user="ur7bqqkes8frnewz",password="L98WyChUoKE5b76u7COK",database="bzcbn4d2uhxhhyxbnv5b")
curs=con.cursor()
curs.execute("select * from totaluserp1 where userid='%s'and pswd='%s'" %(id,ps))
data=curs.fetchone()
if data:
    print("<html>")
    print("<head>")
    print("<meta http-equiv='refresh' content='0;url=AdminPanel.html'>")
    print("</head>")
    print("</html>")
else:
    print("<html>")
    print("<head>")
    print("<meta http-equiv='refresh' content='0;url=Failure.html'>")
    print("</head>")
    print("</html>")
con.close()