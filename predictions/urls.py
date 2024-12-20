from django.urls import path
from . import views
from django.urls import include
from .views import authView

urlpatterns = [
    path('', views.landing, name='landing'),
    # path('logout/', views.logout_view, name='logout'),
    path('about/',views.about,name='about'),
    #path('about/newletter',views.about,name='about'),
    path('architecture/',views.architecture,name='architecture'),
    path('newsletter/submit/', views.newsletter_submit, name='newsletter_submit'),
    #path('newsletter/', views.newsletter_submit, name='newsletter_submit'),
    path('profile/',views.profile,name='profile'),
    path('contact/',views.contact,name='contact'),
    # path('login/',views.login,name='login'),
    path('library/',views.library,name='library'),
    path('prediction/',views.index,name='prediction'),
    # path("signup/", authView, name="authView"),
    path('services/',views.services,name='services'),
    path('form/',views.form,name='form'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('delete/<int:id>/', views.delete_prediction, name='delete_prediction'),

]
