from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    name = models.CharField("Название книги", max_length=128)
    author = models.CharField("Автор", max_length=128)
    short_description = models.TextField("Краткое описание")
    description = models.TextField("Полное описание")
    photo = models.FileField("Фото обложки", upload_to='media/')

    def __str__(self):
        return f'{self.name} by {self.author}'

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField("Отзыв")
    date = models.DateField("Время", auto_now=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username}: {self.date}'

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"