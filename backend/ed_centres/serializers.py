from rest_framework import serializers

from .models import CenterInfo, CenterTask, Discipline, EducationalMaterial, ManagerProfile, StudyPlan, TeachingStaff,\
    EducationalContact


class EducationalContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationalContact
        fields = ('id', 'contact',)


class CenterInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CenterInfo
        fields = ('id', 'title', 'description', 'thesis', 'image',)


class CenterTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = CenterTask
        fields = ('id', 'text',)


class ManagerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManagerProfile
        fields = ('id', 'full_name', 'text', 'image',)


class DisciplineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discipline
        fields = ('id', 'name', 'content',)


class StudyPlanSerializer(serializers.ModelSerializer):
    disciplines = DisciplineSerializer(many=True)

    class Meta:
        model = StudyPlan
        fields = ('id', 'title', 'disciplines')


class TeachingStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeachingStaff
        fields = ('id', 'full_name', 'position',)


class EducationalMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationalMaterial
        fields = ('id', 'title', 'url',)
