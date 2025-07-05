from django.db import models

# Create your models here.

class TodoApp(models.Model):
    text = models.CharField(max_length=128)
    to_be_finished = models.DateTimeField()
    is_completed = models.BooleanField(default=False)
    created_st = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'Todo_app'
