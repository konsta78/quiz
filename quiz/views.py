from django.shortcuts import render
from django.views import View
from .models import Question
from django.http import HttpResponse

num_of_questions = {'all_questions': len(Question.objects.all())}


def set_context(number=1):
    return {'question': Question.objects.get(pk=number)}


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
            if num > num_of_questions["all_questions"]:
                return render(request, 'quiz/index.html')

        return render(request, 'quiz/quiz.html', set_context(num))




