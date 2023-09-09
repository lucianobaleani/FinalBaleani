from django.db import models
from django.contrib.auth.models import User


class Comic(models.Model):
    def __str__(self):
        return f"{self.cover_image}{self.name}"

    cover_image = models.ImageField(upload_to="covers")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=70)
    editorial = models.CharField(max_length=70)
    author = models.CharField(max_length=70)
    published_year = models.IntegerField()


class ChatBox(models.Model):
    comment = models.ForeignKey(
        Comic, related_name="comment", on_delete=models.CASCADE, null=True
    )
    name = models.CharField(max_length=40)
    message = models.TextField(null=True, blank=True)
    comment_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-comment_date"]

    def __str__(self):
        return "%s - %s" % (self.name, self.comment)


class Avatar(models.Model):
    image = models.ImageField(upload_to="avatars")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
