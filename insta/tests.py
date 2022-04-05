from django.test import TestCase
from .models import Profile, Image, Comment
from django.contrib.auth.models import User

class ProfileTestClass(TestCase):
    '''
    Test class to test the behaviour of the Profile model class
    '''

    def setUp(self):
        '''
        Set up method to run before each test case
        '''
       
        # Creating a new user
        self.new_user = User(username = 'Doe', password = 'pass', email = 'johndoe@company.com')
        self.new_user.save()

        # Creating a new profile
        self.new_profile = Profile(id = 1, user = self.new_user, bio = 'Test short bio')
        self.new_profile.save()

    def test_instance(self):
        '''
        Method to test if the new_profile object is an instance of the Profile model
        '''

        self.assertTrue(self.new_profile, Profile)

    def test_delete_method(self):
        Profile.delete_profile(self.new_profile.id)
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) == 0)

    def test_get_profiles(self):
        profiles = Profile.get_profiles()
        self.assertTrue(len(profiles > 0))

class ImageTestClass(TestCase):
    '''
    Test class to test the behavior of the Image model class
    '''

    def setUp(self):
        '''
        set up method to run before each test case
        '''

        # Creating a new user
        self.new_user = User(username = 'Doe', password = 'pass', email = 'johndoe@company.com')
        self.new_user.save()

        # Creating a new profile
        self.new_profile = Profile(id = 1, user = self.new_user, bio = 'Test short bio')
        self.new_profile.save()

        # Creating a new image
        self.new_image = Image(id = 1, image_name = 'Image Name', image_caption = 'Test Caption', profile = self.new_profile)
        self.new_image.save()

    def test_instance(self):
        '''
        test_instance method to test if the new_image object is an instance of the Image model
        '''

        self.assertTrue(isinstance(self.new_image, Image))

    def test_delete_method(self):
        Image.delete_image(self.new_image.id)
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)