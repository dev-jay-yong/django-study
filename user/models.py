from django.db import models


class User(models.Model):
    email = models.EmailField(verbose_name='Email')
    password = models.CharField(max_length=255, verbose_name='Password')
    register_date = models.DateTimeField(auto_now_add=True, verbose_name='Registered Date')

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

