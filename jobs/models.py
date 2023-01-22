from django.db import models
from django.contrib.auth.models import User


class Jobs(models.Model):

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    company = models.CharField(max_length=100)
    image = models.ImageField(
        upload_to='images/', default='../default_job_posting_wpkhwf',
        blank=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
