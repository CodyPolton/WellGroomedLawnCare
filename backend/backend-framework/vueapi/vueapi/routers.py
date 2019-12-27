from rest_framework import routers
from account.viewsets import AccountViewSet

router = routers.DefaultRouter()
router.register(r'account', AccountViewSet)