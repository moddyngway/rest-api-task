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
            a, created = Contact.objects.get_or_create(course=course, **contact)
            course.contacts.add(a)
        for branch in branches:
            a, created = Branch.objects.get_or_create(course=course, **branch)
            course.branches.add(a)
        return course
