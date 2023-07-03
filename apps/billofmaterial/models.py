from django.db import models
from django_fsm import FSMField, transition
from apps.infrastructureinitiationdocument.models import IidProject



    


# Create your models here.
class BillOfMaterial(models.Model):

    STATUS_REQUESTED = 'requested'
    STATUS_REVIEWED = 'reviewed'
    STATUS_REVISION = 'revision'
    STATUS_APPROVED = 'approved'
    STATUS_REJECTED = 'rejected'

    STATUS_CHOICES = (
        (STATUS_REQUESTED, 'Requested'),
        (STATUS_REVIEWED, 'Reviewed'),
        (STATUS_REVISION, 'Revision'),
        (STATUS_APPROVED, 'Approved'),
        (STATUS_REJECTED, 'Rejected'),
    )


    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    project = models.ForeignKey(IidProject, on_delete=models.CASCADE, related_name='boms')
    status = FSMField(choices=STATUS_CHOICES, default=STATUS_REQUESTED)

    # State transitions
    @transition(field=status, source=STATUS_REQUESTED, target=STATUS_REVIEWED)
    def submit_for_review(self):
        pass

    @transition(field=status, source=STATUS_REVIEWED, target=STATUS_APPROVED)
    def approve(self):
        pass

    @transition(field=status, source=STATUS_REVIEWED, target=STATUS_REVISION)
    def request_revision(self):
        pass

    @transition(field=status, source=STATUS_REVISION, target=STATUS_REQUESTED)
    def resubmit_for_review(self):
        pass


    def __str__(self):
        return f"{self.id} - {self.name}"