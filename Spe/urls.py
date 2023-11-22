from django.urls import path 
from Spe.views import * 
app_name='Specific'

urlpatterns=[
    path('Spe1/',Spe1,name='Spe1'),
     path('Spe2/',Spe2,name='Spe2')
]