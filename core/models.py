from django.contrib.auth.models import User
from django.db import models
from tinymce.models import HTMLField

UNIT_CHOICES = (
    ('501','501'),
    ('502', '502'),
    ('503', '503'),
    ('504', '504'),
    ('505', '505'),
    ('506', '506'),
    ('507', '507'),
    ('508', '508'),
)

CHAPTER_CHOICES = (
    ('001','001'),
    ('002', '002'),
    ('003', '003'),
    ('004', '004'),
    ('005', '005'),
    ('006', '006'),
    ('007', '007'),
    ('008', '008'),
    ('008', '008'),
    ('009', '009'),
    ('010', '010'),
    ('011', '011'),
    ('012', '012'),
    ('013', '013'),
    ('014', '014'),
    ('015', '015'),
)
class Units(models.Model):
    name = models.CharField(max_length=10, choices=UNIT_CHOICES, default='501')
    class Meta:
        verbose_name = 'Unit'
        verbose_name_plural = 'Units'
    def __str__(self):
        return self.name
    

class PayData(models.Model):
    phonenumber = models.TextField()
    transcode = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    unit = models.ForeignKey(Units, on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Payment Detail'
        verbose_name_plural = 'Payment Details'
    def __str__(self):
        return self.phonenumber
    

class Post(models.Model):
    title = models.CharField(max_length=10)
    content = HTMLField(blank=True, null=True)
    chapter = models.CharField(max_length=10, choices=CHAPTER_CHOICES, default='001')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    unit = models.ForeignKey(Units, on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
    def __str__(self):
        return self.title