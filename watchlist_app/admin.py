from django.contrib import admin
from watchlist_app.models import movie,streamplateform,watchlist,review

# Register your models here.
admin.site.register(movie)
admin.site.register(streamplateform)
admin.site.register(watchlist)
admin.site.register(review)