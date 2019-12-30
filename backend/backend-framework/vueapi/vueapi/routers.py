from rest_framework import routers
from account.viewsets import AccountViewSet, YardViewSet
from account import views

router = routers.DefaultRouter()
router.register(r'account', AccountViewSet)
router.register(r'yard', YardViewSet) 