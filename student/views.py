from flask import Blueprint,jsonify,request
from student.coordinator import DBQuery
from .exceptions import EmptyData


db_query = DBQuery

##################################################################################
##################################################################################

student= Blueprint("student",__name__)

""" api for new student"""
@student.route("/reg/student", methods=['POST'])
def new_student():
    user_data = request.get_json()
    try:
        if len(user_data['student_name']) == 0:
            raise EmptyData
        output =db_query.student_select_all()

        for user in output:
            if str(user['stud_name']) == str(user_data['student_name']):
                return jsonify({"message": "Student is already present ","data":user_data})
                break
        db_query.insert_student_data(user_data['student_name'])
        return jsonify({"message": "new student is added","data":user_data})
    except EmptyData:
        return jsonify({"message": "Empty data is not allowed","data":user_data})
    except Exception as e:
        return jsonify({"message": e.__str__(),"data": user_data})


""" api for show all students """
@student.route("/student",methods=['GET'])
def get_student():
    output = db_query.student_select_all()
    return jsonify({"message": "All students entries", "data": output})


@student.route("/mongo/reg/student",methods=['POST'])
def mongo_new_student():
    user_data = request.get_json()
    db.student.insert_one(user_data)
    return jsonify({"message": "successful"})


##################################################################################
##################################################################################

teacher= Blueprint("teacher",__name__)

""" api for add new teacher"""
@teacher.route("/reg/teacher", methods=['POST'])
def new_teacher():
    user_data = request.get_json()
    try:
        if len(user_data['teacher_name']) == 0:
            raise EmptyData
        output =db_query.teacher_select_all()
        for user in output:
            if str(user['teach_name']) == str(user_data['teacher_name']):
                return jsonify({"message": "Teacher is already added","data":user_data})
                break
        db_query.insert_teacher_data(user_data['teacher_name'])
        return jsonify({"message": "new teacher is added"},user_data)
    except EmptyData:
        return jsonify({"message": "Empty data is not allowed","data":user_data})
    except Exception as e:
        return jsonify({"message": e.__str__(),"data":user_data})


""" api for show all teachers"""
@teacher.route("/teacher",methods=['GET'])
def get_teacher():
    output = db_query.teacher_select_all()
    return jsonify({"message": "All teachers entries", "data": output})

##################################################################################
##################################################################################

subject= Blueprint("subject",__name__)


""" api for add new subject"""
@subject.route("/reg/subject", methods=['POST'])
def new_subject():
    user_data = request.get_json()
    try:
        if len(user_data['subject_name']) == 0:
            raise EmptyData
        output =db_query.subject_select_all()
        for sub in output:
            if str(sub['sub_name']) == str(user_data['subject_name']):
                return jsonify({"message": "Subject is already added ","data":user_data})
        db_query.insert_subject_data(user_data['subject_name'])
        return jsonify({"message": "New subject is added","data":user_data})
    except EmptyData:
        return jsonify({"message": "Empty data is not allowed","data":user_data})
    except Exception as e:
        return jsonify({"message": e.__str__(),"data":user_data})


""" api for show all subjects"""
@subject.route("/subject",methods=['GET'])
def get_subject():
    output = db_query.subject_select_all()
    return jsonify({"message": "All subjects entries", "data": output})

##################################################################################
##################################################################################

teacher_subject_rel = Blueprint("teacher_subject_rel",__name__)

""" api for assigning subject to teacher"""
@teacher_subject_rel.route("/reg/teacher/subject",methods=['POST'])
def reg_teach_for_sub():
    user_data = request.get_json()
    output = db_query.teach_sub_select_all()
    for teach_sub in output:
        if int(teach_sub['teach_id']) == int(user_data['teacher_id']) and int(teach_sub['sub_id']) == int(user_data['subject_id']):
            return jsonify({"message": "subject is already added for this teacher", "data": user_data})
    db_query.insert_sub_for_teach_data(user_data['teacher_id'],user_data['subject_id'])
    return jsonify({"message":"subject is added for this teacher","data":user_data})


""" api for getting all subject for particular teacher"""
@teacher_subject_rel.route("/rel/teacher/subject",methods=['GET'])
def get_teacher_subject():
    user_data = request.get_json()
    output = db_query.get_teacher_subject(user_data['teacher_id'])
    return jsonify({"message": "teacher subject relationship", "data": output})

""" api for getting all teachers of single subject"""
@teacher_subject_rel.route("/rel/subject/teacher",methods=['GET'])
def get_subject_teacher():
    user_data = request.get_json()
    output = db_query.get_subject_teacher(user_data['subject_id'])
    return jsonify({"message": "teacher subject relationship", "data": output})

##################################################################################
##################################################################################


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


""" api for getting all students for particular teacher"""
@student_teacher_rel.route("/rel/teacher/student",methods=['GET'])
def get_teacher_student():
    user_data = request.get_json()
    output = db_query.get_teacher_student_rel(user_data['teacher_id'])
    return jsonify({"message": "teacher student relationship", "data": output})

""" api for getting all teachers for particular student"""
@student_teacher_rel.route("/rel/student/teacher",methods=['GET'])
def get_student_teacher():
    user_data = request.get_json()
    output = db_query.get_student_teacher_rel(user_data['student_id'])
    return jsonify({"message": "subject teacher relationship", "data": output})



