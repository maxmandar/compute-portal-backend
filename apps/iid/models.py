from django.db import models
from auditlog.models import AuditlogHistoryField
from auditlog.registry import auditlog

from apps.employee.models import Employee

from django_fsm import FSMField, transition


class Segment(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    history = AuditlogHistoryField()

    def __str__(self):
        return self.name
    
auditlog.register(Segment)


class SubSegment(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    history = AuditlogHistoryField()

    def __str__(self):
        return self.name

auditlog.register(SubSegment)





class Iid(models.Model):

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
    segment = models.ForeignKey(Segment, on_delete=models.PROTECT)
    subsegment = models.ForeignKey(SubSegment, on_delete=models.PROTECT)
    project_name = models.CharField(max_length=100)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    objective = models.TextField()
    steering_committee_members = models.ManyToManyField(Employee, related_name='iid_steering_committee_members')
    tno_head = models.ForeignKey(Employee, on_delete=models.PROTECT, related_name='iid_tno_head')
    project_managers = models.ManyToManyField(Employee, related_name='iid_project_managers')
    security_architect = models.ForeignKey(Employee, on_delete=models.PROTECT, related_name='iid_security_architect')
    lead_technical_delivery_manager = models.ForeignKey(Employee, on_delete=models.PROTECT, related_name='iid_lead_tech_delivery_mgr')
    application_l3 = models.ForeignKey(Employee, on_delete=models.PROTECT, related_name='iid_application_l3')
    tagcc_date = models.DateField()
    itc_date = models.DateField()
    go_live_date = models.DateField()
    requestor = models.ForeignKey(Employee, on_delete=models.PROTECT, related_name='iid_requestor',null=True)
    watchers = models.ManyToManyField(Employee, related_name='iid_watchers')
    reviewer = models.ForeignKey(Employee, on_delete=models.PROTECT, related_name='iid_reviewer', null=True)
    verifier = models.ForeignKey(Employee, on_delete=models.PROTECT, related_name='iid_verifier', null=True)
    approver = models.ForeignKey(Employee, on_delete=models.PROTECT, related_name='iid_approver', null=True)


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
        return self.project_name

