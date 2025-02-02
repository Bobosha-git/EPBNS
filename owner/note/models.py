from django.db import models
import uuid

class Page(models.Model):
    title = models.CharField(max_length=200, blank=True)
    content = models.TextField(blank=True)
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title if self.title else "Untiled Page"
