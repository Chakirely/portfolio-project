from django.db import models

# Create A blog models
class Blog(models.Model):
# title
    title = models.CharField(max_length=255)
# pub_date
    pub_date = models.DateTimeField()
# body
    body = models.TextField()
# image
    image = models.ImageField(upload_to='images/')

# Add the Blog app to the settings
#It is added under settings under installed_APPS  as: 'job.apps.BlogConfig'

# Create a migration
# This step it is done by running this commmand in the terminal: python manage.py makemigrations


# Migrate
#This step is done by running this command: python manage.py migrate

# Add to the admin
# This step is added under admin.py where from.models import Blog and admin.site.register(Blog) is added
