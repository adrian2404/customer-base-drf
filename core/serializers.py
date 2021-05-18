from rest_framework import serializers

from .models import Customer, Profession, DataSheet, Document


class DataSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataSheet
        fields = ('description', 'historical_data')


class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = ('id', 'description')


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ('dtype', 'doc_number')

    read_only_fields = ['customer']


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'name', 'address', 'professions', 'data_sheet', 'active', 'status_string',
                  'num_professions', 'document_set')

    num_professions = serializers.SerializerMethodField()
    data_sheet = DataSheetSerializer()
    professions = ProfessionSerializer(many=True)
    document_set = DocumentSerializer(many=True)

    def get_num_professions(self, obj):
        return obj.num_professions()

    def create(self, validated_data):
        professions = validated_data.pop('professions')
        document_set = validated_data.pop('document_set')
        data_sheet = validated_data.pop('data_sheet')
        customer = Customer.objects.create(**validated_data)

        for profession in professions:
            prof = Profession.objects.create(**profession)
            customer.professions.add(prof)

        for doc in document_set:
            Document.objects.create(
                dtype=doc['dtype'],
                doc_number=doc['doc_number'],
                customer_id=customer.id
            )
        d_sheet = DataSheet.objects.create(**data_sheet)
        customer.data_sheet = d_sheet
        customer.save()

        return customer
