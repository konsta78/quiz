from django.shortcuts import render
from django.views import View


class IndexView(View):
    def get(self, request):
        return render(request, 'quiz/index.html')


class QuizView(View):
    def get(self, request):
        return render(request, 'quiz/quiz.html')
