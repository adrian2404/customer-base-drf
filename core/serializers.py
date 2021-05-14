from rest_framework import serializers

from .models import Customer, Profession, DataSheet, Document


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'name', 'address', 'professions', 'data_sheet', 'active', 'status_string',
                  'num_professions', 'document_set')

    num_professions = serializers.SerializerMethodField()
    data_sheet = serializers.PrimaryKeyRelatedField(read_only=True)
    professions = serializers.StringRelatedField(many=True)
    document_set = serializers.StringRelatedField(many=True)

    def get_num_professions(self, obj):
        return obj.num_professions()


class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = ('id', 'description')


class DataSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataSheet
        fields = ('description', 'historical_data')


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ('dtype', 'doc_number', 'customer')