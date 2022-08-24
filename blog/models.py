from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    update = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    discription = models.TextField(verbose_name='Контент')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
        ordering = ['-date']