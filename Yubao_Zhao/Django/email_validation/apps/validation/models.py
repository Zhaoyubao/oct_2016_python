from __future__ import unicode_literals
from django.db import models
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

class EmailManager(models.Manager):
    def validate(self, email):
        errors = []
        if not email or email.isspace():
            errors.append("Please enter the email address!")
        elif not EMAIL_REGEX.match(email):
            errors.append("Email is invalid!")
        elif Email.emailMgr.filter(email__iexact=email).exists():
            errors.append("Email already exists!")

        if errors:
            return (False, errors)
        else:
            e = Email.emailMgr.create(email=email)
            return (True, e)

class Email(models.Model):
    email = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    emailMgr = EmailManager()
