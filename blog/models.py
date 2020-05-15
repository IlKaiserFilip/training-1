from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class BlogPostModel(models.Model):
    titolo = models.CharField(max_length=100)
    contenuto = models.TextField()
    bozza = models.BooleanField()
    autore = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post", default=1)
    #data_creazione = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titolo

    def get_absolute_url(self):
        #return reverse("PostDetailView", kwargs={"pk": self.pk})
        return f"/blog/leggi-post/{self.id}"

class BlogCommentModel(models.Model):
    post = models.ForeignKey(BlogPostModel,on_delete=models.CASCADE,related_name='comments')
    autore = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment")
    contenuto = models.TextField()
    data_creazione = models.DateTimeField(auto_now_add=True)
    attivo = models.BooleanField(default=True)

