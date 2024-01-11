from django.urls import path
from . import views

urlpatterns = [
    path('temp/', views.votingTemp, name="name"),
    path('', views.index, name="name"),
    # path('voter/', views.login, name="login"),
    path('all/', views.my_view, name="voter"),
    path('edit/<int:id>/', views.my_view, name='edit_item'),
    path('delete/<int:id>/', views.delete, name='delete_item'),
    path('edit-item/<int:id>/', views.edit, name='edit_item'),
    # login
    path('login/', views.user_login, name='login'),
    path('register/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
]