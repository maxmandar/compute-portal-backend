# Create your views here.
from rest_framework import generics
from .models import Segment,SubSegment,Iid
from apps.employee.models import Employee
from .serializers import SegmentSerializer,SubSegmentSerializer, IidSerializer,IidUpdateSerializer

from rest_framework.response import Response
from .models import Iid

# from fsm_admin.mixins import FSMTransitionMixin
from django_fsm import TransitionNotAllowed
from rest_framework import status



class SegmentListCreateView(generics.ListCreateAPIView):
    queryset = Segment.objects.all()
    serializer_class = SegmentSerializer

class SegmentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Segment.objects.all()
    serializer_class = SegmentSerializer


class SubSegmentListCreateView(generics.ListCreateAPIView):
    queryset = SubSegment.objects.all()
    serializer_class = SubSegmentSerializer

class SubSegmentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubSegment.objects.all()
    serializer_class = SubSegmentSerializer


class IidListCreateView(generics.ListCreateAPIView):
    queryset = Iid.objects.all()
    serializer_class = IidSerializer

class IidRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Iid.objects.all()
    serializer_class = IidUpdateSerializer

    def update(self, request, *args, **kwargs):
        print("Mandar")
        print(kwargs)
        partial = kwargs.pop('partial', False)
        print(partial)
        instance = self.get_object()
        print(instance)
        print(request.data)
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        print(serializer.is_valid())
        print(serializer)
        print(serializer.is_valid())
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    # def get_serializer(self, *args, **kwargs):
    #     kwargs['exclude_fields'] = ['fsm_state']
    #     return super().get_serializer(*args, **kwargs)

    # def update(self, request, *args, **kwargs):
    #     partial = kwargs.pop('partial', False)
    #     instance = self.get_object()

    #     serializer = self.get_serializer(instance, data=request.data, partial=partial)
    #     serializer.is_valid(raise_exception=True)
    #     instance = serializer.save()

    #     # perform FSM state transition if the payload contains an 'fsm_action' field
    #     fsm_action = request.data.get('fsm_action')
    #     if fsm_action:
    #         try:
    #             getattr(instance, fsm_action)()
    #         except TransitionNotAllowed:
    #             return Response({"detail": "Invalid state transition."}, status=status.HTTP_400_BAD_REQUEST)

    #     serializer = self.get_serializer(instance)
    #     return Response(serializer.data)


