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
    def teach_sub_select_all():
        connection.cursor.execute("select * from teach_sub")
        output = connection.cursor.fetchall()
        return output

    @staticmethod
    def insert_student_data(name):
        connection.cursor.execute("INSERT INTO student (stud_name) VALUES(%s)",[name])
        connection.conn.commit()
        return True

    @staticmethod
    def insert_teacher_data(name):
        query=f"INSERT INTO teacher(teach_name)VALUES('{name}')"
        connection.cursor.execute(query)
        connection.conn.commit()
        return True

    @staticmethod
    def insert_subject_data(name):
        query = f"INSERT INTO subject(sub_name) VALUES('{name}')"
        connection.cursor.execute(query)
        connection.conn.commit()
        return True

    @staticmethod
    def insert_teach_for_stud_data(stud_id,teach_id):
        connection.cursor.execute("INSERT INTO stud_teach(stud_id,teach_id) VALUES(%s,%s)", (stud_id, teach_id))
        connection.conn.commit()
        return True

    @staticmethod
    def insert_sub_for_teach_data(teach_id,sub_id):
        connection.cursor.execute("INSERT INTO teach_sub(teach_id,sub_id) VALUES(%s,%s)", (teach_id,sub_id))
        connection.conn.commit()
        return True

    @staticmethod
    def get_student_teacher_rel(stud_id):
        # connection.cursor.execute("""SELECT stud_name, teach_name
        #                             FROM student
        #                             INNER JOIN stud_teach ON stud_teach.stud_id = student.stud_id
        #                             INNER JOIN teacher ON teacher.teach_id = stud_teach.teach_id
        #                             WHERE student.stud_id = (%s)""",stud_id)
        connection.cursor.execute("""select teacher.teach_id,teacher.teach_name 
                                            from teacher 
                                            inner join stud_teach on stud_teach.teach_id = teacher.teach_id 
                                            inner join student on stud_teach.stud_id = student.stud_id 
                                            where student.stud_id = (%s)""", stud_id)
        output = connection.cursor.fetchall()
        return output

    @staticmethod
    def get_teacher_student_rel(teach_id):
        connection.cursor.execute("""select student.stud_id,student.stud_name
                                        FROM student
                                        INNER JOIN stud_teach ON stud_teach.stud_id = student.stud_id
                                        INNER JOIN teacher ON stud_teach.teach_id = teacher.teach_id
                                        WHERE teacher.teach_id = (%s)""", teach_id)
        output = connection.cursor.fetchall()
        return output

    @staticmethod
    def get_teacher_subject(teach_id):
        connection.cursor.execute("""select teach_name,sub_name 
                                    from teacher 
                                    inner join teach_sub on teach_sub.teach_id = teacher.teach_id 
                                    inner join subject on subject.sub_id = teach_sub.sub_id 
                                    where teacher.teach_id = (%s)""",teach_id)

        output = connection.cursor.fetchall()
        return output

    @staticmethod
    def get_subject_teacher(sub_id):
        connection.cursor.execute("""select teach_name,sub_name
                                        from teacher
                                        inner join teach_sub on teach_sub.teach_id = teacher.teach_id
                                        inner join subject on subject.sub_id = teach_sub.sub_id
                                        where subject.sub_id = (%s)""", sub_id)

        output = connection.cursor.fetchall()
        return output