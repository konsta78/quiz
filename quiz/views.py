from django.shortcuts import render
from django.views import View
from .models import Question


def set_context(number=1):
    context = {'question': Question.objects.get(pk=number)}
    # context = {'question': Question.objects.all()}
    return context

class IndexView(View):
    def get(self, request):
        return render(request, 'quiz/index.html')


class QuizView(View):
    def get(self, request):

        question_number = request.GET.get("question_number")
        print("===> ", question_number)

        if not question_number:
            question_number = 4
        else:
            question_number = int(question_number)

        #return render(request, 'quiz/quiz.html', set_context(4))
        return render(request, 'quiz/quiz.html', set_context(question_number))
