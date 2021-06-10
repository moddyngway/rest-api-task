# Foobar

This is task from Neobis
I used Django and Django, Restframework libraries in order to add rest api to my project. 

## Models

I have 4 models, 3 of them are part of main model - Course.
Other models are Category, Branch and Contact (Contact has hardcoded choices for type field (1-PHONE, 2-FACEBOOK, 3-EMAIL)).
Models are primitive and easy to understand/

```python
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
```

## Usage

Requests:

/courses

GET retrieves all the courses in database

POST adds a course into DB

example of json file to make POST request
```json
{
    "course": {
        "title": "hello",
        "description": "world",
        "logo": "link",
        "category": 1,
        "branches": [
            {
                "id": 1,
                "latitude": "test",
                "longitude": "test",
                "address": "test"
            }
        ],
        "contacts": [
            {
                "id": 1,
                "type": 1,
                "value": "tesk"
            }
        ]
    }
}
```

/courses/{course_id}

GET retrieves a course by course_id with JSON

DELETE deletes a course by course ID


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.


## Roadmap
In the near future i want to add visuals to my project with Bootstrap5. After that i will test my site and deploy my project.
