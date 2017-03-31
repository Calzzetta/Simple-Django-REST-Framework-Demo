from rest_framework import mixins
from rest_framework import generics
from .models import Employee
from .serializers import EmployeeSerializer


class EmployeeList(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class EmployeeDetail(mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin,
                     generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'email'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
