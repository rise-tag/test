
from django.db import models

# Create your models here.
class Basesettings(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок сайта'
    )

    facebook = models.URLField(
        verbose_name='Ссылк на Фейсбук'
    )
    twitter = models.URLField(
        verbose_name='Ссылка на Твитер'
    )
    github = models.URLField(
        verbose_name='Ссылка на Гитхаб'
    )
    email = models.URLField(
        verbose_name='Ссылка на Емайл'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Основная настройка сайта'
        verbose_name_plural = 'Основные настройки сайта'
        
class Empty(models.Model):
    place = models.CharField(
        max_length=255,
        verbose_name="ячейка"
    )

def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Пустая ячейка'
        verbose_name_plural = 'Пустая ячейка'