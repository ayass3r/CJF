from django.contrib import admin
from Schedule.models import Day, Show

class ShowInline(admin.StackedInline):
	model = Show
	extra = 2

class DayAdmin(admin.ModelAdmin):
	inline  = [ShowInline]

admin.site.register(Day)
admin.site.register(Show)