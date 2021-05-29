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
if 'pid' not in form:
        print("<h2>error</h2>")
        print("<p>please enter a valid part name</p>")
else:
        print('<table align = "center" border><tr><th>sname</th><th>address</th></tr>')
        ppid = form['pid'].value
        sql = "select distinct S.sname, S.address from Catalog C, Suppliers S where S.sid = C.sid and C.sid in (select C.sid from Catalog C where C.cost in (select max(C.cost) from Catalog C where C.pid ="+"'"+ppid+"'"+") and C.pid ="+"'"+ppid+"'"+")"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        for x in myresult:
                print('<tr><td>'+str(x[0])+'</td>'+'<td>'+str(x[1])+'</td></tr>')
        print('</table>')
