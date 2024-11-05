from django.urls import path
from . import views
urlpatterns = [
    path('login/',views.login,name='login'),
    path('',views.index,name='index',),
    path('course/',views.course,name='course',),
    path('home/',views.home,name='home',),
    path('student/',views.student,name='student',),
    path('teacher/',views.teacher,name='teacher',),
    path('about/',views.about,name='about',),
    path('save/',views.save,name='save'),
    path('data/', views.data, name='data'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('edit/<int:id>/',views.edit,name='edit'),
    
   
    path('save1/',views.save1,name='save1'),
    path('data1/', views.data1, name='data1'),
    path('delete1/<int:id>/',views.delete1,name='delete1'),
    path('edit1/<int:id>/',views.edit1,name='edit1'),

    path('save2/',views.save2,name='save2'),
    path('data2/', views.data2, name='data2'),
    path('delete2/<int:id>/',views.delete2,name='delete2'),
    path('edit2/<int:id>/',views.edit2,name='edit2'),
    
    ]