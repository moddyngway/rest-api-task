from django.db import models


class Category(models.Model):
    name = models.CharField("Название", max_length=50)
    imgpath = models.CharField("Ссылка на картинку", max_length=50)

    def __str__(self):
        return self.name


class Branch(models.Model):
    latitude = models.CharField(max_length=150)
    longitude = models.CharField(max_length=150)
    address = models.CharField(max_length=150)


class Contact(models.Model):
    type = models.IntegerField("Тип")
    value = models.CharField("Значение", max_length=50)

    def __str__(self):
        return f"{self.type} : {self.value}"


class Course(models.Model):
    title = models.CharField("Название", max_length=50)
    description = models.CharField("Описание", max_length=300)
    logo = models.CharField("Ссылка на лого", max_length=100)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    contacts = models.ManyToManyField(Contact, verbose_name="Контакты")
    branches = models.ManyToManyField(Branch)

    def __str__(self):
        return self.title

