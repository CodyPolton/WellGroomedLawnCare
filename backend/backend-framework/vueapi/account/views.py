from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Yard, Job, JobExpense
from .serializers import YardSerializer, JobSerializer, JobExpenseSerializer
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

class ExpensesOfJob(APIView):

    def get(self,request):
        id = request.GET.get('jobid', '0')
        expenses = JobExpense.objects.filter(job=id)
        logger.info(expenses)
        serializer = JobExpenseSerializer(expenses, many=True)
        if expenses is None:
            return Response({"message": "No expenses " + id})

        else:
           return Response(serializer.data) 

class YardMowed(APIView):

    def get(self,request):
        code = request.GET.get('code', '0')
        mow_price = request.GET.get('mow_price', '0')
        logger.info("mow price is" + mow_price)
        if code == 0 or mow_price == 0:
            return Response({"message": "Need both code and mow_price to process "})

        else:
           return Response({"message": "Successfully mowed"}) 
        


