from django.db import models
from django.urls import reverse


class Legend(models.Model):
    POSITION_CHOICES = [
        ('GK', 'Вратарь'),
        ('DEF', 'Защитник'),
        ('MID', 'Полузащитник'),
        ('FWD', 'Нападающий'),
    ]

    name = models.CharField(max_length=100, verbose_name='Имя легенды')
    position = models.CharField(max_length=3, choices=POSITION_CHOICES, verbose_name='Позиция')
    years_at_club = models.CharField(max_length=20, verbose_name='Годы в клубе')
    image = models.ImageField(upload_to='legends/', blank=True, null=True, verbose_name='Фотография')
    description = models.TextField(verbose_name='Описание')
    achievements = models.TextField(verbose_name='Достижения')
    order = models.IntegerField(default=0, verbose_name='Порядок отображения')

    class Meta:
        verbose_name = 'Легенда'
        verbose_name_plural = 'Легенды'
        ordering = ['order', 'name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('legend_detail', kwargs={'pk': self.pk})


class Trophy(models.Model):
    COMPETITION_CHOICES = [
        ('PL', 'Премьер-Лига'),
        ('FA', 'Кубок Англии'),
        ('LC', 'Кубок Лиги'),
        ('CL', 'Лига Чемпионов'),
        ('EL', 'Лига Европы'),
        ('CS', 'Суперкубок Англии'),
        ('CWC', 'Кубок Обладателей Кубков'),
    ]

    name = models.CharField(max_length=100, verbose_name='Название трофея')
    competition = models.CharField(max_length=3, choices=COMPETITION_CHOICES, verbose_name='Турнир')
    count = models.IntegerField(verbose_name='Количество')
    years = models.TextField(verbose_name='Годы побед', help_text='Перечислите годы через запятую')
    image = models.ImageField(upload_to='trophies/', blank=True, null=True, verbose_name='Изображение')

    class Meta:
        verbose_name = 'Трофей'
        verbose_name_plural = 'Трофеи'
        ordering = ['competition']

    def __str__(self):
        return f"{self.name} ({self.count})"


class HistoryMilestone(models.Model):
    year = models.IntegerField(verbose_name='Год')
    title = models.CharField(max_length=200, verbose_name='Событие')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='milestones/', blank=True, null=True, verbose_name='Изображение')

    class Meta:
        verbose_name = 'Историческая веха'
        verbose_name_plural = 'Исторические вехи'
        ordering = ['year']

    def __str__(self):
        return f"{self.year}: {self.title}"