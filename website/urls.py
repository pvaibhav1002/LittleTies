from django.urls import path
from website import views

urlpatterns = [
    path('',views.home,name ='home'),
    path('login-user/', views.login_user, name ='login_user'),
    path('user/user-form/', views.user_form, name ='user_form'),
    path('user/user-dashboard/', views.user_dashboard, name ='user_dashboard'),
    path('user/rules/',views.rules,name='rules'),
    path('user/edit-profile/',views.edit_profile,name='edit_profile'),
    path('login-agency/', views.login_agency, name ='login_agency'),
    path('agency/agency-form/', views.agency_form, name ='agency_form'),
    path('agency/agency-dashboard/', views.agency_dashboard, name ='agency_dashboard'),
    path('login/', views.login, name='login'),
    path('acc_logout', views.acc_logout, name='acc_logout'),
]