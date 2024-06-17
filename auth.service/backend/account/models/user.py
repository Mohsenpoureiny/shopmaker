from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy  as _

from account.managers import UserManager


class User(AbstractUser):
    username = None
    mobile = models.CharField(_('phone number'), unique=True , max_length=20 , null=True , blank=True)

    USERNAME_FIELD = 'mobile'
    REQUIRED_FIELDS = []

    mobile_verified = models.BooleanField(default=False)
    site_id = models.UUIDField()

    objects = UserManager()

    def __str__(self):
        return self.mobile