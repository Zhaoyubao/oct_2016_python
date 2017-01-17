from __future__ import unicode_literals
from django.db import models
import re, bcrypt

NAME_REGEX = re.compile(r'^[a-zA-Z\s]+$')
ALIAS_REGEX = re.compile(r'^[\w\s]+$')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
SPACE_REGEX = re.compile('.*\s')

class UserManager(models.Manager):
    def validate_reg(self, input):      
        errors = []
        name = input['name']
        alias = input['alias']
        email = input['email']
        pw = input['pw']
        pw_conf = input['pw_confirm']
        if not name or name.isspace():
            errors.append(("Please enter your name!","name"))
        elif not NAME_REGEX.match(name):
            errors.append(("Name is invalid!","name"))
        if not alias or alias.isspace():
            errors.append(("Please enter your alias!","alias"))
        elif not ALIAS_REGEX.match(alias):
            errors.append(("Alias is invalid!","alias"))
        if not email or email.isspace():
            errors.append(("Please enter your email!","email"))
        elif not EMAIL_REGEX.match(email):
            errors.append(("Email is invalid!","email"))
        elif self.filter(email__iexact=email).exists():
            errors.append(("Email already exists!","register"))
        if not pw or pw.isspace():
            errors.append(("Please create a new password.","pw"))
        elif SPACE_REGEX.match(pw) or len(pw) < 8:
            errors.append(("Please create a new password as per the criteria.","pw"))
        if not pw == pw_conf:
            errors.append(("The passwords entered don't match.","confirm"))

        if errors:
            return (False, errors)
        else:
            hashed = bcrypt.hashpw(pw.encode(), bcrypt.gensalt())
            user = self.create(name=name, alias=alias, email=email, pw_hash=hashed)
            return (True, user.id)

    def validate_log(self, input):
        errors = []
        user = User.objects.filter(email=input['email'])
        if user.exists():
            hashed_pw = user[0].pw_hash.encode()
            input_pw = input['pw'].encode()
            if bcrypt.checkpw(input_pw, hashed_pw):
                return (True, user[0].id)
            else:
                errors.append(("Incorrect password!","login_pw"))
        else:
            errors.append(("Email address doesn't exist!","login_email"))
        return (False, errors)

class User(models.Model):
    name = models.CharField(max_length=100)
    alias = models.CharField(max_length=55)
    email = models.CharField(max_length=100)
    pw_hash = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

class Author(models.Model):
    name = models.CharField(max_length=55)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Book(models.Model):
    title = models.CharField(max_length=55)
    author = models.ForeignKey(Author)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Review(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User)
    book = models.ForeignKey(Book)
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
