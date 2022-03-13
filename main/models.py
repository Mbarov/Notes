from django.db import models
from django.conf import settings


class Note(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    full_text = models.TextField('Текст')
    date = models.DateTimeField(auto_now=True  )

    def __str__(self):
        return self.full_text[:30]

    
    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural ='Заметки'