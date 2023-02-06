#pip install Flask-SQLAlchemy

from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contacts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    modelo = db.Column(db.String(80), nullable=False)
    marca =  db.Column(db.String(20), nullable=False)
    year =  db.Column(db.String(20), nullable=False)
    obs =  db.Column(db.String(20), nullable=False)
    valor =  db.Column(db.String(20), nullable=False)
    status =  db.Column(db.String(20), nullable=False)
    

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def dict(self):
       return {"id":self.id, "modelo":self.modelo,"marca": self.marca,
       "year":self.year, "obs":self.obs, "valor":self.valor, "status":self.status}

with app.app_context():
    db.create_all()


@app.route('/axios.html', methods=['GET'])
def axios():
    return render_template('axious.html')

@app.route('/contacts.html', methods=['GET'])
def datas():
    return render_template('contacts.html')

@app.route('/index.html', methods=['GET'])
def teste():
    return render_template('index.html')


# GET request to retrieve all contacts
@app.route('/contacts', methods=['GET'])
def get_contacts():
    contacts = Contact.query.all()
    return jsonify({'contacts':[contact.as_dict() for contact in contacts]}), 200


@app.route('/modelos/<carros>', methods=['GET'])
def load_modelos(carros):
    print('modelo', carros)
    data = request.get_json()
    print(data)
    # if not data or not all(key in data for key in ('modelo','marca','year','obs','valor','status')):
    #     return jsonify({'message': 'Bad request'}), 400
    # contact = Contact.query.get_or_404(id)
    # contact.modelo = data['modelo']
    # contact.marca = data['marca']
    # contact.year = data['year']
    # contact.obs = data['obs']
    # contact.valor = data['valor']
    # contact.status = data['status']
    # db.session.commit()
    return jsonify({'contact': 'Teste'}), 200



# POST request to add a new contact
@app.route('/contacts', methods=['POST'])
def add_contact():
    data = request.get_json()
    if not data or not all(key in data for key in ('modelo','marca','year','obs','valor','status')):
        return jsonify({'message': 'Bad request'}), 400

    contact = Contact(modelo=data['modelo'],marca=data['marca'],year=data['year'],
    obs=data['obs'],valor=data['valor'],status=data['status'])
    db.session.add(contact)
    db.session.commit()
    return jsonify({'contact': contact.as_dict()}), 201

# PUT request to update a contact
@app.route('/contacts/<int:id>', methods=['PUT'])
def update_contact(id):
    data = request.get_json()
    if not data or not all(key in data for key in ('modelo','marca','year','obs','valor','status')):
        return jsonify({'message': 'Bad request'}), 400
    contact = Contact.query.get_or_404(id)
    contact.modelo = data['modelo']
    contact.marca = data['marca']
    contact.year = data['year']
    contact.obs = data['obs']
    contact.valor = data['valor']
    contact.status = data['status']
    db.session.commit()
    return jsonify({'contact': contact.as_dict()}), 200

# DELETE request to delete a contact
@app.route('/contacts/<int:id>', methods=['DELETE'])
def delete_contact(id):
    contact = Contact.query.get_or_404(id)
    db.session.delete(contact)
    db.session.commit()
    return jsonify({'message': 'Contact has been deleted.'}), 200

if __name__ == '__main__':
    app.run(debug=True,port=5000)


'''
@app.route('/contacts', methods=['GET', 'POST', 'PUT', 'DELETE'])
def contacts():
    if request.method == 'GET':
        contacts = Contact.query.all()
        return jsonify([contact.as_dict() for contact in contacts])

    if request.method == 'POST':
        contact = Contact(name=request.json['name'], phone=request.json['phone'])
        db.session.add(contact)
        db.session.commit()
        return '', 201

    if request.method == 'PUT':
        contact = Contact.query.get(request.form['id'])
        if not contact:
            return '', 404
        contact.name = request.form['name']
        contact.phone = request.form['phone']
        db.session.commit()
        return '', 200

    if request.method == 'DELETE':
        contact = Contact.query.get(request.form['id'])
        if not contact:
            return '', 404
        db.session.delete(contact)
        db.session.commit()
        return '', 200

if __name__ == '__main__':
    app.run(debug=True)
'''