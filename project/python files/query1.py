#!D:\Python\Python37\python
import cgi
import mysql.connector
print ("Content-Type: text/html\n\n")

mydb = mysql.connector.connect(
       host ="localhost",
       user = "root",
       passwd ="63936388",
       database ="SupplyDB")

mycursor = mydb.cursor()
form = cgi.FieldStorage()
if 'partname' not in form :
        print("<h2>error</h2>")
        print("<p>please enter a valid part name</p>")
else:
        print('<table align = "center" border><tr><th>sid</th><th>sname</th><th>address</th><th>cost</th></tr>')
        ppname = form['partname'].value
        sql = "select S.*, C.cost from Suppliers S,Catalog C where S.sid = C.sid and C.pid in(select distinct C.pid from Parts P, Catalog C where P.pid = C.pid and P.pname="+"'"+ppname+"'"+")"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        for x in myresult:
                print('<tr><td>'+str(x[0])+'</td>'+'<td>'+str(x[1])+'</td>'+'<td>'+str(x[2])+'</td>'+'<td>'+str(x[3])+'</td></tr>')
        print('</table>')
