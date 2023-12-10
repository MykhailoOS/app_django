from django.db import models


class Features(models.Model):
    title = models.CharField(max_length=20, verbose_name='feature_item')
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=55, db_index=True, verbose_name='url')
    is_visible = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Features"
        unique_together = ['id', 'slug']

    def __str__(self):
        return f"{self.title}"


class Download(models.Model):
    text = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "Download"

    def __str__(self):
        return f"{self.text}"
