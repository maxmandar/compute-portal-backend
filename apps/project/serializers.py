from rest_framework import serializers
from django.shortcuts import get_object_or_404
from django.db import transaction

from .models import *
from apps.permission.models import UserRole
from apps.authentication.serializers import CustomUserSerializer


class ProjectCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['name', 'description_objective', 'fsm_state']

    @transaction.atomic
    def create(self, validated_data):
        project = Project.objects.create(**validated_data)

        # Getting the requestor role, replace 'Requestor' with the actual role name
        requestor_role = 'Requestor'
        
        # Create ProjectAction and ProjectRole instances
        ProjectAction.objects.create(
            project=project, 
            username=self.context['request'].user.username,
            fullname=self.context['request'].user.fullname,
            email=self.context['request'].user.email,
            action=project.fsm_state
        )
        ProjectPermission.objects.create(
            project=project, 
            username=self.context['request'].user.username,
            fullname=self.context['request'].user.fullname,
            email=self.context['request'].user.email,
            role=requestor_role
        )

        return project


class ProjectUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['name', 'description_objective', 'fsm_state']

    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description_objective = validated_data.get('description_objective', instance.description_objective)
        instance.fsm_state = validated_data.get('fsm_state', instance.fsm_state)
        instance.save()

        if instance.fsm_state:
            ProjectAction.objects.create(
                project=instance, 
                username=self.context['request'].user.username,
                fullname=self.context['request'].user.fullname,
                email=self.context['request'].user.email,
                action=instance.fsm_state
            )

        return instance



class ProjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class ProjectRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['name', 'description_objective', 'fsm_state']






class ProjectActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectAction
        fields = ['project', 'action', 'user']


class ProjectPermissionSerializer(serializers.ModelSerializer):
    project = ProjectListSerializer()

    class Meta:
        model = ProjectPermission
        fields = ['id', 'project', 'username', 'fullname', 'email', 'role']




class ProjectCreatePermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectPermission
        fields = ['username', 'fullname', 'email', 'role']

    def create(self, validated_data):
        # Get the project ID from the context and use it to fetch the Project object
        project_id = self.context['project_id']
        project = Project.objects.get(id=project_id)
        # Add the Project object to the validated data
        validated_data['project'] = project
        return super().create(validated_data)


class UserRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRole
        fields = ['id', 'name', 'description']

