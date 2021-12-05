from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
import django.core.exceptions
from django.urls import reverse



# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length = 200, unique = True, verbose_name = "Название", error_messages ={'unique': "Такое название, уже есть. Назовите другим именем"})
	text = models.TextField(verbose_name = "Текст ")
	slug = models.SlugField(unique = True, blank = True, verbose_name = "URL", allow_unicode =True )
	created_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name = "Автор")
	created_at = models.DateTimeField(verbose_name = "Дата создания",auto_now = True)


	def save(self,  *args, **kwargs):
		self.slug = slugify(self.title, allow_unicode=True)
		return super(Post, self).save(*args, **kwargs)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post_detail', kwargs = {'slug':self.slug})