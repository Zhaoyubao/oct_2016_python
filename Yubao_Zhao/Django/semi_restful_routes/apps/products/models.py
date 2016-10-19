from __future__ import unicode_literals
from django.db import models

class ProductManager(models.Manager):
    def validate_new(self, input):
        errors = []
        name = input['name']
        desc = input['description']
        price = input['price']
        if not name or name.isspace():
            errors.append('Please input the product name!')
        if not desc or desc.isspace():
            errors.append('Please input the product description!')
        if not price:
            errors.append('Please input the product price!')
        if errors:
            return (False, errors)
        p = self.create(name=name, description=desc, price=price)
        return (True, p)

    def validate_update(self, input, id):
        p = self.get(id=id)
        name = input['name']
        desc = input['description']
        price = input['price']
        if (not name or name.isspace()) and (not desc or desc.isspace()) and not price:
            return False
        if not name or name.isspace():
            name = p.name
        if not desc or desc.isspace():
            desc = p.description
        if not price:
            price = p.price
        self.filter(id=id).update(name=name, description=desc, price=price)
        return True

class Product(models.Model):
    name = models.CharField(max_length=55)
    description = models.CharField(max_length=255)
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ProductManager()
