from django.db import models


class Student(models.Model):
    s_name = models.CharField(max_length=10, unique=True)
    s_age = models.IntegerField(default=16)
    s_sex = models.BooleanField(default=1)
    operator_time = models.DateTimeField(auto_now=True)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'student'
