from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    category = models.ForeignKey(Category)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Product(models.Model):
    subcategory = models.ForeignKey(Subcategory)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


