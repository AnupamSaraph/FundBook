from django.db import models


class Project (models.Model):
	title = models.CharField(max_length=100)
	start_date = models.DateField()

def __unicode__(self):
	return self.title
