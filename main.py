from flask import Flask
from student.views import student
from student.views import teacher
from student.views import subject
from student.views import student_teacher_rel
from student.views import teacher_subject_rel

app = Flask(__name__)

app.register_blueprint(student)
app.register_blueprint(teacher)
app.register_blueprint(subject)
app.register_blueprint(student_teacher_rel)
app.register_blueprint(teacher_subject_rel)

if __name__ == '__main__':
    app.run(debug=True)
