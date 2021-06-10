from rest_framework import serializers
from .models import Course, Category, Contact, Branch


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('title', 'description', 'logo', 'category', 'branches', 'contacts')

    branches = BranchSerializer(many=True)
    contacts = ContactSerializer(many=True)
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all()
    )

    def create(self, validated_data):
        contacts = validated_data.pop('contacts')
        branches = validated_data.pop('branches')
        course = Course.objects.create(**validated_data)

        for contact in contacts:
            Contact.objects.create(course=course, **contact)
        for branch in branches:
            Branch.objects.create(course=course, **branch)
        return course
