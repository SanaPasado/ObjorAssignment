from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):
    def normalize_username(self, username):
        """Normalize the username by converting it to lowercase and removing leading/trailing whitespace."""
        if not username:
            raise ValueError('Users must have a username')
        return username.lower().strip()

    def create_user(self, username, password=None, is_active=True, is_staff=False, is_admin=False):
        if not username:
            raise ValueError('Users must have a username ')
        if not password:
            raise ValueError('Users must have a password')

        # Correctly call normalize_username and assign to model fields
        user_obj = self.model(
            username=self.normalize_username(username),
            is_active=is_active,
            is_staff=is_staff,
            is_admin=is_admin
        )
        user_obj.set_password(password)
        user_obj.save(using=self._db)

        return user_obj

    def create_staffuser(self, username, password=None):
        user = self.create_user(
            username,
            password=password,
            is_active=True,
            is_staff=True
        )
        return user

    def create_superuser(self, username, password=None):
        user = self.create_user(
            username,
            password=password,
            is_active=True,
            is_staff=True,
            is_admin=True
        )
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        max_length=255,
        unique=True,
    )
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.username

    @property
    def staff_status(self):
        return self.is_staff

    @property
    def admin_status(self):
        return self.is_admin

    @property
    def active_status(self):
        return self.is_active

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin
