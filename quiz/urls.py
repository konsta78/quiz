from django.urls import path
from .views import IndexView, QuizView, ResultsView

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('quiz/', QuizView.as_view(), name='quiz'),
    path('results/', ResultsView.as_view(), name='results'),
]