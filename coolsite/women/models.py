from django.db import models
from django.urls import reverse

class Women(models.Model):
    title = models.CharField(max_length=255, verbose_name="Վերնագիր")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=True, verbose_name="Հոդվածի տեքստը")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Նկար")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Ստեղծման ամսաթիվը")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Փոփոխման ամսաթիվը")
    is_published = models.BooleanField(default=True, verbose_name="Հրապարակում")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name="Կատեգորիաներ")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Հայտնի կին'
        verbose_name_plural = 'Հայտնի կանայք'
        ordering = ['id']


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Կատեգորիա")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Կատեգորիա'
        verbose_name_plural = 'Կատեգորիաներ'
        ordering = ['id']
