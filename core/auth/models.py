from django.db import models
from rest_framework.authtoken.models import Token


class AuthTokenManager(models.Manager):
    pass


class AuthToken(Token):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    object = AuthTokenManager

    class Meta:
        db_table = 'auth.auth_token'
        managed = True
