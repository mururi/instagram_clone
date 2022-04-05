from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length = 100)
    profile_photo = models.ImageField(upload_to = 'profile/')
    bio = models.TextField()

    def __str__(self):
        return self.name

class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    image_name = models.CharField(max_length = 60)
    image_caption = models.TextField()
    profile = models.ForeignKey(Profile, on_delete = models.CASCADE)
    likes = models.IntegerField()
    pub_date = models.DateTimeField(auto_now_add = True)

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return self.image_name

    @classmethod
    def get_images(cls):
        images = cls.objects.all()
        return images

class Comment(models.Model):
    content = models.TextField()
    image = models.ForeignKey(Image, on_delete = models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.content