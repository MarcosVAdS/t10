from django.urls import path
from django.conf.urls import url
from partner import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'', views.listPartners)
router.register(r'<int:id>/', views.detailedPartner)

urlpatterns = router.urls
