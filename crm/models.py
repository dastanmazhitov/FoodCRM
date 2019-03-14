from django.db import models


class Tables(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Roles(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Departments(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Meal_Categories(models.Model):
    name = models.CharField(max_length=50)
    departmentsid = models.ForeignKey(Departments, on_delete=models.CASCADE, null=True)


class Statuses(models.Model):
    name = models.CharField(max_length=100, default='in progress')

    def __str__(self):
        return self.name


class Meals(models.Model):
    name = models.CharField(max_length=50)
    categoryid = models.ForeignKey(Meal_Categories, on_delete=models.CASCADE, null=True)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.name
