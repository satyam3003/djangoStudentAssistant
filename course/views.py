from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from users.models import Profile, LectureLink


# Create your views here.
@login_required
def home(request):
    user_data = Profile.objects.filter(user=request.user)
    all_subscribed_courses = []
    for u in user_data:
        sub_courses = u.courses.all()
        for c in sub_courses:
            all_subscribed_courses.append(c)
    context = {
        'all_subscribed_courses': all_subscribed_courses
    }
    return render(request, 'course/homepage.html', context)


# Course details -> list of lectures
@login_required
def course_detail(request, course):
    show_course = LectureLink.objects.filter(course__course_code=course)
    context = {
        'course': show_course,
    }
    return render(request, 'course/course.html', context)


@login_required
def lecture(request, lecture_id):
    lecture_display = LectureLink.objects.get(id=lecture_id)
    context = {
        'lecture': lecture_display,
    }
    return render(request, 'course/lecture.html', context)
