from rest_framework.views import APIView
from django.http import JsonResponse
from ..models import Subscriber
from .serializers import SubsciberCreateSerializer, SubsciberReadSerializer


class SubsicriberApiView(APIView):
    def post(self, args ,*kwargs):
        data = self.request.data
        print(data, 111)

        serializer = SubsciberCreateSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data ,status=201, safe= False)
        
    def get(self , *args , **kwargs):
        sub = Subscriber.objects.all()
        serializer = SubsciberReadSerializer(sub ,  context={"request": self.request} , many = True)
        return JsonResponse(serializer.data , safe=False)