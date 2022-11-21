from django.contrib import admin
from .models import (Traveller,Houseown,House,Bookedhouse,Review,Post,Comment)


admin.site.register(Traveller)
admin.site.register(Houseown)
admin.site.register(Bookedhouse)
admin.site.register(Review)
admin.site.register(House)
admin.site.register(Post)
admin.site.register(Comment)