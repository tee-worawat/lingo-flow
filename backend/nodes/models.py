from django.db import models

class Node(models.Model):
    name = models.CharField(max_length=100)
    prompt = models.TextField()

    def __str__(self):
        return self.name