from django.urls import path
from .views import school_list, school_create, classroom_list, classroom_create
from .viewsets import SchoolViewSet, ClassroomViewSet

urlpatterns = [
   
    path("schools/", school_list, name="school-list"),
    path("schools/create/", school_create, name="school-create"),
    path("classrooms/", classroom_list, name="classroom-list"),
    path("classrooms/create/", classroom_create, name="classroom-create"),
    path("schools/viewset/", SchoolViewSet.as_view(), name="school-viewset"),
    path("schools/viewset/<int:pk>/", SchoolViewSet.as_view(), name="school-detail-viewset"),
    path("classrooms/viewset/", ClassroomViewSet.as_view(), name="classroom-viewset"),
    path("classrooms/viewset/<int:pk>/", ClassroomViewSet.as_view(), name="classroom-detail-viewset"),
]
