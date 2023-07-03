from django.db import models
from django_fsm import FSMField, transition
from apps.employee.models import Employee
from django.contrib.auth.models import User
# from authentication.models import CustomUser
from django.conf import settings


class IidProject(models.Model):
    # FSM stages
    DRAFT = 'Draft'
    REVIEW = 'Review'
    SUBMITTED = 'Submitted'
    VERIFIED = 'Verified'
    APPROVED = 'Approved'
    CANCELLED = 'Cancelled'
    REWORK = 'Rework'
    RE_SUBMITTED = 'Resubmitted'
    RE_REVIEWED = 'Rereviewed'

    # FSM transition choices
    TRANSITIONS = [
        (DRAFT, 'Draft'),
        (REVIEW, 'Review'),
        (SUBMITTED, 'Submitted'),
        (VERIFIED, 'Verified'),
        (APPROVED, 'Approved'),
        (CANCELLED, 'Cancelled'),
        (REWORK, 'Rework'),
        (RE_SUBMITTED, 'Resubmitted'),
        (RE_REVIEWED, 'Rereviewed')
    ]

    name = models.CharField(max_length=255)
    description_objective = models.TextField()

    fsm_state = FSMField(choices=TRANSITIONS, default=DRAFT, protected=True)

    
    @transition(field=fsm_state, source=[DRAFT, CANCELLED], target=REVIEW)
    def review(self):
        pass

    @transition(field=fsm_state, source=REVIEW, target=SUBMITTED)
    def submit(self):
        pass

    @transition(field=fsm_state, source=SUBMITTED, target=VERIFIED)
    def verify(self):
        pass

    @transition(field=fsm_state, source=VERIFIED, target=APPROVED)
    def approve(self):
        pass

    @transition(field=fsm_state, source=[REVIEW, VERIFIED], target=CANCELLED)
    def cancel(self):
        pass

    @transition(field=fsm_state, source=[VERIFIED, RE_REVIEWED], target=REWORK)
    def rework(self):
        pass

    @transition(field=fsm_state, source=REWORK, target=RE_SUBMITTED)
    def resubmit(self):
        pass

    @transition(field=fsm_state, source=RE_SUBMITTED, target=RE_REVIEWED)
    def rereview(self):
        pass
    

    def __str__(self):
        return self.name
    


class IidRequestor(models.Model):
    iid_project = models.ForeignKey(IidProject, on_delete=models.CASCADE, related_name='requestors')
    requestor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='requestor_iid_projects')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.iid_project} - {self.requestor}'