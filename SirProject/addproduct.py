#!D:\Program Files\Python311\python
import pymysql
import cgi

print('content-type:text/html')
print()
req=cgi.FieldStorage()

pnm=req.getvalue("prodnm")
cat=req.getvalue("category")
com=req.getvalue("company")
pr=float(req.getvalue("price"))
# print(pnm+cat+com+pr)
try:
    con=pymysql.connect(host="bzcbn4d2uhxhhyxbnv5b-mysql.services.clever-cloud.com",user="ur7bqqkes8frnewz",password="L98WyChUoKE5b76u7COK",database="bzcbn4d2uhxhhyxbnv5b")
    curs=con.cursor()
    curs.execute("insert into itemsp1(prodnm,category,company,price) values('%s','%s','%s',%.2f)" %(pnm,cat,com,pr))
    con.commit()
    con.close()
    print("<h2> Congrats! Item Added Sucessfully ! </h2>")
    print("<a href='AdminPanel.html'> Home </a> ")
    print("<h3 style='color:blue'> Want to add more product ?</h3>")
    print("<a href='AddNewProduct.html'>Add New Product</a>")
except:
    print("<style= color:red >Please, Try Again</style>")

