from django.urls import path
from .views import HomePage, CreatePatiant, PatientDetail, PatientEdit, PatienDelete

urlpatterns = [
    path('', HomePage.as_view(), name='home'),

    path('post/<int:pk>/delete/', PatienDelete.as_view(), name='delete_patient'),
    path('post/<int:pk>/edit/', PatientEdit.as_view(), name='edit_patient'),
    path('new/', CreatePatiant.as_view(), name='new_patient'),
    path('post/<int:pk>/', PatientDetail.as_view(), name='post_detail'),
]