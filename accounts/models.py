from django.contrib.auth.models import (AbstractBaseUser, AbstractUser,
                                        BaseUserManager)
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, username):
        if not email:
            raise ValueError("User's must have an email address")

        email = self.normalize_email(email)
        user = self.model(email=email, username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, email, password, username):
        

        user = self.create_user(email, password=password, username=username)
        user.is_admin=True
        user.is_staff=True
        user.is_active=True
        user.save(using=self._db)
        return user



class User(AbstractUser):
    email = models.EmailField(verbose_name='email address', unique=True)
    username = models.CharField(verbose_name='username', max_length=50, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
