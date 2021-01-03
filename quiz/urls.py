from django.urls import path
from .views import IndexView, QuizView

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('quiz/', QuizView.as_view(), name='quiz'),
    # path('quiz?nextq=<int>', QuizView.as_view(), name='quiz'),
]