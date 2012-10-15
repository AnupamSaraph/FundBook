from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

class Drinker(models.Model):
	user	= models.OneToOneField(User)
	register_date = models.DateField()
	name =	models.CharField(max_length=100)

	def __unicode__(self):
		return self.name		

# create our user object to attach to our drinker object
#def create_drinker_user_callback(sender,instance, **Kwargs):
#	drinker. new = Drinker.objects.get_or_create(user=instance)
#post_save.connect(create_drinker_user_callback, User)


