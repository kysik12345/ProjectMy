from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from slugify import slugify
from django.urls import reverse

User = get_user_model()
# Create your models here.
class Post(models.Model):
    # author = models.CharField(max_length=50, verbose_name="Автор")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    text = models.TextField(verbose_name="Текст поста")
    created_at = models.DateTimeField(auto_now=True, verbose_name="Опубликовано", editable=False)
    image = models.ImageField(upload_to='posts/', null=True, verbose_name="Изображение")
    slug = models.SlugField(max_length=200, unique=True, editable=False, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute(self):
        return reverse('myblog:post_detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    def __str__(self):
        return self.title












