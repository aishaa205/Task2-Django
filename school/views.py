import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import School, Classroom
def json_response(data, status=200):
    return HttpResponse(json.dumps(data), content_type="application/json", status=status)


def get_object(model, pk):
    try:
        return model.objects.get(pk=pk)
    except model.DoesNotExist:
        return None


def school_list(request):
    if request.method == "GET":
        schools = list(School.objects.values("id", "name", "number_of_classes", "area"))
        return json_response(schools)

@csrf_exempt
def school_create(request):
    if request.method == "POST":
        data = json.loads(request.body)
        if not all(key in data for key in ["name", "number_of_classes", "area"]):
            return json_response({"error": "Missing required fields"}, status=400)

        school = School.objects.create(
            name=data["name"],
            number_of_classes=int(data["number_of_classes"]),
            area=float(data["area"])
        )
        return json_response({"id": school.id, "name": school.name, "number_of_classes": school.number_of_classes, "area": school.area}, status=201)


def classroom_list(request):
    if request.method == "GET":
        classrooms = list(Classroom.objects.values("id", "school", "name", "area"))
        return json_response(classrooms)

@csrf_exempt
def classroom_create(request):
    if request.method == "POST":
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
