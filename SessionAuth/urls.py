from django.contrib import admin
from django.urls import path
from crud import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.register_view,name="register"),
    path('login/', views.login_view,name="login"),
    path('logout/', views.logout_view,name="logout"),
    path('dashboard/', views.dashboard,name="dashboard"),
    path('create/', views.create,name="create"),
    path('update/<int:id>', views.update,name="update"),
    path('delete/<int:id>', views.delete,name="delete"),
]
