from flask import Flask, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'gamal311996'
app.config['MYSQL_DB'] = 'GP'

mysql = MySQL(app)

def get_period(t):
    cur = mysql.connection.cursor()
    cur.execute("select pid from period where starttime < '"+t+"' and endtime > '"+t+"';")
    r = cur.fetchall()
    p = r[0][0]
    print(p)
    mysql.connection.commit()
    cur.close()
    return p

def get_day_id(d):
    cur = mysql.connection.cursor()
    cur.execute("select did from `day` where `Name` = '"+d+"';")
    r = cur.fetchall()
    did = r[0][0]
    print(did)
    mysql.connection.commit()
    cur.close()
    return did

def get_course_id(day_id,period,class_id):
    cur = mysql.connection.cursor()
    cur.execute("select timetable.course_cid from timetable where day_did="+str(day_id)+" and class_cid="+str(class_id)+" and period_pid="+str(period)+";")
    r = cur.fetchall()
    cid = r[0][0]
    print(cid)
    mysql.connection.commit()
    cur.close()
    return cid


@app.route('/api',methods=['POST'])
def attendance():
    studends_ids = [1,2]
    class_id = 1
    period = get_period('8:45')
    day_id = get_day_id('sat')
    course_id = get_course_id(day_id,period,class_id)
    cur = mysql.connection.cursor()
    for student_id in studends_ids:
        cur.execute("insert into attendance values("+str(student_id)+","+str(course_id)+",str_to_date('24-4-2019','%d-%m-%Y'));")
    mysql.connection.commit()
    cur.close()
    return('done')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
