from django.db import models

class User(models.Model):
    username = models.CharField(max_length=75, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='pictures')

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    bio = models.TextField(blank=True)
    website = models.URLField(blank=True)
    location = models.CharField(max_length=75, blank=True)

    def __str__(self):
        return self.user.username
    

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    caption = models.TextField()
    image_or_video = models.FileField(upload_to='posts')
    publication_date = models.DateTimeField(auto_now_add=True)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)

class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    date_followed = models.DateTimeField(auto_now_add=True)