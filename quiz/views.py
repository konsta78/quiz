from django.shortcuts import render, redirect
from django.views import View
from .models import Question

# кол-во вопросов
num_of_questions = {'all_questions': len(Question.objects.all())}


class IndexView(View):
    """
    Отображение стартовой страницы
    """
    user_r_a = 0
    flag = 1

    def get(self, request):
        return render(request, 'quiz/index.html')


class QuizView(View):
    """
    Отображение страницы с вопросом и вариантами ответа
    """

    def check_num_question(self, request, template, **answer):
        num = request.GET.get("question")
        img_style = 'height'
        if not num:
            num = 1
        else:
            num = int(num) + 1
            if num > num_of_questions["all_questions"]:
                return redirect('results')
            elif num in [5, 6]:
                img_style = 'width'

        context = {'question': Question.objects.get(pk=num), 'answer': answer, 'img_style': img_style}
        return render(request, template, context)

    def get(self, request):
        IndexView.flag = 1
        num = self.check_num_question(request, 'quiz/quiz.html')
        return num

    def post(self, request):
        if request.method == 'POST':
            answer = request.POST.get('ans_but')
            r = request.POST.get('right_answer')

            if answer == r and IndexView.flag == 1:
                IndexView.user_r_a += 1
                IndexView.flag = 0

        num = self.check_num_question(request, 'quiz/answer.html', answer=answer)
        return num


class ResultsView(View):
    def get(self, request):
        context = {'user_results': IndexView.user_r_a}
        IndexView.user_r_a = 0
        return render(request, 'quiz/results.html', context)