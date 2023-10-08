#!D:\Program Files\Python311\python
import pymysql

print('content-type:text/html')
print()

print("<html>")
print("<head>")
print("<link rel='stylesheet' href='bootstrap.min.css'>")
print("</head>")
print("<body>")
print("<div class='container'>")
print("<br><br><h2  style=' color: purple'> Items Report<br></h2>")

print("<br><br><table class='table table-bordered table-hover '>")
print("<tr style='background-color:pink'>")
print("<th>Product ID</th>")
print("<th>Name</th>")
print("<th>Category</th>")
print("<th>Company</th>")
print("<th>Price</th>")
print("</tr>")

con=pymysql.connect(host="bzcbn4d2uhxhhyxbnv5b-mysql.services.clever-cloud.com",user="ur7bqqkes8frnewz",password="L98WyChUoKE5b76u7COK",database="bzcbn4d2uhxhhyxbnv5b")
cur=con.cursor()
cur.execute("select * from itemsp1")
data=cur.fetchall()
for rec in data:
    print("<tr>")
    print("<td>",rec[0])
    print("<td>",rec[1])
    print("<td>",rec[2])
    print("<td>",rec[3])
    print("<td>",rec[4])
    print("</tr>")
print("</body>")
print("</html>")
print("</table>")