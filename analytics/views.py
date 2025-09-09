from django.shortcuts import render
from gameplay.models import Attempt

def teacher_dashboard(request):
    attempts = Attempt.objects.all().select_related("student", "quiz")
    return render(request, "teacher_dashboard.html", {"attempts": attempts})

