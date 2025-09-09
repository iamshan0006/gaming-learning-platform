from django.shortcuts import render
from .models import Attempt

def attempt_history(request):
    attempts = Attempt.objects.filter(student=request.user)
    return render(request, "attempts.html", {"attempts": attempts})
