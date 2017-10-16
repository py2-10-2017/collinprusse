from __future__ import unicode_literals

from django.db import models

class books(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    notes = models.TextField()
    books = models.ManyToManyField(books, related_name="authors")

    def __str__(self):
        return self.first_name
