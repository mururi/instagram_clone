from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name = 'profile')
    profile_photo = models.ImageField(upload_to = 'profile/')
    bio = models.TextField()

    def save_profile(self):
        self.save()

    @classmethod
    def delete_profile(cls, id):
        '''
        Method to delete a Profile object
        '''
        cls.objects.filter(id = id).delete()

    @classmethod
    def get_profiles(cls):
        '''
        Method to get all profile objects
        '''
        profiles = cls.objects.all()
        return profiles

    def __str__(self):
        return self.user.username

class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    image_name = models.CharField(max_length = 60)
    image_caption = models.TextField()
    profile = models.ForeignKey(Profile, on_delete = models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add = True)

    class Meta:
        ordering = ['-pub_date']
    
    def save_image(self):
        self.save()

    @classmethod
    def delete_image(cls, id):
        '''
        Method to delete an Image object
        '''

        cls.objects.filter(id = id).delete()

    @classmethod
    def get_images(cls):
        '''
        method to get all Image objects
        '''
        images = cls.objects.all()
        return images

    @classmethod
    def update_image(cls, id):
        pass

    @classmethod
    def search_image(cls, search_term):
        images = cls.objects.filter(image_caption__icontains = search_term)
        return images

    def __str__(self):
        return self.image_name

    

class Comment(models.Model):
    content = models.TextField()
    image = models.ForeignKey(Image, on_delete = models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.content

class Like(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    image = models.ForeignKey(Image, on_delete = models.CASCADE)
    like_date = models.DateTimeField(auto_now_add = True)