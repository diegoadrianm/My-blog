from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, null=True)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Post(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True, db_index=True)
    image = models.CharField(max_length=50)
    author = models.ForeignKey("Author", on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    excerpt = models.CharField(max_length=180)
    content = models.TextField(validators=[MinLengthValidator(10)])
    tag = models.ManyToManyField("Tag", related_query_name="tags")

    def __str__(self):
        return f"{self.title}"


class Tag(models.Model):

    caption = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    def __str__(self):
        return str(self.caption)
