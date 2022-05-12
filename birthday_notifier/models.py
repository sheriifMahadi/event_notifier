import imp
from pyexpat import model
from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Event(models.Model):
    """Database model which takes 
    a birthday event details"""
    celebrant = models.CharField(max_length=256, help_text='Celebrant Name')
    birthdate = models.DateTimeField(help_text="Date of Birth")
    slug = models.SlugField(max_length=250) 
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.celebrant)

    # class Meta:
    #     constraints = [
    #         models.UniqueConstraint(fields=['celebrant'], name='unique title for each user')
    #     ]

    def get_absolute_url(self):
        return reverse("main:detail", kwargs={'slug': self.slug})
    
    def save(self, *args, **kwargs): 
        if not self.slug:
            self.slug = slugify(self.celebrant)
        return super().save(*args, **kwargs)