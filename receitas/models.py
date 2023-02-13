from django.db import models

# Create your models here.
class Receita():
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=165)
    slug = models.SlugField()
    preparation_time = models.IntegerField()
    preparation_time_unit = models.CharField(max_length=65)
    servings_time = models.IntegerField()
    servings_time_unit = models.CharField(max_length=65)
    preparation_steps = models.TextField()
    preparation_steps_is_html = models.BooleanField()
    created_at = models.DatetimeField(auto_now_add=True)
    updated_at = models.DatetimeField(auto_now=True)
    is_posted = models.BooleanField(defautl=False)
    cover = models.ImageField(upload_to='receitas/covers/%Y/%m/%d/')
    