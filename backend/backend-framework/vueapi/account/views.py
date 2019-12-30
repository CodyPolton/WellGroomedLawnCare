from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Yard
from .serializers import YardSerializer
import logging

logger = logging.getLogger(__name__)

# Create your views here.

class YardsOfAccount(APIView):

    def get(self, request):
        id = request.GET.get('id', '0')
        yards = Yard.objects.filter(account=id)
        logger.error(yards)
        serializer = YardSerializer(yards, many=True)
        if yards is None:
            return Response({"message": "Hello, world! " + id})
        
        else:
           return Response(serializer.data) 
        


