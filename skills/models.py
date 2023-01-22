from django.db import models
from django.contrib.auth.models import User


class Skills(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=300)
    speciality = models.CharField(max_length=50)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_skills_ursquz')

    class Meta:
        ordering = ['-created_at']

        def __str__(self):
            return f'{self.id} {self.title}'
