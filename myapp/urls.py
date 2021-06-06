from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('trainspot', views.Train_Spot, name='trainspot'),
    path('schedule', views.Schedule, name='schedule'),
    path('booktrain', views.Book_Train, name='booktrain'),
    path('cancel', views.Cancel, name='cancel'),
    path('reschedule', views.Reschedule, name='reschedule'),
    path('login', views.user_Login, name='login'),
    path('logout', views.user_Logout, name='logout'),
    path('status', views.Status, name='status'),
    path('signup', views.user_Regi, name='signup'),
    path('ticket', views.BuyTicket, name='ticket'),
  ]