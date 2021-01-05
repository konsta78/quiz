from django.shortcuts import render
from django.views import View
from .models import Question

# кол-во вопросов
num_of_questions = {'all_questions': len(Question.objects.all()) - 1}


def set_context(number):
    """
    Выбор вопроса по ключю (primary key)
    """
    return {'question': Question.objects.get(pk=number)}


class IndexView(View):
    """
    Отображение стартовой страницы
    """
    def get(self, request):
        return render(request, 'quiz/index.html')


class QuizView(View):
    """
    Отображение страницы с вопросом и вариантами ответа
    """
    def get(self, request):
        num = request.GET.get("nextq")
        if not num:
            num = 1
        else:
            num = int(num) + 1
            if num > num_of_questions["all_questions"]:
                return render(request, 'quiz/index.html')

        return render(request, 'quiz/quiz.html', set_context(num))




