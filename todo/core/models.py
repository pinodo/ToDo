from django.db import models

# Create your models here.
class TodoLists(models.Model):
    title = models.CharField(max_length=200, default="Untitled")

    class Category(models.TextChoices):
        MONEY = "Money", 'Money'
        LANGUAGE = "Language", 'Language'
        HABIT = "Habit", 'Habit'
        JOB = "Job", 'Job'
        LIFESTYLE = "Lifestyle", "Life Style"
    
    category = models.CharField(max_length=100, choices=Category.choices, default=1)

    class Priority(models.TextChoices):
        IMPORTANT_URGENT = "IU", 'Important & Urgent'
        IMPORTANT_NOTURGENT = "INU", 'Important & Not Urgent'
        NOTIMPORTANT_URGENT = "NIU", 'Not Important & Urgent'
        NOTIMPORTANT_NOTURGENT = "NINU", 'Not Important & Not Urgent'

    priority = models.CharField(max_length=100, choices=Priority.choices, default=1)
    # name = models.CharField(max_length=30)
    # details = models.CharField(max_length=200)