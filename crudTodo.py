from flask import Flask, jsonify, request, render_template,redirect, url_for
from flask_sqlalchemy import SQLAlchemy
# create the extension
db = SQLAlchemy()
app = Flask(__name__)

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
# initialize the app with the extension
db.init_app(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    phone = db.Column(db.String)

with app.app_context():
    db.create_all()


contacts = [{'id': 1, 'name': 'John Doe',  'phone': '555-555-5555'}]

@app.route('/contact.html')
def contact():
    users = User.query.all() #db.session.execute(db.select(User).order_by(User.username)).scalars()
    for user in user:
        print(user.name)
    return render_template('contact.html', users=users)

# GET request to retrieve all contacts
@app.route('/contacts', methods=['GET'])
def get_contacts():
    if not contacts:
        return jsonify({'message':'No contacts founded in server'}), 404
    return jsonify({'contacts': contacts}), 200

# GET request to retrieve one contacts
@app.route('/contacts/<int:id>', methods=['get'])
def get_contact(id):
    for contact in contacts:
        if id == contact['id']:
            return jsonify({'contact': contact}),200
    return jsonify({'message':'contact not found'}), 404

# POST request to add a new contact with data of the new contact on a json file
@app.route('/contacts', methods=['POST'])
def add_contact():
    # if not request.is_json:
    #     return jsonify({'message':'body is not a json'}), 415
    # data = request.get_json()
    # if not data or not all(key in data for key in ('name','phone')):
    #     return jsonify({'message':'bad request'}), 400
    # id = 1
    # if len(contacts) > 0:
    #     id = contacts[-1]['id']+1
    # c = {'id':id,'name':data['name'],'phone':data['phone']}
    # contacts.append(c) 

    if request.method == "POST":
        user = User(
            username=request.form["username"],
            phone=request.form["phone"],
        )
        db.session.add(user)
        db.session.commit()

        return redirect(url_for("user_detail", id=user.id))

    return render_template("user/create.html")
    # return jsonify({'contact': c}), 201

# PUT request to update a contact
@app.route('/contacts/<int:id>', methods=['PUT'])
def update_contact(id):
    if not request.is_json:
        return jsonify({'message':'body is not a json'}), 415
    data = request.get_json()
    if not data or not all(key in data for key in ('name','phone')):
        return jsonify({'message':'bad request'}), 400
    for i,contact in enumerate(contacts):
        if contact['id'] == id:
            contacts[i] = {'id':id, 'name':data['name'],'phone':data['phone']}    
            return jsonify({'contact': contacts[i]}),200
    return jsonify({'message':'contact not found'}), 404

# DELETE request to delete a contact
@app.route('/contacts/<int:id>', methods=['DELETE'])
def delete_contact(id):
    for i,contact in enumerate(contacts):
        if contact['id'] == id:
            del contacts[i]   
            return jsonify({'message': 'contact deleted'}),200
    user = db.get_or_404(User, id)
    if request.method == "POST":
        db.session.delete(user)
        db.session.commit()
    return jsonify({'message':'contact not found'}), 404
    




app.run(debug=True)