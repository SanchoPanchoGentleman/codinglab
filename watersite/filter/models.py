from django.db import models
from django.urls import reverse

# kelvin = superuser's name
# pswrd: 1234qwer

class Filter(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=True, verbose_name="Текст инфо о фильтре")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время обновления")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name="Категории") ##category, ключ форейгн кэй который ссылается на класс Categoryf1

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:

        # verbose_name_plural = 'Filter' здесь мы пишем название списка своими буквами как захотим
        ordering = ['id'] #сортировка списка постов

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Type of filter")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})


    class Meta:
        verbose_name_plural = 'Categories'