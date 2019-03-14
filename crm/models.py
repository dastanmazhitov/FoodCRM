from django.db import models


class Tables(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Roles(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Departments(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


"""
class Users(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    login = models.CharField(max_length=16)
    password = models.CharField(max_length=32)
    email = models.CharField(max_length=30)
    roleid = models.ForeignKey(Roles, on_delete=models.CASCADE, null=True)
    dateofadd = models.DateField(auto_now_add=True)
    phone = models.CharField(max_length=50)

    def __str__(self):
        return self.name + ' ' + self.surname
"""


class Meal_Categories(models.Model):
    name = models.CharField(max_length=50)
    departmentsid = models.ForeignKey(Departments, on_delete=models.CASCADE, null=True)


class Meals(models.Model):
    name = models.CharField(max_length=50)
    categoryid = models.ForeignKey(Meal_Categories, on_delete=models.CASCADE, null=True)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.name
