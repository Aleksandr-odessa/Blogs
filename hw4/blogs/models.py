from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
	title = models.TextField()
	text = models.TextField()
	slug = models.SlugField(unique = True, verbose_name='Идентификатор')
	created_by = models.ForeignKey(User, on_delete=models.CASCADE)
	created_at = models.DateField()

	def __str__(self):
		return self.title