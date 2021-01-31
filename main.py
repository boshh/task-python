
from flask import Flask, jsonify, request, render_template
import mysql.connector
from mysql.connector import Error
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


class create_dict(dict):
    # __init__ function
    def __init__(self):
        self = dict()

    # Function to add key:value
    def add(self, key, value):
        print(self, key, value)
        self[key] = value


@app.route('/')
def home():
    return render_template('index.html')


# post /store data: {name :}
@app.route('/tasks', methods=['POST'])
def post_Tasks():
    request_data = request.get_json()

    connection = mysql.connector.connect(
        host='localhost',
        database='todolist',
        user='root',
        password='1111')

    try:
        if connection.is_connected():
            # 新增資料
            sql = "INSERT INTO list (description) \
                 VALUES (%s);"
            new_data = (request_data['description'],)

            cursor = connection.cursor()
            cursor.execute(sql, new_data)

            connection.commit()

            cursor.execute("SELECT * from list;")
            record = cursor.fetchall()

            mydict = create_dict()
            array = []
            for row in record:
                array.append({
                    "id": row[0],
                    "isFinish": row[1],
                    "description": row[2],
                    "startDate": row[3],
                    "endDate": row[4]
                    })

            mydict.add('result', (array))

            return jsonify(mydict)
    except Error as e:
        print("資料庫連接失敗：", e)
        return e
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("資料庫連線已關閉")

    # End


# post /store data: {name :}
@app.route('/tasks', methods=['PUT'])
def put_Tasks():
    request_data = request.get_json()
    connection = mysql.connector.connect(
        host='localhost',
        database='todolist',
        user='root',
        password='1111')

    try:
        if connection.is_connected():
            # 新增資料
            sql = "UPDATE list SET description = %s,isFinish=%s WHERE id = %s;"
            new_data = (request_data['description'],
                        request_data['isFinish'],
                        request_data['id'],)

            cursor = connection.cursor()
            cursor.execute(sql, new_data)

            connection.commit()

            cursor.execute("SELECT * from list;")
            record = cursor.fetchall()

            mydict = create_dict()
            array = []
            for row in record:
                array.append({
                    "id": row[0],
                    "isFinish": row[1],
                    "description": row[2],
                    "startDate": row[3],
                    "endDate": row[4]
                    })

            mydict.add('result', (array))

            return jsonify(mydict)
    except Error as e:
        print("資料庫連接失敗：", e)
        return e
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("資料庫連線已關閉")

    # End


# post /store data: {name :}
@app.route('/tasks', methods=['DELETE'])
def delete_Tasks():
    request_data = request.get_json()
    print(request_data)

    connection = mysql.connector.connect(
        host='localhost',
        database='todolist',
        user='root',
        password='1111')

    try:
        if connection.is_connected():
            # 新增資料
            sql = "DELETE FROM list WHERE id = %s;"
            new_data = (request_data['id'],)

            cursor = connection.cursor()
            cursor.execute(sql, new_data)

            connection.commit()

            cursor.execute("SELECT * from list;")
            record = cursor.fetchall()

            mydict = create_dict()
            array = []
            for row in record:
                array.append({
                    "id": row[0],
                    "isFinish": row[1],
                    "description": row[2],
                    "startDate": row[3],
                    "endDate": row[4]
                    })

            mydict.add('result', (array))

            return mydict
    except Error as e:
        print("資料庫連接失敗：", e)
        return e
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("資料庫連線已關閉")
    # End


# get /store
@app.route('/tasks')
def get_Tasks():

    connection = mysql.connector.connect(
            host='localhost',
            database='todolist',
            user='root',
            password='1111')

    try:

        if connection.is_connected():

            # dbversion
            db_Info = connection.get_server_info()
            print("dbversion:", db_Info)

            # db
            cursor = connection.cursor()
            cursor.execute("SELECT * from list;")
            record = cursor.fetchall()
            print("db:", record)

            mydict = create_dict()
            array = []
            for row in record:
                array.append({
                    "id": row[0],
                    "isFinish": row[1],
                    "description": row[2],
                    "startDate": row[3],
                    "endDate": row[4]
                    })

            mydict.add('result', (array))

            return mydict
    except Error as e:
        print("資料庫連接失敗：", e)
        return e
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("資料庫連線已關閉")
    # End


app.run(port=5000)
