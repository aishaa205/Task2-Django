from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClassroomViewSet, CourseViewSet, SchoolViewSet, ExamViewSet

router = DefaultRouter()
router.register(r'classrooms', ClassroomViewSet)
router.register(r'schools', SchoolViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'exams', ExamViewSet)



urlpatterns = [
   
    # path("schools/", school_list, name="school-list"),
    # path("schools/create/", school_create, name="school-create"),
    # path("classrooms/", classroom_list, name="classroom-list"),
    # path("classrooms/create/", classroom_create, name="classroom-create"),
    # path("schools/viewset/", SchoolViewSet.as_view(), name="school-viewset"),
    # path("schools/viewset/<int:pk>/", SchoolViewSet.as_view(), name="school-detail-viewset"),
    # path("classrooms/viewset/", ClassroomViewSet.as_view(), name="classroom-viewset"),
    # path("classrooms/viewset/<int:pk>/", ClassroomViewSet.as_view(), name="classroom-detail-viewset"),
    
    path('', include(router.urls)),
]
