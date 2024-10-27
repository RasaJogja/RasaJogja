from django.db import models
from django.contrib.auth.models import User
import uuid

class ForumEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # tambahkan baris ini
    title = models.CharField(max_length=255)  # Menambahkan judul untuk setiap entri forum
    description = models.TextField()  # Menambahkan deskripsi untuk setiap entri forum
    

class Comment(models.Model):
    forum_entry = models.ForeignKey(ForumEntry, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.forum_entry.title}"