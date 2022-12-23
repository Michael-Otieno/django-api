from django.urls import path
from .views import RegisterView,LoginView,UserView,LogoutView,LandOwnerInformationView,LandOwnerDetailInfoView,LandInfoDetailView,LandInfoView
from .import views 

urlpatterns = [
    path('',views.getRoutes),
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('user/', UserView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('land-information/', LandOwnerInformationView.as_view()),
    path('land-information/<int:pk>/', LandOwnerDetailInfoView.as_view()),
    path('land-detail/', LandInfoView.as_view()),
    path('land-detail/<int:pk>/', LandInfoDetailView.as_view()),

]
