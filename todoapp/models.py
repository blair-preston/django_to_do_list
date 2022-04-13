from django.db import models

class User(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name

class Category(models.Model):
    title = models.CharField(max_length=300)
    color = models.CharField(max_length=100)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
     verbose_name_plural = 'Categories'

class Event(models.Model):
    label = models.CharField(max_length=300)
    description = models.CharField(max_length=800, blank=True, null=True) #optional (might need default='')
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    duration = models.DurationField()
    location = models.CharField(max_length=500)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.label

class Daily(models.Model):
    label = models.CharField(max_length=300)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True) #optional (might need default='')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.label

    class Meta:
     verbose_name_plural = 'Dailies'

class Priority(models.Model):
    label = models.CharField(max_length=300)

    def __str__(self):
        return self.label

    class Meta:
     verbose_name_plural = 'Priorities'

class Status(models.Model):
    label = models.CharField(max_length=300)

    def __str__(self):
        return self.label

    class Meta:
     verbose_name_plural = 'Statuses'

class Todo(models.Model):
    label = models.CharField(max_length=300)
    description = models.CharField(max_length=800, blank=True, null=True) #optional (might need default='')
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField('date created')
    priority_id = models.ForeignKey(Priority, on_delete=models.CASCADE)
    due_by = models.DateTimeField(blank=True, null=True)
    status_id = models.ForeignKey(Status, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.label