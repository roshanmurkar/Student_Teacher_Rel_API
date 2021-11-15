from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, InfoModel,InfoModelSchema
from flask import Flask,jsonify,request


from app import app


app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:root@localhost:5432/test_psql"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)




# general Flask Code
@app.route('/register',methods=['POST'])
def register():
    user_data = request.get_json()
    username = user_data['user_name']
    password = user_data['password']
    new_user = InfoModel(username,password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message":"data is inserted","data":output})

@app.route('/details',methods=['GET'])
def details():
    info_model = InfoModel.query.all()
    info_model_schema = InfoModelSchema(many=True)
    output = info_model_schema.dump(info_model)
    return jsonify({'details': output})



@app.route('/')
def home():
    return jsonify({"message":"welcome to home page"})



if __name__ == '__main__':
    app.run(debug=True)