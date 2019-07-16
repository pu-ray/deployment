from django.urls import path,include

from .views import StudentViewSet
from .views import CourseViewSet
from .views import TeacherViewSet



from rest_framework import routers

router = routers.DefaultRouter()
router.register("students", StudentViewSet)
router.register("courses",  CourseViewSet)
router.register("teachers", TeacherViewSet)
urlpatterns = [
path("",include(router.urls)),
]