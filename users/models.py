from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


def upload_status_image_faculty(instance, filename):
    return "faculty_img/{user}/{filename}".format(user=instance.user, filename=filename)



def upload_status_image_student(instance, filename):
    return "student_img/{user}/{filename}".format(user=instance.user, filename=filename)

class User(AbstractUser):
    is_student = models.BooleanField()
    is_teacher = models.BooleanField()

    def __str__(self):
        return self.username

class Faculty(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    photo       = models.ImageField(upload_to=upload_status_image_faculty, null=True, blank=True)  # Django Storages --> AWS S3
    subject_name=models.CharField(max_length=100)
    def get_absolute_url(self):
        return reverse('detail', kwargs={'slug': self.user.username})
    def __str__(self):
        return self.user.username

class Student(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    photo       = models.ImageField(upload_to=upload_status_image_student, null=True, blank=True)  # Django Storages --> AWS S3
    DOB=models.DateField(blank=True, null=True)
    first_sem_percentage=models.FloatField(default=0)
    second_sem_percentage=models.FloatField(default=0)
    third_sem_percentage=models.FloatField(default=0)
    fourth_sem_percentage=models.FloatField(default=0)
    fifth_sem_percentage=models.FloatField(default=0)
    sixth_sem_percentage=models.FloatField(default=0)
    seventh_sem_percentage=models.FloatField(default=0)
    eighth_sem_percentage=models.FloatField(default=0)
    branch = models.CharField(max_length=100,
        choices=(('Computer Science & Engineering','Computer Science & Engineering'),('Electrical Engineering','Electrical Engineering'),('Mechanical Engineering','Mechanical Engineering'),('Civil Engineering','Civil Engineering'),('Others','Others')),
        default='Computer Science & Engineering',
        )

    year = models.IntegerField(
        choices=((1,'Ist Year'),(2,'IInd Year'),(3,'IIIrd Year'),(4,'IVth Year')),
        default=1,
        )
    def get_absolute_url(self):
        return reverse('detail', kwargs={'slug': self.user.username})

    def __str__(self):
        return self.user.username



class Subject(models.Model):
    subject_name=models.CharField(max_length=100)
    faculty=models.ForeignKey(to=Faculty,on_delete=models.CASCADE, related_name="teaches", null=True, blank=True)
    def __str__(self):
        return self.subject_name

class SelectedSubject(models.Model):
    subject=models.ForeignKey(to=Subject, on_delete=models.CASCADE, related_name="studies", null=True, blank=True)
    student=models.ForeignKey(to=Student, on_delete=models.CASCADE, related_name="selected", null=True, blank=True)

    def percentage(self):
        p,a=self.present(),self.absent()
        s=p+a
        if s!=0:
            return str(round(p*100.0/s,2))+"%"
        else:
            return 'N.A'
    def present(self):
        a=self.attendance.all()
        return a.filter(present=True).count()
    def absent(self):
        a=self.attendance.all()
        return a.filter(present=False).count()
    def eligiblity(self):
        if self.percentage()=='N.A':
            return False
        return float(self.percentage()[:-1])>60
    def timesheet(self):
        return self.attendance.all().order_by('Date')
    def __str__(self):
        return "{0} - {1}".format(self.subject, self.student)

class AttendanceRecord(models.Model):
    selected_subject=models.ForeignKey(to=SelectedSubject,on_delete=models.CASCADE, related_name="attendance", null=True, blank=True)
    Date=models.DateField(null=True)
    present=models.BooleanField(null=True)
    def __str__(self):
        return "{0} - {1}".format(self.selected_subject, self.Date)
