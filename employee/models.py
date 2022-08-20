from django.db import models


class AbstractPerson(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.IntegerField()

    def get_age(self):
        res = 2022 - self.birth_date
        print(res)

    class Meta:
        abstract = True


class Employee(AbstractPerson):
    position = models.CharField(max_length=100)
    salary = models.IntegerField()
    work_experience = models.IntegerField()

    def save(self, *args, **kwargs):
        print(f'position={self.position} salary={self.salary} work_experience={self.work_experience}')
        super().save(*args, **kwargs)


class Passport(models.Model):
    inn = models.CharField(max_length=100)
    id_card = models.CharField(max_length=100)
    employee_pas = models.OneToOneField(Employee, on_delete=models.CASCADE)

    def get_inn(self):
        if self.inn[0] == '2':
            result = 'Male'
        else:
            result = 'Female'
        return result

    def save(self, *args, **kwargs):
        print(f'inn={self.inn} id_card={self.id_card}')
        super().save(*args, **kwargs)


class WorkProject(models.Model):
    project_name = models.CharField(max_length=100)
    member = models.ManyToManyField(Employee, through='Membership')

    def save(self, *args, **kwargs):
        print(f'project_name={self.project_name}')
        super().save(*args, **kwargs)


class Membership(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    work_project = models.ForeignKey(WorkProject, on_delete=models.CASCADE)
    date_joined = models.DateField()

    def save(self, *args, **kwargs):
        print(f'date_joined={self.date_joined}')
        super().save(*args, **kwargs)


class Client(AbstractPerson):
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        print(f'address={self.address} phone_number={self.phone_number}')
        super().save(*args, **kwargs)


class VIPClient(Client):
    vip_status = models.DateField()
    donation_amount = models.IntegerField()

    def save(self, *args, **kwargs):
        print(f'vip_status={self.vip_status} donation_amount={self.donation_amount}')
        super().save(*args, **kwargs)
