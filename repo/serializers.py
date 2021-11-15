from rest_framework import serializers
from .models import Document, Questionnaire


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Document
        fields = '__all__'
        read_only_fields = ('created_ts', 'updated_ts')


class QuestionnaireSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Questionnaire
        fields = '__all__'
        read_only_fields = ('created_ts', 'updated_ts')
