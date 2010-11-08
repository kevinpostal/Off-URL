import sys
import csv
import codecs
import settings
from django.core.management import setup_environ
from django.template.defaultfilters import slugify
setup_environ(settings)
import time
from django.template.defaultfilters import slugify
from url.models import Offensive_List
from django.contrib.sites.models import Site
from tagging.models import Tag

file = open("list.csv")

reader = csv.reader(file,delimiter=',', quotechar='"')

x = 1

for row in reader:
    try:
        
        tags = slugify(row[0])
        #tags = ",".join(tags)
        
        
        vid = Offensive_List.objects.get_or_create(name=tags)

        print x
        x = x + 1
    
    except:
        import pdb; pdb.set_trace()
        raise
        
        
