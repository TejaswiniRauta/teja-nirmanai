from flask import Flask, request, jsonify, render_template
from flask_mysqldb import MySQL
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

app.config.from_pyfile('config.py')

mysql = MySQL(app)

@app.route('/test', methods=['GET'])
def test():
    return "✅ Backend is working"

# ✅ Route to upload tool details (JSON-based)
@app.route('/uploadTool', methods=['POST'])
def upload_tool():
    data = request.get_json()
    name = data['name']
    price = data['price']
    contact = data['contact']
    image_url = data['image_url']

    cur = mysql.connection.cursor()
    cur.execute(
        "INSERT INTO tools (name, price, contact, image_url) VALUES (%s, %s, %s, %s)",
        (name, price, contact, image_url)
    )
    mysql.connection.commit()
    cur.close()

    return jsonify({'message': 'Tool uploaded successfully'})

# ✅ Route to get all tools
@app.route('/getTools', methods=['GET'])
def get_tools():
    cur = mysql.connection.cursor()
    result = cur.execute("SELECT * FROM tools")
    if result > 0:
        tools = cur.fetchall()
        tool_list = []
        for tool in tools:
            tool_list.append({
                'id': tool[0],
                'name': tool[1].strip() if tool[1] else "",
                'price': tool[2],
                'contact': tool[3].strip() if tool[3] else "",
                'image_url': tool[4].strip() if tool[4] else "",
                'status': tool[5] if len(tool) > 5 else "available"
            })
        return jsonify({'tools': tool_list})
    else:
        return jsonify({'tools': []})

# ✅ Route to mark tool as bought
@app.route('/buyTool', methods=['POST'])
def buy_tool():
    tool_id = request.form['tool_id']
    cur = mysql.connection.cursor()
    cur.execute("UPDATE tools SET status = 'bought' WHERE id = %s", (tool_id,))
    mysql.connection.commit()
    cur.close()
    return jsonify({'message': 'Tool marked as bought'})

# ✅ Route to handle rental requests (using JSON data)
@app.route('/rentTool', methods=['POST'])
def rent_tool():
    data = request.get_json()
    tool_name = data['tool_name']
    renter_name = data['renter_name']
    renter_contact = data['renter_contact']
    duration_days = data['duration_days']

    cur = mysql.connection.cursor()
    cur.execute(
        "INSERT INTO rent_requests (tool_name, renter_name, renter_contact, duration_days) VALUES (%s, %s, %s, %s)",
        (tool_name, renter_name, renter_contact, duration_days)
    )
    mysql.connection.commit()
    cur.close()

    return jsonify({'message': 'Rent request saved successfully'})

# ✅ Route to serve tools.html from templates
@app.route('/tools', methods=['GET'])
def tools_page():
    return render_template('tools.html')

@app.route('/', methods=['GET'])
def home():
    return "✅ Welcome to Teja NirmanAI Backend"

if __name__ == '__main__':
    app.run(debug=True)
