from django.db import models


class File(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    file = models.FileField()

    class Meta:
        verbose_name = "File"
        verbose_name_plural = "Files"

    def __str__(self):
        return self.file.name
