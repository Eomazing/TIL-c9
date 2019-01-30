from django.shortcuts import render
from .models import Question, Choice

# Create your views here.
def index(request):
    questions = Question.objects.last()
    return render(request, 'index.html', {'questions':questions})