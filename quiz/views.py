from django.shortcuts import render, redirect
from django.views import View
from .models import Question

# кол-во вопросов
num_of_questions = {'all_questions': len(Question.objects.all())}


class IndexView(View):
    """
    Отображение стартовой страницы
    """
    user_answers = {}

    def get(self, request):
        return render(request, 'quiz/index.html')


class QuizView(View):
    """
    Отображение страницы с вопросом и вариантами ответа
    """

    def get(self, request):
        IndexView.user_answers = {}
        context = {'question': Question.objects.get(pk=1)}
        return render(request, 'quiz/quiz.html', context)

    def post(self, request):
        num = int(request.POST.get("question"))

        if request.POST.get('ans_but'):
            answer = request.POST.get('ans_but')

            IndexView.user_answers[num] = answer

            if num in [5, 8, 9, 10, 12, 13, 14, 15, 16, 18, 19, 20]:
                template = 'quiz/answer_w.html'
            else:
                template = 'quiz/answer.html'

            context = {'question': Question.objects.get(pk=num), 'answer': answer}
            return render(request, template, context)

        num += 1
        if num > 20:
            return redirect('results')

        context = {'question': Question.objects.get(pk=num)}
        return render(request, 'quiz/quiz.html', context)


class ResultsView(View):
    def get(self, request):
        return render(request, 'quiz/results.html')
