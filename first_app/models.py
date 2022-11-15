from django.db import models

# Create your models here.


class Books(models.Model):
    """informations about books"""
    name = models.CharField(max_length=20)
    book_code = models.IntegerField()
    auther = models.CharField(max_length=20)
    


    class Meta:
        db_table = 'book_library'

    def __str__(self):
        return self.name






