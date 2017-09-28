from django.db import models
from django.utils import timezone
# Create your models here.
class Post(models.Model): #this line defines our model
# class is a special keyword that indicates we are defining an object
# Post is the name of the model , should be always uppercase
# models.Models means that the Post is a Django Model,
#so Django knows that it should be saved in the database.
    author = models.ForeignKey('auth.User')
    #models.ForeignKey - this is a link to another model
    title = models.CharField(max_length=200)
    #models.Charfield - this is hwo you define text with a limited no of char
    text = models.TextField()
    #models.TextField - long text without a limit
    created_date = models.DateTimeField(
            default=timezone.now)
    #models.DateTimeField - this is date and time
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    #In this scenario, when we call __str__() we will get a text (string)
    # with a Post title.
