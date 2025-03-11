from django.db import models

# Create your models here.
class School(models.Model):
    name = models.CharField(verbose_name="school name",max_length=255)
    number_of_classes = models.IntegerField()
    area = models.FloatField() 
     
    def __str__(self):
        return self.name
    


class Classroom(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name="classrooms")
    name = models.CharField(max_length=255)
    area = models.FloatField()  

    def __str__(self):
        return f"{self.name} - {self.school.name}"     
    
   
   
class Course(models.Model):
    name = models.CharField(max_length=255)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name


class Exam(models.Model):
    file = models.FileField(upload_to='exams/')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Exam for {self.course.name} by {self.user.username}"
 
    