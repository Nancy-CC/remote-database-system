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
if 'saddress' not in form:
        print("<h2>error</h2>")
        print("<p>please enter a valid address</p>")
else:
        print('<table align = "center" border><tr><th>sid</th><th>sname</th></tr>')
        saddress = form['saddress'].value
        sql = "select S.sid, S.sname from Suppliers S where S.address ="+"'"+saddress+"' and S.sid not in (select distinct sid from Catalog)"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        for x in myresult:
                print('<tr><td>'+str(x[0])+'</td>'+'<td>'+str(x[1])+'</td></tr>')
        print('</table>')
