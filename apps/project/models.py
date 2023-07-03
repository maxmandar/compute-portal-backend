from django.db import models

from apps.authentication.models import CustomUser, CustomGroup
from apps.permission.models import UserRole

from django_fsm import FSMField, transition
from django_fsm import post_transition




class Project(models.Model):
    # FSM stages
    DRAFT = 'ProjectDraft'
    REVIEWED = 'ProjectReviewed'
    SUBMITTED = 'ProjectSubmitted'
    VERIFIED = 'ProjectVerified'
    APPROVED = 'ProjectApproved'
    CANCELLED = 'ProjectCancelled'
    REWORKED = 'ProjectReworked'
    PROJECT_REWORK_SUBMITTED = 'ProjectReworkSubmitted'
    PROJECT_REWORK_REVIEWED = 'ProjectReworkReviewed'

    # FSM transition choices
    TRANSITIONS = [
        (DRAFT, 'Project Draft'),
        (REVIEWED, 'Project Reviewed'),
        (SUBMITTED, 'Project Submitted'),
        (VERIFIED, 'Project Verified'),
        (APPROVED, 'Project Approved'),
        (CANCELLED, 'Project Cancelled'),
        (REWORKED, 'Project Reworked'),
        (PROJECT_REWORK_SUBMITTED, 'Project Rework Submitted'),
        (PROJECT_REWORK_REVIEWED, 'Project Rework Reviewed'),
    ]

    name = models.CharField(max_length=255)
    description_objective = models.TextField()
    fsm_state = FSMField(choices=TRANSITIONS, default=DRAFT, protected=True)

    @transition(field=fsm_state, source=[DRAFT, CANCELLED], target=REVIEWED)
    def review(self):
        pass

    @transition(field=fsm_state, source=REVIEWED, target=SUBMITTED)
    def submit(self):
        pass

    @transition(field=fsm_state, source=SUBMITTED, target=VERIFIED)
    def verify(self):
        pass

    @transition(field=fsm_state, source=VERIFIED, target=APPROVED)
    def approve(self):
        pass

    @transition(field=fsm_state, source=[REVIEWED, VERIFIED], target=CANCELLED)
    def cancel(self):
        pass

    @transition(field=fsm_state, source=[VERIFIED, PROJECT_REWORK_REVIEWED], target=REWORKED)
    def rework(self):
        pass

    @transition(field=fsm_state, source=REWORKED, target=PROJECT_REWORK_SUBMITTED)
    def resubmit(self):
        pass

    @transition(field=fsm_state, source=PROJECT_REWORK_SUBMITTED, target=PROJECT_REWORK_REVIEWED)
    def rereview(self):
        pass

    def __str__(self):
        return self.name



class ProjectAction(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    username = models.CharField(max_length=255)
    fullname = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.project.name} - {self.username} - {self.action} - {self.timestamp}'


class ProjectPermission(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    username = models.CharField(max_length=255)
    fullname = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    role = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.username} - {self.role} - {self.project.name}'
    

class UserRole(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name