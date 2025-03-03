from django.db import models
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Ad(models.Model):
    CATEGORIES = [
        ('Tanks', 'Танки'),
        ('Healers', 'Хилы'),
        ('Damage_dealers', 'ДД'),
        ('Traders', 'Торговцы'),
        ('Guild_masters', 'Гилдмастеры'),
        ('Quests_giver', 'Квестгиверы'),
        ('Blacksmiths', 'Кузнецы'),
        ('Tanners', 'Кожевники'),
        ('Potion_makers', 'Зельевары'),
        ('Spellmasters', 'Мастера заклинаний'),

    ]

    title = models.CharField(max_length=255)
    content = RichTextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
