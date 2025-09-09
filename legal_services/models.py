from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


class Legislation(models.Model):
    """модель законодательство"""
    title = models.CharField(max_length=500, verbose_name="Заголовок")
    description = models.CharField(max_length=15000, verbose_name="описание законодательства")
    created_at = models.DateField(auto_now_add=True)
    image = ProcessedImageField(
        upload_to='photos/',
        processors=[ResizeToFill(800, 600)],
        format='JPEG',
        options={'quality': 90},
    )


    def __str__(self):
        return f" {self.title} создано {self.created_at} "

    class Meta:
        verbose_name = "закон"
        verbose_name_plural = "законы"
        ordering = ["title", "created_at"]