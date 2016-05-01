from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    date_of_death = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    nationality = models.CharField(max_length=255, blank=True)
    bio = models.TextField(blank=True)
    slug = models.SlugField(max_length=255)
    url = models.URLField(max_length=255, verbose_name="Extenal Link URL", blank=True)
    image = models.ImageField(upload_to="images/catalogue/author", null=True, blank=True)

    def get_fullname(self):
        """
        Returns Author's concatenated full name.
        """
        return "{} {}".format(self.first_name, self.surname)

    def __str__(self):
        return self.get_fullname()

class Book(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    pub_date = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    image = models.ImageField(upload_to="images/catalogue/book", null=True, blank=True)
    isbn = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(max_length=255)
    url = models.URLField(max_length=255, verbose_name="Extenal Link URL", blank=True)

    def __str__(self):
        return self.title

class CarouselSlide(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    image = models.ImageField(upload_to="images/catalogue/homepage", null=True, blank=True)
    url = models.URLField(max_length=255, verbose_name="Extenal Link URL", blank=True)
    created_on = models.DateField(auto_now=True, null=True, blank=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Homepage Carousel Slide"
