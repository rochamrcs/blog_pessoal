from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255)
    texto = models.TextField()
    data_criacao = models.DateTimeField(default=timezone.now)
    data_publicacao = models.DateTimeField(blank=True, null=True)

    def publicacao(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo