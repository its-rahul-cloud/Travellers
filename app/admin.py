from django.contrib import admin
from .models import (Traveller,Houseown,House,Bookedhouse,Review)


admin.site.register(Traveller)
admin.site.register(Houseown)
admin.site.register(Bookedhouse)
admin.site.register(Review)
admin.site.register(House)