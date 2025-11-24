from django.db import models
from django.urls import reverse


class News(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержание')
    image = models.ImageField(upload_to='news_images/', blank=True, null=True, verbose_name='Изображение')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    views = models.IntegerField(default=0, verbose_name='Просмотры')

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-date_created']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news_detail', kwargs={'pk': self.pk})