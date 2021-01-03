from django.shortcuts import render
from django.views import View
from .models import Question
from django.http import HttpResponse


def set_context(number=1):
    context = {'question': Question.objects.get(pk=number)}
    # context = {'question': Question.objects.all()}
    return context

class IndexView(View):
    def get(self, request):
        return render(request, 'quiz/index.html')


class QuizView(View):
    def get(self, request):
        num = request.GET.get("nextq")
        print(num)
        if not num:
            num = 1
        else:
            num = int(num) + 1
        return render(request, 'quiz/quiz.html', set_context(num))




