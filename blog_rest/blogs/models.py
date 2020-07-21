from django.db import models


class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-
    updating ``created`` and ``modified`` fields.
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Blog(TimeStampedModel):
    title = models.CharField(max_length=40, default=None)
    text = models.TextField(max_length=200)
    owner = models.ForeignKey('auth.User', related_name='blogs',  on_delete=models.CASCADE)

    class Meta:
        ordering = ('-created',)


class Comment(TimeStampedModel):
    text = models.TextField(max_length=200)
    owner = models.ForeignKey('auth.User', related_name='comments', on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, related_name='comments',  on_delete=models.CASCADE)

    class Meta:
        ordering = ('-created',)