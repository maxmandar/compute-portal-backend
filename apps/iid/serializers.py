from rest_framework import serializers
from .models import Segment
from .models import SubSegment
from .models import Iid

from apps.employee.models import Employee

from apps.employee.serializers import EmployeeSerializer

from drf_writable_nested.serializers import WritableNestedModelSerializer

class SegmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Segment
        fields = ('id', 'name')


class SubSegmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubSegment
        fields = ('id', 'name')



# Here, we define the IidSerializer and inherit from WritableNestedModelSerializer
# to enable support for writable nested fields
class IidSerializer(WritableNestedModelSerializer):
    steering_committee_members = EmployeeSerializer(many=True)
    project_managers = EmployeeSerializer(many=True)
    security_architect = EmployeeSerializer()
    lead_technical_delivery_manager = EmployeeSerializer()
    application_l3 = EmployeeSerializer()
    segment = SegmentSerializer()
    subsegment = SubSegmentSerializer()
    tno_head = EmployeeSerializer()
    requestor = EmployeeSerializer()
    watchers = EmployeeSerializer(many=True)

    class Meta:
        model = Iid
        exclude = ['fsm_state']
        # fields = ('id', 'project_name', 'steering_committee_members','requestor', 'watchers','security_architect',
        #           'tno_head', 'project_managers','application_l3','lead_technical_delivery_manager','segment',
        #           'subsegment')
   
    # def is_valid(self, raise_exception=False):
    #     if self.partial:  
    #         return super().is_valid(raise_exception=raise_exception)
    #     else:  
    #         return True

class IidUpdateSerializer(WritableNestedModelSerializer):
    watchers = EmployeeSerializer(many=True)

    class Meta:
        model = Iid
        exclude = ['fsm_state']