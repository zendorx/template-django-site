from django.db import models

# Create your models here.


class FirstModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, default="")
    image = models.ImageField(upload_to="some_dir", default='no-img.jpeg')
    text = models.TextField(null=True)

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
            verbose_name_plural = "Values"
            verbose_name = "Value"