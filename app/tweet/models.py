from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.


class Tweet(models.Model):
    author = models.ForeignKey(User, related_name='user',
                               on_delete=models.CASCADE)
    parent_id = models.ForeignKey(
        "self", on_delete=models.CASCADE, related_name='parenttweet', null=True, blank=True)
    sub_parent_id = models.ForeignKey(
        "self", on_delete=models.CASCADE, related_name='subparenttweet', null=True, blank=True)
    tweet_message = models.TextField(blank=True, null=True)
    retweet_id = models.ForeignKey(
        "self", on_delete=models.CASCADE, related_name='retweetid', null=True, blank=True)
    liked = models.ManyToManyField(User, blank=True)
    share_count = models.IntegerField(default=0)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ("Tweet")
        verbose_name_plural = ("Tweets")

    @property
    def like_count(self):
        return self.liked.count()
