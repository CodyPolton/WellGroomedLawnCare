from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Yard, Job
from .serializers import YardSerializer, JobSerializer
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


class JobsOfYard(APIView):

    def get(self,request):
        id = request.GET.get('yardid', '0')
        jobs = Job.objects.filter(yard=id)
        logger.info(jobs)
        serializer = JobSerializer(jobs, many=True)
        if jobs is None:
            return Response({"message": "No jobs " + id})

        else:
           return Response(serializer.data) 
        


