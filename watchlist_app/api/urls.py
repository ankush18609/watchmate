from django.urls import path,include

from . import views
urlpatterns = [
    path('movielist/',views.WatchListAv.as_view(),name='movie_list'),
    path('<int:pkey>/',views.watchlistDetail.as_view(),name='get_by_id'),
    path('stream/',views.streamplateformAv.as_view(),name='stream'),
  path('stream/<int:pk>/',views.streamplateformDetail.as_view(),name='streamplateformlist'),
  path('<int:pkey>/review/',views.reviewlistav.as_view(),name='review'),
  path('review/<int:pk>/',views.reviewdetails.as_view(),name='reviewdetails')
]
