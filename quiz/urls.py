from django.urls import path
from .views import IndexView, QuizView

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('quiz/', QuizView.as_view(), name='quiz'),
    path('quiz/<int:question_number>', QuizView.as_view(), name='quiz'),
    path('quiz?question_number=<int:question_number>', QuizView.as_view(), name='quiz'), # <---- !!!

]