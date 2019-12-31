from rest_framework import routers
from account.viewsets import AccountViewSet, YardViewSet, JobTypeViewSet, JobViewSet
from account import views

router = routers.DefaultRouter()
router.register(r'account', AccountViewSet)
router.register(r'yard', YardViewSet) 
router.register(r'jobtype', JobTypeViewSet)
router.register(r'job', JobViewSet)