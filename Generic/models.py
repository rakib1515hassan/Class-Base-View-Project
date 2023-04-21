from django.db import models
from django.utils.safestring import mark_safe


# Creata Slug field auto depend on name and position
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver

## Auto Genarete slug field ( pip install django-autoslug )
from autoslug import AutoSlugField

#from django.utils.html import format_html

# Create your models here.

class Player(models.Model):
    name = models.CharField(max_length=25)
    #pic = models.ImageField(default="img/default_pic.jpg", upload_to="Profile")
    pic = models.ImageField(upload_to="Profile", null=True, blank=True)
    age = models.IntegerField(default=18)
    play = models.CharField(max_length=30)
    position = models.CharField(max_length=30)

    slug = AutoSlugField(default=None, null=True, blank=True, unique=True, populate_from='name',editable=False)
    ## slug = models.SlugField(default=None, null=True, blank=True, unique=True, max_length=100)

    def admin_photo(self):
        return mark_safe('<img src="{}" width="60" style="border-radius: 100%;" />'.format(self.pic.url))
    admin_photo.short_descreption = 'pic'
    admin_photo.allow_tags = True

    def __str__(self):
        return self.name



## This is another way to declare slug fild---------------------------------
## এটি class এর বাহিরে হবে--------

# @receiver(pre_save, sender=Player)
# def generate_slug(sender, instance, *args, **kwargs):
#     if not instance.slug:
#         slug = slugify(instance.name + ' ' + instance.play+ ' ' + instance.position)
#         instance.slug = slug[:99]  # truncate to maximum length of 100


