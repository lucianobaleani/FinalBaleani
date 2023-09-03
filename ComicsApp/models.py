from django.db import models


class Author(models.Model):
    def __str__(self):
        return f"{self.name} {self.role} {self.currently_active}"

    name = models.CharField(max_length=70, unique=True)
    role = models.CharField(max_length=20)
    currently_active = models.BooleanField()


class Editorial(models.Model):
    def __str__(self):
        return f"{self.name}  {self.country} {self.state}"

    name = models.CharField(max_length=70)
    country = models.CharField(max_length=70)
    state = models.CharField(max_length=70)


class Comic(models.Model):
    def __str__(self):
        return f"{self.name} {self.editorial} {self.author} {self.published_year}"

    name = models.CharField(max_length=70)
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    published_year = models.IntegerField()
    # autoconclusive = models.BooleanField()
    # cover_image = models.ImageField(upload_to="covers/")
