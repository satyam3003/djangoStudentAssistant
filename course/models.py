from django.db import models


# Create your models here.
class Year(models.Model):
    year = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.year}"


class Branch(models.Model):
    branch = models.CharField(max_length=120)

    def __str__(self):
        return f"{self.branch}"


class CourseAbbrivation(models.Model):
    course_abbr = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.course_abbr}"


class Course(models.Model):
    course_code = models.CharField(max_length=20)
    course_name = models.CharField(max_length=100)
    course_year = models.ForeignKey(Year, default=None, on_delete=models.CASCADE)
    course_abbriv = models.ForeignKey(CourseAbbrivation, default=None, on_delete=models.CASCADE)
    course_branch = models.ForeignKey(Branch, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.course_name} - {self.course_code}"


class LectureLink(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    lec_num = models.IntegerField()
    lec_date_time = models.DateTimeField(auto_now_add=True)
    lec_link = models.URLField()

    def __str__(self):
        return f"{self.course} - {self.lec_num}"
