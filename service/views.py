from django_filters import rest_framework as filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from service.crud import CDRCrud
from service.serializers import CDRListSerializer, CDRSerializer


class CDRViewSet(ModelViewSet):
    queryset = CDRCrud.get_all()
    permission_classes = [IsAuthenticated, ]
    http_method_names = ['get', 'post', 'delete']
    filter_backends = (filters.DjangoFilterBackend, )
    filterset_fields = ('created', 'calling_number', 'called_number', 'status')

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    def get_serializer_class(self):
        if self.action == 'list':
            return CDRListSerializer
        return CDRSerializer
