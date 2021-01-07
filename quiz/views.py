from django.shortcuts import render
from django.views import View
from .models import Question

# кол-во вопросов
num_of_questions = {'all_questions': len(Question.objects.all())}


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
    def check_num_question(self, request, template, **answer):
        num = request.GET.get("question")
        if not num:
            num = 1
        else:
            num = int(num) + 1
            if num > num_of_questions["all_questions"]:
                return render(request, 'quiz/index.html')

        context = {'question': Question.objects.get(pk=num), 'answer': answer}
        return render(request, template, context)

    def get(self, request):
        num = self.check_num_question(request, 'quiz/quiz.html')
        return num

    def post(self, request):
        answer = request.POST.get('ans_but')
        num = self.check_num_question(request, 'quiz/answer.html', answer=answer)
        return num

