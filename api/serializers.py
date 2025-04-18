from rest_framework import serializers
from .models import Report , DocumentFormat,ProductReport , Paragraph, Text , Section,Image ,ShopDrawReport



class ReportSerializer(serializers.ModelSerializer):
    create_by = serializers.CharField(source='create_by.username', read_only=True)
    class Meta:
        model = Report
        fields = ['id', 'create_date', 'type', 'signer','name','create_by']  # Specify the fields you want to include
        read_only_fields = ['create_by']


class ProductReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductReport
        fields = ReportSerializer.Meta.fields + [
            'product', 'document', 'priority', 'document_number', 'document_date', 
            'company', 'buildingType', 'buildingStruct', 'structureID', 
            'buildingPlace', 'contractID', 'contractDate', 'products', 'departmentCode' , 'table'
        ]
class ShopDrawReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopDrawReport
        fields = ReportSerializer.Meta.fields + ["sDraw", "sDraws", "document", "priority", "document_number",  
          "document_date", "company", "buildingType", "buildingStruct",  
          "structureID", "buildingPlace", "contractID", "contractDate",  
          "departmentCode", "reName", "reLevel", "reNum", "floor"]
        
class TextSerializer(serializers.ModelSerializer):
    class Meta:
        model = Text
        fields = ['id', 'content', 'bold', 'italic', 'underline', 'font', 'size', 'color']


class ParagraphSerializer(serializers.ModelSerializer):
    texts = TextSerializer(many=True, read_only=True)  # Include related Texts

    class Meta:
        model = Paragraph
        fields = ['id', 'alignment', 'tabs', 'indentation', 'spacing', 'texts']


class DocumentFormatSerializer(serializers.ModelSerializer):
    paragraphs = ParagraphSerializer(many=True, read_only=True)  # Include related Paragraphs

    class Meta:
        model = DocumentFormat
        fields = ['id', 'name', 'paragraphs']

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ['id', 'top','left','right','bottom']

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'name','image_data']
