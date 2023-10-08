#!D:\Program Files\Python311\python
import cgi
import pymysql

print('content-type:text/html')
print()
req=cgi.FieldStorage()
com=req.getvalue("company")

print("<link rel='stylesheet' href='bootstrap.min.css'>")
print("<div class='container'>")
print("<br><br>")
print("<h2>Search Result for %s </h2><hr> " %com)
print("<table class='table table-bordered table-hover'>")
print("<tr style='background-color:pink'>")
print("<th>Product Number")
print("<th>Name")
print("<th>Category")
print("<th>Price")
print("</tr>")
print("</div>")

con=pymysql.connect(host="bzcbn4d2uhxhhyxbnv5b-mysql.services.clever-cloud.com",user="ur7bqqkes8frnewz",password="L98WyChUoKE5b76u7COK",database="bzcbn4d2uhxhhyxbnv5b")
cur=con.cursor()
cur.execute("select * from itemsp1 where company='%s'" %com)
data=cur.fetchall()
for rec in data:
    print("<tr>")
    print("<td>",rec[0])
    print("<td>",rec[1])
    print("<td>",rec[2])
    print("<td>",rec[4])
    print("</tr>")

con.close()
print("</table>")