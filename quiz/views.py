from django.shortcuts import render, redirect
from django.views import View
from .models import Question

# словарь с правильными ответами
RIGHT_ANSWERS = {
    1: '1', 2: '2', 3: '1', 4: '3', 5: '2',
    6: '3', 7: '4', 8: '2', 9: '4', 10: '2',
    11: '3', 12: '2', 13: '1', 14: '4', 15: '3',
    16: '2', 17: '4', 18: '1', 19: '3', 20: '4',
}


class IndexView(View):
    """
    Отображение стартовой страницы
    """
    users_answers = {} # ответы пользователя

    def get(self, request):
        return render(request, 'quiz/index.html')


class QuizView(View):
    """
    Отображение страницы с вопросом и вариантами ответа
    """

    def get(self, request):
        try:
            # получаем токен пользователя и инициализируем его словпрь с ответами
            token = request.headers['Cookie'].split('; ')[0].split('csrftoken=')[1]
            IndexView.users_answers[token] = {}
        except:
            pass
        context = {'question': Question.objects.get(pk=1)}
        return render(request, 'quiz/quiz.html', context)

    def post(self, request):
        num = int(request.POST.get("question"))  # номер текущего вопроса

        if request.POST.get('ans_but'):
            answer = request.POST.get('ans_but')  # ответ пользователя (№ кнопки)

            token = request.headers['Cookie'].split('; ')[0].split('csrftoken=')[1]

            if token not in IndexView.users_answers:
                IndexView.users_answers[token] = {}
            IndexView.users_answers[token][num] = answer

            # выбор шаблона для отображения ответа (по высоте или по ширине)
            if num in [5, 8, 9, 10, 12, 13, 14, 15, 16, 18, 19, 20]:
                template = 'quiz/answer_w.html'
            else:
                template = 'quiz/answer.html'

            context = {'question': Question.objects.get(pk=num), 'answer': answer}
            return render(request, template, context)

        # проверка окончания теста (всего 20 вопросов)
        num += 1
        if num > 20:
            return redirect('results')

        context = {'question': Question.objects.get(pk=num)}
        return render(request, 'quiz/quiz.html', context)


class ResultsView(View):
    """
    Подсчет результатов и их отображение на странице
    """
    def get(self, request):

        user_right_answers = 0  # счетчик правильных ответов
        token = request.headers['Cookie'].split('; ')[0].split('csrftoken=')[1]
        user_answers = IndexView.users_answers[token]

        for i in range(1, 21):
            if user_answers[i] == RIGHT_ANSWERS[i]:
                user_right_answers += 1

        context = {'user_results': user_right_answers}
        # удаление из общего словаря с ответами результаты текущего пользователя
        del IndexView.users_answers[token]
        return render(request, 'quiz/results.html', context)
