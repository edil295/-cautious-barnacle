from employee.models import *

em1 = Employee.objects.create(name='Edil', birth_date=1999, position='Junior', salary=40000, work_experience=2022)
em2 = Employee.objects.create(name='Uluk', birth_date=1989, position='S_admin', salary=58000, work_experience=2017)
em3 = Employee.objects.create(name='Elzar', birth_date=1994, position='Java-development', salary=30000, work_experience=2021)
em4 = Employee.objects.create(name='Meerim', birth_date=1998, position='Middle', salary=150000, work_experience=2019)

p1 = Passport.objects.create(inn='123445689009123', id_card=123445689009123, employee_pas=em1)
p2 = Passport.objects.create(inn='178437589406033', id_card=878435455465465, employee_pas=em2)
p3 = Passport.objects.create(inn='165465467468654', id_card=325687547823456, employee_pas=em3)
p4 = Passport.objects.create(inn='265765856547548', id_card=789325364657425, employee_pas=em4)

to_delete_employee = Employee.objects.get(id=4)
to_delete_employee.delete()

w1 = WorkProject.objects.create(project_name='Anabioz')
w1.member.set([])
