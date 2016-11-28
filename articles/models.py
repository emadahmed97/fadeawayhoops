from __future__ import unicode_literals
import datetime
from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import JSONField
from django.contrib.postgres.fields import ArrayField
from django.contrib.postgres.fields import HStoreField
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.conf import settings



# Create your models here.

def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)

class Metadata(models.Model):
    article_category = models.CharField(max_length=200)
    article_tags = models.TextField #turn into a list
    def __str__(self):
       return self.article_category

class Content(models.Model):

    article_title = models.CharField(max_length=200)
    article_tagline = models.CharField(max_length=200, null=True)
    article_author = models.CharField(max_length=2000)
    article_date = models.DateTimeField('date published')
    article_id = models.IntegerField
    article_text = models.TextField(max_length=20000, blank=True)
    article_image = models.FileField(null=True, blank=True)    # add image field to this later
    slug = models.SlugField(unique=True,null=True,blank=True,max_length=255);
    metadata = models.ForeignKey('metadata', null=True)

    heading1 = models.CharField(max_length=250,null=True,blank=True);
    paragraph1 = models.TextField(max_length=20000,null=True,blank=True);

    heading2 = models.CharField(max_length=250,null=True,blank=True);
    paragraph2 = models.TextField(max_length=20000,null=True,blank=True);

    heading3 = models.CharField(max_length=250,null=True,blank=True);
    paragraph3 = models.TextField(max_length=20000,null=True,blank=True);

    heading4 = models.CharField(max_length=250,null=True,blank=True);
    paragraph4 = models.TextField(max_length=20000,null=True,blank=True);

    heading5 = models.CharField(max_length=250,null=True,blank=True);
    paragraph5 = models.TextField(max_length=20000,null=True,blank=True);

    heading6 = models.CharField(max_length=250,null=True,blank=True);
    paragraph6 = models.TextField(max_length=20000,null=True,blank=True);

    heading7 = models.CharField(max_length=250,null=True,blank=True);
    paragraph7 = models.TextField(max_length=20000,null=True,blank=True);

    heading8 = models.CharField(max_length=250,null=True,blank=True);
    paragraph8 = models.TextField(max_length=20000,null=True,blank=True);

    heading9 = models.CharField(max_length=250,null=True,blank=True);
    paragraph9 = models.TextField(max_length=20000,null=True,blank=True);

    heading10 = models.CharField(max_length=250,null=True,blank=True);
    paragraph10 = models.TextField(max_length=20000,null=True,blank=True);

    heading11 = models.CharField(max_length=250,null=True,blank=True);
    paragraph11 = models.TextField(max_length=20000,null=True,blank=True);

    heading12 = models.CharField(max_length=250,null=True,blank=True);
    paragraph12 = models.TextField(max_length=20000,null=True,blank=True);

    heading13 = models.CharField(max_length=250,null=True,blank=True);
    paragraph13 = models.TextField(max_length=20000,null=True,blank=True);

    heading14 = models.CharField(max_length=250,null=True,blank=True);
    paragraph14 = models.TextField(max_length=20000,null=True,blank=True);

    heading15 = models.CharField(max_length=250,null=True,blank=True);
    paragraph15 = models.TextField(max_length=20000,null=True,blank=True);

    heading16 = models.CharField(max_length=250,null=True,blank=True);
    paragraph16 = models.TextField(max_length=20000,null=True,blank=True);

    heading17 = models.CharField(max_length=250,null=True,blank=True);
    paragraph17 = models.TextField(max_length=20000,null=True,blank=True);

    


    def save(self, *args, **kwargs):
                # Uncomment if you don't want the slug to change every time the name changes
                #if self.id is None:
                        #self.slug = slugify(self.name)
            self.slug = slugify(self.article_title)
            super(Content, self).save(*args, **kwargs)

    def __unicode__(self):
            return self.article_title

    def __str__(self):
        return self.article_title












class LongArticle(models.Model):

    article_title = models.CharField(max_length=200,null=True)
    article_tagline = models.CharField(max_length=200, null=True)
    article_author = models.CharField(max_length=2000, null=True)
    article_date = models.DateTimeField('date published',null=True)
    article_id = models.IntegerField(null=True)
    article_text = models.TextField(max_length=20000,null=True)
    DEFAULT_PK =1
    metadata = models.ForeignKey(Metadata, null=True)
    article_image = models.FileField(null=True, blank=True)    # add image field to this later

    heading1 = models.CharField(max_length=250,null=True);
    paragraph1 = models.TextField(max_length=20000,null=True);

    heading2 = models.CharField(max_length=250,null=True);
    paragraph2 = models.TextField(max_length=20000,null=True);

    heading3 = models.CharField(max_length=250,null=True);
    paragraph3 = models.TextField(max_length=20000,null=True);

    heading4 = models.CharField(max_length=250,null=True);
    paragraph4 = models.TextField(max_length=20000,null=True);

    heading5 = models.CharField(max_length=250,null=True);
    paragraph5 = models.TextField(max_length=20000,null=True);

    heading6 = models.CharField(max_length=250,null=True);
    paragraph6 = models.TextField(max_length=20000,null=True);

    heading7 = models.CharField(max_length=250,null=True);
    paragraph7 = models.TextField(max_length=20000,null=True);

    heading8 = models.CharField(max_length=250,null=True);
    paragraph8 = models.TextField(max_length=20000,null=True);

    heading9 = models.CharField(max_length=250,null=True);
    paragraph9 = models.TextField(max_length=20000,null=True);

    heading10 = models.CharField(max_length=250,null=True);
    paragraph10 = models.TextField(max_length=20000,null=True);

    heading11 = models.CharField(max_length=250,null=True);
    paragraph11 = models.TextField(max_length=20000,null=True);

    heading12 = models.CharField(max_length=250,null=True);
    paragraph12 = models.TextField(max_length=20000,null=True);

    heading13 = models.CharField(max_length=250,null=True);
    paragraph13 = models.TextField(max_length=20000,null=True);

    heading14 = models.CharField(max_length=250,null=True);
    paragraph14 = models.TextField(max_length=20000,null=True);

    heading15 = models.CharField(max_length=250,null=True);
    paragraph15 = models.TextField(max_length=20000,null=True);

