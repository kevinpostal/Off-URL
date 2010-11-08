from django.db import models
from django.contrib.sites.models import Site

key_length = 2000

class URL(models.Model):
    link = models.URLField()
    short_link = models.URLField()
    key = models.CharField(max_length=key_length, unique=True, primary_key=True)
    
    creation_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def generate_url(self, force_insert=False, force_update=False):  
        from string import lowercase, digits
        from random import choice
        from django.db import IntegrityError      
        
        def randomize():
            pattern = '%s%s' % (lowercase, digits)
            try:
                # First try to save with key without checking to create it fast
                self.key = ('').join([choice(pattern) for y in range(5)])
                self.key += "/%s_%s.mov" % (Offensive_List.objects.order_by('?')[0],Offensive_List.objects.order_by('?')[0])

                # Then we need to save the link of the file
                self.short_link = current_site.domain + self.key
                super(URL, self).save(force_insert, force_update)
            except IntegrityError, e:
                # if an exception is raised, we make sure the the key is unique
                # and save it. if something else is wrong on kwargs it will raised the                 # exception.
                while True:
                    self.key = ('').join([choice(pattern) for y in range(5)])
                    if not self.objects.filter(key = self.key):
                        super(URL, self).save(force_insert, force_update)


        if not self.key:
            current_site = Site.objects.get_current()        
            randomize()

        else:
            randomize()
            super(URL, self).save(force_insert, force_update)
                     
        
class Offensive_List(models.Model):
    name = models.CharField(max_length=255,unique=True)

    def __unicode__(self):
        return self.name
