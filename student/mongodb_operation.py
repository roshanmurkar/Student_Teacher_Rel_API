from flask import Flask,jsonify,request

from flask_pymongo import PyMongo
# from flask.json import JSONEncoder

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/classroom"
mongodb_client = PyMongo(app)
db = mongodb_client.db
print("successful")

@app.route("/reg/student",methods=['POST'])
def new_student():
    user_data = request.get_json()
    insert_data = {"stud_name":user_data['student_name'],"teacher":[user_data['teacher_name']]}
    db.student.insert_one(insert_data)
    var = insert_data['_id']
    insert_data.update({"_id": str(var)})
    return jsonify({"message":"insert successfully","data":insert_data})

@app.route("/update/student",methods=['POST'])
def update_student():
    user_data = request.get_json()
    for entry in db.student.find():
        if str(entry['_id']) == user_data['id']:
            db.student.update_one({"_id": entry['_id']}, {"$push": {"teacher": user_data["teacher_name"]}})
            return jsonify({"message": "update successfully", "data": user_data})
    return jsonify({"message":"no student found with this id","data":user_data})

@app.route("/reg/teacher",methods=['POST'])
def new_teacher():
    user_data = request.get_json()
    insert_data = {"teach_name":user_data['teacher_name'],"subject":[user_data['subject_name']]}
    db.teacher.insert_one(insert_data)
    var = insert_data['_id']
    insert_data.update({"_id": str(var)})
    return jsonify({"message":"insert successfully","data":insert_data})

@app.route("/update/teacher",methods=['POST'])
def update_teacher():
    user_data = request.get_json()
    for entry in db.teacher.find():
        if str(entry['_id']) == user_data['id']:
            db.teacher.update_one({"_id": entry['_id']}, {"$push": {"subject": user_data["subject_name"]}})
            return jsonify({"message": "update successfully", "data": user_data})
    return jsonify({"message":"no teacher is found with this id","data":user_data})

@app.route("/reg/subject",methods=['POST'])
def new_subject():
    user_data = request.get_json()
    db.subject.insert_one(user_data)
    var = user_data['_id']
    user_data.update({"_id": str(var)})
    return jsonify({"message":"insert successfully","data":user_data})


@app.route("/student",methods=['GET'])
def get_students():
    docs = []
    for entry in db.student.find():
        var = entry['_id']
        entry.update({"_id": str(var)})
        docs.append(entry)
    return jsonify({"message":"all student list","data":docs})

@app.route("/teacher",methods=['GET'])
def get_teachers():
    docs = []
    for entry in db.teacher.find():
        var = entry['_id']
        entry.update({"_id": str(var)})
        docs.append(entry)
    return jsonify({"message":"all teachers list","data":docs})

@app.route("/subject",methods=['GET'])
def get_subjects():
    docs = []
    for entry in db.subject.find():
        var = entry['_id']
        entry.update({"_id": str(var)})
        docs.append(entry)
    return jsonify({"message":"all subject list","data":docs})



@app.route("/rel/student/teacher",methods=['GET'])
def rel_student_teacher():
    user_data = request.get_json()
    name = user_data['student_name']
    for data in db.student.find({"stud_name":name}):
        var = data['_id']
        data.update({"_id": str(var)})
    return jsonify({"message":"student teacher relationship","data":data})


@app.route("/rel/teacher/subject",methods=['GET'])
def rel_teacher_subject():
    user_data = request.get_json()
    name = user_data['teacher_name']
    for data in db.teacher.find({"teach_name":name}):
        var = data['_id']
        data.update({"_id": str(var)})
    return jsonify({"message":"teacher subject relationship","data":data})

@app.route("/rel/subject/teacher",methods=['GET'])
def rel_subject_teacher():
    docs = []
    user_data = request.get_json()
    name = user_data['subject_name']
    for data in db.teacher.find({"subject":name}):
        var = data['_id']
        data.update({"_id": str(var)})
        docs.append(data)
    return jsonify({"message":"subject teacher relationship","data":docs})


if __name__ == '__main__':
    app.run(debug=True)



# from mongoengine import connect
# connect(db="classroom", host="localhost", port=27017)