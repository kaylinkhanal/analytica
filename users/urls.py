from rest_framework.routers import DefaultRouter
from .views import UserViewSet,StudentViewSet, FacultyViewSet,SubjectViewSet,SelectedSubjectViewSet,AttendanceRecordViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, base_name='users')
router.register(r'student', StudentViewSet, base_name='student')
router.register(r'faculty', FacultyViewSet, base_name='faculty')
router.register(r'subject', SubjectViewSet, base_name='subject')
router.register(r'selectedsubject', SelectedSubjectViewSet, base_name='selectedsubject')
router.register(r'attendancerecord', AttendanceRecordViewSet, base_name='attendancerecord')
urlpatterns = router.urls
