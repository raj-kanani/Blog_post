from django.urls import path, include
from .views import *
# for view set
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'blog', BlogPostGenericView)

urlpatterns = [
    path('register/', UserRegisterAPIView.as_view(), name='user-register'),
    path('login/', UserLoginAPIView.as_view(), name='user-login'),
    path('', include(router.urls)),
    path('blogs/<int:pk>/', BlogUpdateGenericView.as_view(), name='update-delete-blog'),
    path('comments/', CommentCreateAPIView.as_view(), name='create-comment')

]
