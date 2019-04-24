from rest_framework.routers import DefaultRouter
from .views import UserViewSet,StudentViewSet, FacultyViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, base_name='users')
router.register(r'student', StudentViewSet, base_name='student')
router.register(r'faculty', FacultyViewSet, base_name='faculty')
urlpatterns = router.urls
