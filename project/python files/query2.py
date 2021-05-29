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
if 'cost'not in form:
        print("<h2>error</h2>")
        print("<p>please enter a valid cost </p>")
else:
        print('<table align = "center" border><tr><th>sname</th></tr>')
        sscost = form['cost'].value
        sql = "select DISTINCT S.sname  from Suppliers S,Catalog C where S.sid = C.sid and C.cost>"+"'"+sscost+"'"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        for x in myresult:
                print('<tr><td>'+x[0]+'</td></tr>')
        print('</table>')
