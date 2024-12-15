from django.contrib import admin
from backoffice.models import *

admin.site.register(Service)
admin.site.register(Car)
admin.site.register(Coordinate)
admin.site.register(ContactForm)
admin.site.register(CarForm)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('author', 'content', 'active')
    list_filter = ('active',)
    search_fields = ('author', 'content')
    actions = ['approve_reviews']

    def approve_reviews(self, request, queryset):
        queryset.update(active=True)
    approve_reviews.short_description = "Approuver les avis sélectionnés"

