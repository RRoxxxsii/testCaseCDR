from rest_framework.routers import DefaultRouter

from service import views

urlpatterns = [

]

router = DefaultRouter()
router.register(r'cdr', views.CDRViewSet, basename='cdr')

urlpatterns += router.urls
