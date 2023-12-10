from django.db import models
from django.urls import reverse


# Create your models here.

class NavigationBar(models.Model):
    title = models.CharField(max_length=50, verbose_name='item bar')
    slug = models.SlugField(max_length=50, db_index=True, verbose_name='url')
    is_anchor = models.BooleanField(default=False)
    is_visible = models.BooleanField(default=True)
    order = models.PositiveSmallIntegerField()

    def get_absolute_url(self):
        if self.is_anchor:
            return reverse('app1:home') + f'#{self.slug}'

        return self.slug

    def __str__(self):
        return f'{self.title}/{self.slug}'

    class Meta:
        ordering = ('order',)