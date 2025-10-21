from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class MyAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, user_name, email, password=None):
        if not email:
            return ValueError('User must have an email address')
        if not user_name:
            return ValueError('User must have a user name')
        user = self.model(
            email = self.normalize_email(email),  #capital letter to small letter everything normalised
            user_name = user_name,
            first_name = first_name,
            last_name = last_name,
        )

        user.set_password(password)
        user.save(using=self._db)    #specify the database
        return user

    def create_superuser(self, first_name, last_name, email, user_name, password=None):
        user = self.create_user(
            email = self.normalize_email(email),
            user_name = user_name,
            password = password,
            first_name = first_name,
            last_name = last_name,
        )

        # he is a superuser all permissions granted
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user

#account holder and uses my account manager
class Account(AbstractBaseUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length = 100, unique = True)
    phone_number = models.CharField(max_length=15, unique=True)

    #required_fiels
    date_joined = models.DateTimeField(auto_now_add = True)
    last_login = models.DateTimeField(auto_now = True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    objects = MyAccountManager()

    #login field 
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'first_name', 'last_name']

    def __str__(self):
        return self.email
    
    #compulsory required for custom user model
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    #
    def has_module_perms(self, app_label):
        return True
