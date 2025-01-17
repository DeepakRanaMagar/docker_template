from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Accounts(models.Model):
    email = models.EmailField(_("Email"), max_length=254)
    username = models.CharField(_("Username"), max_length=50)
    password = models.CharField(_("Password"), max_length=50)
    
    def __str__(self):
        return {self.username} - {self.email}
    
    class Meta:
        db_table = 'Account'
        managed = True
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'
        
class UserProfile(models.Model):
    user = models.OneToOneField("accounts.Accounts", verbose_name=_("User Profile"), on_delete=models.CASCADE)
    first_name = models.CharField(_("First Name"), max_length=50)
    last_name = models.CharField(_("Last Name"), max_length=50)
    phone_number = models.CharField(_("Phone Number"), max_length=50, blank=True)
    address = models.CharField(_("Address"), max_length=50, blank=True, null=True)
    
    def __str__(self):
        return {self.first_name} + {self.last_name}
    
    class Meta:
        db_table = 'UserProfile'
        managed = True
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'
        