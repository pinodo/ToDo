from django.db import models

# Create your models here.
class TodoLists(models.Model):
    title = models.CharField(max_length=200, default="Core")

    class Category(models.TextChoices):
        MONEY = "1", 'Money'
        LANGUAGE = "2", 'Language'
        HABIT = "3", 'Habit'
        JOB = "4", 'Job'
        LIFESTYLE = "5", "Life Style"
    
    category = models.CharField(max_length=20, choices=Category.choices, default=1)

    class Priority(models.TextChoices):
        IU = "1", 'Important & Urgent'
        INU = "2", 'Important & Not Urgent'
        NIU = "3", 'Not Important & Urgent'
        NINU = "4", 'Not Important & Not Urgent'

    priority = models.CharField(max_length=4, choices=Priority.choices, default=1)
    # name = models.CharField(max_length=30)
    # details = models.CharField(max_length=200)