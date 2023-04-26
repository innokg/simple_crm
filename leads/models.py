from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser
from loguru import logger


class User(AbstractUser):
    """
    creating user model in our database
    """
    is_organisor = models.BooleanField(default=True)
    is_agent = models.BooleanField(default=False)


class UserProfile(models.Model):  # страничка, которую видит юзер когда залогиниться
    user = models.OneToOneField(User, on_delete=models.CASCADE) # agent is a user, user inherits from User model

    def __str__(self):
        return self.user.username


class Lead(models.Model):
    """
    creating lead model in our database
    """
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    agent = models.ForeignKey("Agent", null=True, blank=True, on_delete=models.SET_NULL) # create a foreign key to Agent model here
    
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Agent(models.Model):
    """
    creating agent model in our database
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE) # agent is a user, user inherits from User model
    organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE) 

    def __str__(self):
        return self.user.email



def post_user_created_signal(sender, instance, created, **kwargs):
    logger.info(f"New user created: {instance}, created: {created}")
    if created:
        UserProfile.objects.create(user=instance)



post_save.connect(post_user_created_signal, sender=User)