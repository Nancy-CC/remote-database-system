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
if 'colour' not in form:
        print("<h2>error</h2>")
        print("<p>please enter a valid color</p>")
if 'saddress' not in form:
        print("<h2>error</h2>")
        print("<p>please enter a valid address</p>")
else:
        print('<table align = "center" border><tr><th>pname</th></tr>')
        colour = form['colour'].value
        saddress = form['saddress'].value
        sql = "select distinct P.pname from Catalog C, Parts P where P.pid=C.pid and C.pid in (select C.pid from Catalog C, Suppliers S where S.sid=C.sid and S.address="+"'"+saddress+"'"+"and C.pid in (select distinct C.pid from Catalog C, Parts P where C.pid=P.pid and P.color="+"'"+colour+"') group by C.pid having count(*)=(select count(S.sid) from Suppliers S where S.address="+"'"+saddress+"'))"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        for x in myresult:
                print('<tr><td>'+str(x[0])+'</td></tr>')
        print('</table>')
