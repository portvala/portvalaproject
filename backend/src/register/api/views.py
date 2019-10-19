from rest_framework.generics import ListAPIView,RetrieveAPIView

from register.models import register as Reg
from .serializers import RegisterSerializer

class registerListView(ListAPIView):
    queryset = Reg.objects.all()
    serializer_class = RegisterSerializer

class registerDetailView(RetrieveAPIView):
    queryset = Reg.objects.all()
    serializer_class = RegisterSerializer