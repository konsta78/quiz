from django.db import models


class Question(models.Model):
    ANSWERS = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
    )

    number = models.IntegerField(verbose_name="Номер вопроса")
    title = models.TextField(max_length=600, verbose_name="Текс вопроса")
    ans1 = models.TextField(max_length=100, verbose_name="Вариант № 1")
    ans2 = models.TextField(max_length=100, verbose_name="Вариант № 2")
    ans3 = models.TextField(max_length=100, verbose_name="Вариант № 3")
    ans4 = models.TextField(max_length=100, verbose_name="Вариант № 4")
    r_ans = models.CharField(max_length=2, choices=ANSWERS, verbose_name="Правильный ответ")
    text_answer = models.TextField(max_length=1500, verbose_name="Текст ответа", default="")

    def __str__(self):
        return "Вопрос № " + str(self.number)


