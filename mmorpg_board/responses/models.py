from django.db import models


class Response(models.Model):
    ad = models.ForeignKey('ads.Ad', on_delete=models.CASCADE)
    author = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_accepted = models.BooleanField(default=False)

    def __str__(self):
        return f"Response to {self.ad.title}"