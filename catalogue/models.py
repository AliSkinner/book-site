from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False)
    date_of_death = models.DateField(auto_now=False, auto_now_add=False)
    nationality = models.DateField(auto_now=False, auto_now_add=False)
    bio = models.TextField()
    slug = models.SlugField(max_length=255)
    url = models.URLField(max_length=255, verbose_name="Extenal Link URL")

    def __str__(self):
        return "{} {}".format(self.first_name, self.surname)

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField()
    pub_date = models.DateField(auto_now=False, auto_now_add=False)
    # image = models.ImageField(upload_to=None) 
    isbn = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    url = models.URLField(max_length=255, verbose_name="Extenal Link URL")

    def __str__(self):
        return self.title
