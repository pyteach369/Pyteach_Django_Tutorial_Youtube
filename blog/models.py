from django.db import models


class Post(models.Model):
    STATUS_CHOICES = (
        ('drf', 'Draft'),
        ('pub', 'Publish'),
    )

    title = models.CharField(max_length=100)
    body = models.TextField()

    status = models.CharField(choices=STATUS_CHOICES)

    def __str__(self):
        return self.title
