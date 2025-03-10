from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

class UserDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    lastAtive = models.DateField(null=True, blank=True)
    

class Report(models.Model):
    id = models.AutoField(primary_key=True)
    create_date = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    signer = models.CharField(max_length=255)
    name = models.CharField(max_length=255,null=True)
    create_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reports",null=True)

class ProductReport(Report):   
    product = models.CharField(max_length=255)
    document = models.CharField(max_length=255)
    priority = models.CharField(max_length=255,blank=True)
    document_number = models.CharField(max_length=255)
    document_date = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    buildingType = models.CharField(max_length=255)
    buildingStruct = models.CharField(max_length=255)
    structureID = models.CharField(max_length=255)
    buildingPlace = models.CharField(max_length=255)
    contractID = models.CharField(max_length=255)
    contractDate = models.CharField(max_length=255)
    products = models.CharField(max_length=255)
    departmentCode = models.CharField(max_length=255)
    table = models.JSONField(default=dict,null=True)

class ShopDrawReport(Report):   
    sDraw = models.CharField(max_length=255)
    sDraws = models.CharField(max_length=255)
    document = models.CharField(max_length=255)
    priority = models.CharField(max_length=255,blank=True)
    document_number = models.CharField(max_length=255)
    document_date = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    buildingType = models.CharField(max_length=255)
    buildingStruct = models.CharField(max_length=255)
    structureID = models.CharField(max_length=255)
    buildingPlace = models.CharField(max_length=255)
    contractID = models.CharField(max_length=255)
    contractDate = models.CharField(max_length=255)
    departmentCode = models.CharField(max_length=255)
    reName = models.CharField(max_length=255)
    reLevel = models.CharField(max_length=255)
    reNum = models.CharField(max_length=255)
    floor = models.CharField(max_length=255)


class DocumentFormat(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    def __str__(self):
        return {'id':self.id , 'name':self.name}

class Paragraph(models.Model):
    document_format = models.ForeignKey(DocumentFormat, on_delete=models.CASCADE, related_name="paragraphs")
    alignment = models.IntegerField(default=None,null=True)  # e.g., 'left', 'right', 'center', 'justify'
    tabs = models.JSONField(default=list)  # List of tab settings: [{'position': 10, 'alignment': 'left', 'leader': '.'}]
    indentation = models.JSONField(default=dict)  # {'left': 10, 'right': 5, 'first_line': 20}
    spacing = models.JSONField(default=dict)  # {'before': 5, 'after': 10, 'line': 1.5, 'line_spacing_rule': 'exact'}

class Text(models.Model):
    paragraph = models.ForeignKey(Paragraph, on_delete=models.CASCADE, related_name="texts")
    content = models.TextField()  # The actual text
    bold = models.BooleanField(default=None ,null=True)
    italic = models.BooleanField(default=None ,null=True)
    underline = models.IntegerField(default=0, null=True)  # 0 for no underline, other integers for different styles
    font = models.CharField(max_length=100,null=True)  # Font name
    size = models.FloatField(null=True)  # Font size
    color = models.CharField(max_length=7,null=True)

class Section(models.Model):
    top = models.IntegerField(default=0, null=True)
    left = models.IntegerField(default=0, null=True)
    right = models.IntegerField(default=0, null=True)
    bottom = models.IntegerField(default=0, null=True)

class Image(models.Model):
    name = models.CharField(max_length=100)
    image_data = models.BinaryField()