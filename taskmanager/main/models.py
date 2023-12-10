from django.db import models


class Task(models.Model):
    title = models.CharField('Title name', max_length=50)
    task = models.TextField('Info about task')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'