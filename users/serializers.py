from allauth.account.adapter import get_adapter
from rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from .models import User,Student,Faculty,Subject,SelectedSubject,AttendanceRecord, Notice,StudentOfTheYear,FacultyOfTheYear


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','email', 'username', 'password', 'is_student', 'is_teacher')



class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('user','full_name',  'photo', 'DOB', 'first_sem_percentage', 'second_sem_percentage','third_sem_percentage','fourth_sem_percentage','fifth_sem_percentage','sixth_sem_percentage','seventh_sem_percentage','eighth_sem_percentage','branch')


class StudentOfTheYearSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentOfTheYear
        fields = ('faculty','faculty_name',  'student','student_name', 'vote')

class FacultyOfTheYearSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacultyOfTheYear
        fields = ('student', 'student_name', 'faculty', 'faculty_name','vote')


class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = ('user', 'photo', 'subject_name')


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('subject_name', 'faculty')


class SelectedSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = SelectedSubject
        fields = ('subject', 'student')


class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = ('title','faculty','noticedetails')


class AttendanceRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendanceRecord
        fields = ('selected_subject', 'Date')




class CustomRegisterSerializer(RegisterSerializer):
    is_student = serializers.BooleanField()
    is_teacher = serializers.BooleanField()

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'is_student', 'is_teacher')

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'password2': self.validated_data.get('password2', ''),
            'email': self.validated_data.get('email', ''),
            'is_student': self.validated_data.get('is_student', ''),
            'is_teacher': self.validated_data.get('is_teacher', '')
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        user.is_student = self.cleaned_data.get('is_student')
        user.is_teacher = self.cleaned_data.get('is_teacher')
        user.save()
        adapter.save_user(request, user, self)
        return user


class TokenSerializer(serializers.ModelSerializer):
    user_type = serializers.SerializerMethodField()

    class Meta:
        model = Token
        fields = ('key', 'user', 'user_type')

    def get_user_type(self, obj):
        serializer_data = UserSerializer(
            obj.user
        ).data
        is_student = serializer_data.get('is_student')
        is_teacher = serializer_data.get('is_teacher')
        return {
            'is_student': is_student,
            'is_teacher': is_teacher
        }
