#!D:\Program Files\Python311\python
import cgi
import pymysql

print('content-type:text/html')
print()

req=cgi.FieldStorage()
product=req.getvalue("pdnm")
inprs=float(req.getvalue("initpr"))
fnprs=float(req.getvalue("finpr"))
# print(product )
# print(inprs)
# print( fnprs)
try:
    con=pymysql.connect(host="bzcbn4d2uhxhhyxbnv5b-mysql.services.clever-cloud.com",user="ur7bqqkes8frnewz",password="L98WyChUoKE5b76u7COK",database="bzcbn4d2uhxhhyxbnv5b")
    cur=con.cursor()
    cur.execute("update itemsp1 set price=%.2f where  prodnm='%s' and price=%.2f" %(fnprs,product,inprs))
    con.commit()

    print("<html>")
    print("<head>")
    print("<link rel='stylesheet' href='bootstrap.min.css'>")
    print("</head>")
    print("<body>")
    print("<div class='container'>")
    print("<br><br><table class='table table-bordered table-hover '>")
    print("<tr style='background-color:pink'>")
    print("<th>Product ID</th>")
    print("<th>Name</th>")
    print("<th>Category</th>")
    print("<th>Company</th>")
    print("<th>Price</th>")
    print("</tr>")
    cur.execute("select * from itemsp1   where  prodnm='%s' and price=%.2f" %(product,fnprs))
    data=cur.fetchall()
    print("<br><br>")
    for rec in data:
        print("<tr>")
        print("<td>",rec[0])
        print("<td>",rec[1])
        print("<td>",rec[2])
        print("<td>",rec[3])
        print("<td>",rec[4])
        print("</tr>")
    print("<br></tr>")
    print("</table>")
    print("</body>")
    print("</html>")

except:
    print("<h2 style='color:red'>Product Not Found</h2>")
    print("<br><br><a href='ProductReport.py'>Want to see Products ?</a>")

con.close()