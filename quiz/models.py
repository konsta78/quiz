from django.db import models


class Question(models.Model):
    ANSWERS = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
    )

    number = models.IntegerField(verbose_name="Номер вопроса")
    title = models.TextField(max_length=400, verbose_name="Текс вопроса")
    ans1 = models.TextField(max_length=20, verbose_name="Вариант № 1")
    ans2 = models.TextField(max_length=20, verbose_name="Вариант № 2")
    ans3 = models.TextField(max_length=20, verbose_name="Вариант № 3")
    ans4 = models.TextField(max_length=20, verbose_name="Вариант № 4")
    r_ans = models.IntegerField(choices=ANSWERS, verbose_name="Парвильный ответ")

    def __str__(self):
        return "Вопрос № " + str(self.number)


