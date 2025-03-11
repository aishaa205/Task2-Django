import json
from django.http import HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import Classroom, Course, School, Exam
from rest_framework import viewsets, permissions
from .serializers import ClassroomSerializer, CourseSerializer, SchoolSerializer, ExamSerializer
def json_response(data, status=200):
    return HttpResponse(json.dumps(data), content_type="application/json", status=status)


def get_object(model, pk):
    try:
        return model.objects.get(pk=pk)
    except model.DoesNotExist:
        return None

@method_decorator(csrf_exempt, name="dispatch")
class SchoolViewSet(View):
    def get(self, request, pk=None):
        if pk:
            school = get_object(School, pk)
            if school is None:
                return json_response({"error": "School not found"}, status=404)
            return json_response({"id": school.id, "name": school.name, "number_of_classes": school.number_of_classes, "area": school.area})
        else:
            schools = list(School.objects.values("id", "name", "number_of_classes", "area"))
            return json_response(schools)

    def post(self, request):
        data = json.loads(request.body)
        if not all(key in data for key in ["name", "number_of_classes", "area"]):
            return json_response({"error": "Missing required fields"}, status=400)

        school = School.objects.create(
            name=data["name"],
            number_of_classes=int(data["number_of_classes"]),
            area=float(data["area"])
        )
        return json_response({"id": school.id, "name": school.name, "number_of_classes": school.number_of_classes, "area": school.area}, status=201)

@method_decorator(csrf_exempt, name="dispatch")
class ClassroomViewSet(View):
    def get(self, request, pk=None):
        if pk:
            classroom = get_object(Classroom, pk)
            if classroom is None:
                return json_response({"error": "Classroom not found"}, status=404)
            return json_response({"id": classroom.id, "school": classroom.school.id, "name": classroom.name, "area": classroom.area})
        else:
            classrooms = list(Classroom.objects.values("id", "school", "name", "area"))
            return json_response(classrooms)

    def post(self, request):
        data = json.loads(request.body)
        if not all(key in data for key in ["school", "name", "area"]):
            return json_response({"error": "Missing required fields"}, status=400)

        school = get_object(School, data["school"])
        if school is None:
            return json_response({"error": "Invalid school ID"}, status=400)

        classroom = Classroom.objects.create(
            school=school,
            name=data["name"],
            area=float(data["area"])
        )
        return json_response({"id": classroom.id, "school": classroom.school.id, "name": classroom.name, "area": classroom.area}, status=201)


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = [permissions.IsAuthenticated]

class ExamViewSet(viewsets.ModelViewSet):
    serializer_class = ExamSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Exam.objects.all()
        return Exam.objects.filter(user=user)