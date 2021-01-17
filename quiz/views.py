from django.shortcuts import render, redirect
from django.views import View
from .models import Question

# кол-во вопросов
num_of_questions = {'all_questions': len(Question.objects.all())}


class IndexView(View):
    """
    Отображение стартовой страницы
    """

    def get(self, request):
        IndexView.user_r_a = 0
        IndexView.flag = 1
        return render(request, 'quiz/index.html')


class QuizView(View):
    """
    Отображение страницы с вопросом и вариантами ответа
    """

    def check_num_question(self, request):
        num = request.GET.get("question")
        if not num:
            num = 1
        else:
            num = int(num) + 1

        return num

    def get(self, request):

        IndexView.flag = 1
        num = self.check_num_question(request)
        if num > num_of_questions["all_questions"]:
            return redirect('results')

        context = {'question': Question.objects.get(pk=num)}
        return render(request, 'quiz/quiz.html', context)

    def post(self, request):
        answer = request.POST.get('ans_but')
        r = request.POST.get('right_answer')

        if answer == r and IndexView.flag == 1:
            IndexView.user_r_a += 1
            IndexView.flag = 0

        num = self.check_num_question(request)
        if num in [5, 8, 9, 10, 12, 13, 14, 15, 16, 18, 19, 20]:
            template = 'quiz/answer_w.html'
        else:
            template = 'quiz/answer.html'

        context = {'question': Question.objects.get(pk=num), 'answer': answer}
        return render(request, template, context)


class ResultsView(View):
    def get(self, request):
        context = {'user_results': IndexView.user_r_a}
        IndexView.user_r_a = 0
        return render(request, 'quiz/results.html', context)
