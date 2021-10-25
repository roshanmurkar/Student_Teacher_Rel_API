from flask import Blueprint,jsonify,request
from student.coordinator import DBQuery
from .exceptions import EmptyData

db_query = DBQuery

student= Blueprint("student",__name__)

""" api for new student"""
@student.route("/reg/student", methods=['POST'])
def new_student():
    user_data = request.get_json()
    try:
        if len(user_data['stud_name']) == 0:
            raise EmptyData
        output =db_query.student_select_all()

        for user in output:
            if int(user['stud_id']) == int(user_data['stud_id']):
                return jsonify({"message": "Id is already assigned to the student","data":user_data})
                break
        db_query.insert_student_data(user_data['stud_id'], user_data['stud_name'])
        return jsonify({"message": "new student is added","data":user_data})
    except EmptyData:
        return jsonify({"message": "Empty data is not allowed","data":user_data})
    except Exception as e:
        return jsonify({"message": e.__str__(),"data": user_data})


""" api for show all students """
@student.route("/get/student",methods=['GET'])
def get_student():
    output = db_query.student_select_all()
    return jsonify({"message": "All students entries", "data": output})


# Teacher

teacher= Blueprint("teacher",__name__)

""" api for add new teacher"""
@teacher.route("/reg/teacher", methods=['POST'])
def new_teacher():
    user_data = request.get_json()
    try:
        if len(user_data['teache_name']) == 0:
            raise EmptyData
        output =db_query.teacher_select_all()
        for user in output:
            if int(user['teach_id']) == int(user_data['teach_id']):
                return jsonify({"message": "Id is already assigned to the teacher","data":user_data})
                break
        db_query.insert_teacher_data(user_data['teach_id'], user_data['teache_name'])
        return jsonify({"message": "new teacher is added"},user_data)
    except EmptyData:
        return jsonify({"message": "Empty data is not allowed","data":user_data})
    except Exception as e:
        return jsonify({"message": e.__str__(),"data":user_data})


""" api for show all teachers"""
@teacher.route("/get/teacher",methods=['GET'])
def get_teacher():
    output = db_query.teacher_select_all()
    return jsonify({"message": "All teachers entries", "data": output})

# Subject

subject= Blueprint("subject",__name__)


""" api for add new subject"""
@subject.route("/reg/subject", methods=['POST'])
def new_subject():
    user_data = request.get_json()
    try:
        if len(user_data['sub_name']) == 0:
            raise EmptyData
        output =db_query.subject_select_all()
        for sub in output:
            if str(sub['sub_name']) == str(user_data['sub_name']) and int(sub['t_id']) == int(user_data['teach_id']):
                return jsonify({"message": "Subject is already added for this teacher","data":user_data})
        db_query.insert_subject_data(user_data['sub_name'], user_data['teach_id'])
        return jsonify({"message": "subject is added for this teacher","data":user_data})
    except EmptyData:
        return jsonify({"message": "Empty data is not allowed","data":user_data})
    except Exception as e:
        return jsonify({"message": e.__str__(),"data":user_data})


""" api for show all subjects"""
@subject.route("/get/subject",methods=['GET'])
def get_subject():
    output = db_query.subject_select_all()
    return jsonify({"message": "All subjects entries", "data": output})


student_teacher_rel = Blueprint("student_teacher_rel",__name__)


""" api for assigning teacher to student"""
@student_teacher_rel.route("/reg/student/teacher",methods=['POST'])
def reg_teach_for_stud():
    user_data = request.get_json()
    output = db_query.stud_teach_select_all()
    for stud_teach in output:
        if int(stud_teach['stud_id']) == int(user_data['student_id']) and int(stud_teach['teach_id']) == int(user_data['teacher_id']):
            return jsonify({"message": "teacher is already added for this student", "data": user_data})
    db_query.insert_teach_for_stud_data(user_data['student_id'],user_data['teacher_id'])
    return jsonify({"message":"teacher is added for this student","data":user_data})


""" api for getting particular teachers subject"""
@student_teacher_rel.route("/rel/teacher/subject",methods=['GET'])
def get_teacher_subject():
    user_data = request.get_json()
    output = db_query.get_teacher_subject(user_data['teacher_id'])
    return jsonify({"message": "teacher subject relationship", "data": output})


""" api for getting particular teachers student"""
@student_teacher_rel.route("/rel/teacher/student",methods=['GET'])
def get_teacher_student():
    user_data = request.get_json()
    output = db_query.get_teacher_student_rel(user_data['teacher_id'])
    return jsonify({"message": "teacher subject relationship", "data": output})

""" api for getting student teacher relationship using student particular id"""
@student_teacher_rel.route("/rel/student/teacher", methods=['GET'])
def get_stud_teach_rel():
    user_data = request.get_json()
    output = db_query.get_student_teacher_rel(user_data['student_id'])
    return jsonify({"message": "student teacher relationship", "data": output})


""" getting student teacher subject relationship"""
@student_teacher_rel.route("/rel/teacher/student/subject", methods=['GET'])
def get_stud_teach_sub_rel():
    user_data = request.get_json()
    output = db_query.get_student_teacher_subject_rel(user_data['student_id'])
    return jsonify({"message": "student teacher subject relationship", "data": output})
