from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import *
from .serializers import *
from django.db.models import Q

from rest_framework.permissions import IsAuthenticated




class ProjectCreateAPIView(generics.CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectCreateSerializer


class ProjectRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectRetrieveSerializer

class ProjectUpdateAPIView(generics.UpdateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectUpdateSerializer

class ProjectListAPIView(generics.ListAPIView):
    serializer_class = ProjectListSerializer

    def get_queryset(self):
            username = self.request.user.username
            return Project.objects.filter(Q(projectpermission__username=username)).distinct()
    



class ProjectDestroyAPIView(generics.DestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectCreateSerializer



class ProjectActionCreateView(generics.CreateAPIView):
    queryset = ProjectAction.objects.all()
    serializer_class = ProjectActionSerializer

class ProjectActionRetrieveView(generics.RetrieveAPIView):
    queryset = ProjectAction.objects.all()
    serializer_class = ProjectActionSerializer

class ProjectActionUpdateView(generics.UpdateAPIView):
    queryset = ProjectAction.objects.all()
    serializer_class = ProjectActionSerializer

class ProjectActionDestroyView(generics.DestroyAPIView):
    queryset = ProjectAction.objects.all()
    serializer_class = ProjectActionSerializer



class ProjectPermissionListAPIView(generics.ListAPIView):
    queryset = ProjectPermission.objects.all()
    serializer_class = ProjectPermissionSerializer

    def get_queryset(self):
        """
        This view should return a list of all the permissions
        for the project as determined by the project portion of the URL.
        """
        project_id = self.kwargs['pk']
        return ProjectPermission.objects.filter(project__id=project_id)
    


class ProjectPermissionCreateAPIView(generics.CreateAPIView):
    queryset = ProjectPermission.objects.all()
    serializer_class = ProjectCreatePermissionSerializer

    def create(self, request, *args, **kwargs):
        # Add the project ID to the serializer context
        self.serializer_class.context = {'project_id': self.kwargs['pk']}
        return super().create(request, *args, **kwargs)

class ProjectPermissionUpdateAPIView(generics.UpdateAPIView):
    queryset = ProjectPermission.objects.all()
    serializer_class = ProjectPermissionSerializer

class ProjectPermissionDestroyAPIView(generics.DestroyAPIView):
    queryset = ProjectPermission.objects.all()
    serializer_class = ProjectPermissionSerializer



class UserRoleListAPIView(generics.ListAPIView):
    queryset = UserRole.objects.all()
    serializer_class = UserRoleSerializer

class UserRoleCreateAPIView(generics.CreateAPIView):
    queryset = UserRole.objects.all()
    serializer_class = UserRoleSerializer

class UserRoleRetrieveAPIView(generics.RetrieveAPIView):
    queryset = UserRole.objects.all()
    serializer_class = UserRoleSerializer

class UserRoleUpdateAPIView(generics.UpdateAPIView):
    queryset = UserRole.objects.all()
    serializer_class = UserRoleSerializer

class UserRoleDestroyAPIView(generics.DestroyAPIView):
    queryset = UserRole.objects.all()
    serializer_class = UserRoleSerializer

# def generate_pdf(request, pk):
#     # Get the project object
#     project = Project.objects.get(pk=pk)

#     # Create a file-like buffer to receive PDF data.
#     buffer = BytesIO()

#     # Create the PDF object, using the BytesIO object as its "file."
#     p = canvas.Canvas(buffer)

#     # Draw things on the PDF. Here's where the PDF generation happens.
#     # See the ReportLab documentation for the full list of functionality.
#     p.drawString(100, 800, f"Project Name: {project.name}")
#     p.drawString(100, 780, f"Project Manager: {', '.join(str(manager) for manager in project.project_managers.all())}")
#     p.drawString(100, 760, f"Requestor: {project.requestor}")
#     p.drawString(100, 740, f"Verifier: {project.verifier}")
#     p.drawString(100, 720, f"Approver: {project.approver}")

#     # Close the PDF object cleanly, and we're done.
#     p.showPage()
#     p.save()

#     # FileResponse sets the Content-Disposition header so that browsers
#     # present the option to save the file.
#     buffer.seek(0)
#     return HttpResponse(buffer, content_type='application/pdf')

# from django.http import HttpResponse
# from reportlab.pdfgen import canvas
# from django.template.loader import get_template

# from django.template import Context
# from reportlab.pdfgen import canvas
# from io import BytesIO


# from reportlab.lib.pagesizes import letter, landscape
# from reportlab.lib import colors
# from reportlab.lib.units import inch
# from reportlab.platypus import SimpleDocTemplate, Table, TableStyle


# def generate_pdf(request, pk):
#     project = Project.objects.get(pk=pk)
#     context = {'project': project}

#     # Create a file-like buffer to receive PDF data
#     buffer = BytesIO()

#     # Create the PDF object, using the BytesIO object as its "file."
#     doc = SimpleDocTemplate(buffer, pagesize=landscape(letter))

#     # Our container for 'Flowable' objects
#     elements = []

#     # Define the style of the table
#     style = TableStyle([
#         ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
#         ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
#         ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
#         ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
#         ('FONTSIZE', (0, 0), (-1, 0), 14),
#         ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
#         ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
#     ])

#     # Create table
#     data = [
#         ['Project Name:', project.name],
#         ['Requestor:', project.requestor.fullname],
#         ['Verfier:', project.verifier.fullname ],
#         ['Approver:', project.approver.fullname],
#         # ['Project Managers:', ' '.join([pm.fullname for pm in project.project_managers.all()])],
#         ['Status:', project.fsm_state],
#     ]
#     table = Table(data)
#     table.setStyle(style)
#     elements.append(table)

#     # Add more elements to the document...

#     # Write the PDF to the buffer
#     doc.build(elements)

#     # Get the value of the BytesIO buffer and write it to the response.
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'filename="project.pdf"'
#     response.write(buffer.getvalue())
#     buffer.close()

#     return response