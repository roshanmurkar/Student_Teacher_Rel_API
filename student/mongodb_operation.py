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
    # print(user_data)
    db.student.insert_one({"stud_name":user_data['student_name'],"teacher":[user_data['teacher_name']]})
    # print(user_data,a)
    # user_data.pop('_id')
    return jsonify({"message":"insert successfully","data":user_data})

@app.route("/reg/teacher",methods=['POST'])
def new_teacher():
    user_data = request.get_json()
    db.teacher.insert_one({"teach_name":user_data['teacher_name'],"subject":[user_data['subject_name']]})
    # user_data.pop('_id')
    return jsonify({"message":"insert successfully","data":user_data})

@app.route("/reg/subject",methods=['POST'])
def new_subject():
    user_data = request.get_json()
    db.subject.insert_one(user_data)
    user_data.pop('_id')
    return jsonify({"message":"insert successfully","data":user_data})


@app.route("/student",methods=['GET'])
def get_students():
    docs = []
    for entry in db.student.find():
        #entry.pop('_id')
        docs.append(entry)
        print(entry['_id'])
        print(entry)
    # print(docs,"docs")
    return jsonify({"message":"all student list","data":docs})

@app.route("/teacher",methods=['GET'])
def get_teachers():
    docs = []
    for entry in db.teacher.find():
        entry.pop('_id')
        docs.append(entry)
    return jsonify({"message":"all teachers list","data":docs})

@app.route("/subject",methods=['GET'])
def get_subjects():
    docs = []
    for entry in db.subject.find():
        entry.pop('_id')
        docs.append(entry)
    return jsonify({"message":"all subject list","data":docs})



@app.route("/rel/student/teacher",methods=['GET'])
def rel_student_teacher():
    user_data = request.get_json()
    name = user_data['student_name']
    # data = db.student.find({"stud_name":name})
    # print(data,"data")
    for data in db.student.find({"stud_name":name}):
        print(data,"with _id")
        data.pop('_id')
        print(data,"without _id")
    return jsonify({"message":"student teacher relationship","data":data})


@app.route("/rel/teacher/subject",methods=['GET'])
def rel_teacher_subject():
    user_data = request.get_json()
    name = user_data['teacher_name']
    for data in db.teacher.find({"teach_name":name}):
        print(data,"with _id")
        data.pop('_id')
        print(data,"without _id")
    return jsonify({"message":"teacher subject relationship","data":data})

@app.route("/rel/subject/teacher",methods=['GET'])
def rel_subject_teacher():
    docs = []
    user_data = request.get_json()
    name = user_data['subject_name']
    for data in db.teacher.find({"subject":name}):
        print(data,"with _id")
        data.pop('_id')
        docs.append(data)
        print(data,"without _id")
    return jsonify({"message":"subject teacher relationship","data":docs})


if __name__ == '__main__':
    app.run(debug=True)



# from mongoengine import connect
# connect(db="classroom", host="localhost", port=27017)