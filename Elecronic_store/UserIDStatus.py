#!D:\Program Files\Python311\python
import pymysql
import cgi

print('content-type:text/html')
print()
req=cgi.FieldStorage()
id=req.getvalue("userid")
# print("userID",id)
con=pymysql.connect(host="bzcbn4d2uhxhhyxbnv5b-mysql.services.clever-cloud.com",user="ur7bqqkes8frnewz",password="L98WyChUoKE5b76u7COK",database="bzcbn4d2uhxhhyxbnv5b")
curs=con.cursor()
curs.execute("select * from totaluserp1 where userid='%s'" %(id))
data=curs.fetchone()
if data:
    print("<span style='color:red'>Sorry! UserID %s is NOT available</span>" %id)
else:
    print("<span style='color:green'>Congrats! you can take UserID :- %s</span>" %id)
con.close()