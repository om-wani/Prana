# from django.urls import path
# from . import views

# # Create your urls here

# urlpatterns = [
#     path('', views.home, name='home'),
#     path('signup/', views.signup, name='signup'),
#     path('signin/', views.signin, name='signin'),
#     path('signout/', views.signout, name='signout'),
#     path('dashboard/', views.dashboard, name='dashboard'),
# ]

# urls.py
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    # path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path("logout/", views.logout_view, name="logout"),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('dashboard/doctor/', views.doctor_dashboard, name='doctor_dashboard'),
    path('dashboard/patient/', views.patient_dashboard, name='patient_dashboard'),
    path('dashboard/admin/', views.admin_dashboard, name='admin_dashboard'),

]