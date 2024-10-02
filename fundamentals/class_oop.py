class Student:
    name = ''
    subject=''
    class_time=''

    def __init__(self,subject_name,class_time):
        self.subject = subject_name
        self.class_time = class_time
        # print(self.subject)
        # print(self.class_time)

m_obj = Student('python','3 PM')
# on_obj = Student()
# far_obj = Student()
# shah_paran_obj = Student()
# hamza_paran_obj = Student()

m_obj.name = 'mehedi'
# on_obj.name = 'ongkon'
# far_obj.name = 'farhad'
# shah_paran_obj.name = 'shahparan'
# hamza_paran_obj.name = 'hamza'

m_obj.activity()

# obj1.activity()