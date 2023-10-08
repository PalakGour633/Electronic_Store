#!D:\Program Files\Python311\python
import cgi
import pymysql

print('content-type:text/html')
print()

req=cgi.FieldStorage()
product=req.getvalue("pdnm")
com=req.getvalue("cmp")
pr=float(req.getvalue("prs"))
# print(product)
# print(com)
# print(pr)
try:
    con=pymysql.connect(host="bzcbn4d2uhxhhyxbnv5b-mysql.services.clever-cloud.com",user="ur7bqqkes8frnewz",password="L98WyChUoKE5b76u7COK",database="bzcbn4d2uhxhhyxbnv5b")
    cur=con.cursor()
    cur.execute("delete from itemsp1 where  prodnm='%s' and price=%.2f " %(product,pr))
    con.commit()

    print("<html>")
    print("<head>")
    print("<link rel='stylesheet' href='bootstrap.min.css'>")
    print("</head>")
    print("<body>")
    print("<div class='container'>")
    print("<br>")
    print("<h2 style='color:brown'> Item Deleted Succesfully !</h2>")
    print("<br><br>")
    print("<img src='sad-face.gif'>")

except:
    print("<h2 style='color:red'>Product Not Found</h2>")
    print("<br><br><a href='ProductReport.py'>Want to see Products ?</a>")

con.close()