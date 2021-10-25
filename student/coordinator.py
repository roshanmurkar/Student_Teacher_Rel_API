from student.utility import DBConnection

connection = DBConnection

class DBQuery:
    @staticmethod
    def student_select_all():
        connection.cursor.execute("select * from student")
        output = connection.cursor.fetchall()
        return output

    @staticmethod
    def teacher_select_all():
        connection.cursor.execute("select * from teacher")
        output = connection.cursor.fetchall()
        return output

    @staticmethod
    def subject_select_all():
        connection.cursor.execute("select * from subject")
        output = connection.cursor.fetchall()
        return output

    @staticmethod
    def stud_teach_select_all():
        connection.cursor.execute("select * from stud_teach")
        output = connection.cursor.fetchall()
        return output

    @staticmethod
    def insert_student_data(id, name):
        connection.cursor.execute("INSERT INTO student VALUES(%s,%s)", (id,name))
        connection.conn.commit()
        return True

    @staticmethod
    def insert_teacher_data(id, name):
        connection.cursor.execute("INSERT INTO teacher VALUES(%s,%s)", (id, name))
        connection.conn.commit()
        return True

    @staticmethod
    def insert_subject_data(name,id):
        connection.cursor.execute("INSERT INTO subject(sub_name,t_id) VALUES(%s,%s)", (name,id))
        connection.conn.commit()
        return True

    @staticmethod
    def insert_teach_for_stud_data(stud_id,teach_id):
        connection.cursor.execute("INSERT INTO stud_teach(stud_id,teach_id) VALUES(%s,%s)", (stud_id, teach_id))
        connection.conn.commit()
        return True


    @staticmethod
    def get_student_teacher_rel(stud_id):
        connection.cursor.execute("""select student.stud_name,teacher.teache_name
                                  from student
                                  join stud_teach on stud_teach.stud_id = student.stud_id
                                  join teacher on teacher.teach_id=stud_teach.teach_id
                                  where student.stud_id = (%s)""",stud_id)
        output = connection.cursor.fetchall()
        return output

    @staticmethod
    def get_teacher_student_rel(teach_id):
        connection.cursor.execute("""select teacher.teache_name,student.stud_name
                                        from teacher
                                        join stud_teach on stud_teach.teach_id = teacher.teach_id
                                        join student on stud_teach.stud_id = student.stud_id
                                        where teacher.teach_id = (%s);""", teach_id)
        output = connection.cursor.fetchall()
        return output

    @staticmethod
    def get_student_teacher_subject_rel(stud_id):
        connection.cursor.execute("""select student.stud_name,teacher.teache_name,subject.sub_name
                                      from student
                                      join stud_teach on stud_teach.stud_id = student.stud_id
                                      join subject on subject.sub_id=stud_teach.teach_id
                                      join teacher on teacher.teach_id=subject.t_id
                                      where student.stud_id = (%s)""",stud_id)
        output = connection.cursor.fetchall()
        return output

    @staticmethod
    def get_teacher_subject(t_id):
        connection.cursor.execute("""select teacher.teache_name,subject.sub_name
                                    from teacher
                                    join subject on subject.t_id = teacher.teach_id
                                    where teacher.teach_id =(%s);""",t_id)
        output = connection.cursor.fetchall()
        return output