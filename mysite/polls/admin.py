from django.contrib import admin

# Register your models here.
from polls.models import Poll, Choice

class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 4

class PollAdmin(admin.ModelAdmin):
	fieldsets = [
		('Questions BEYATCH!!!',			{'fields': ['question']}),
		('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
	]

	list_filter = ['pub_date']
	
	inlines = [ChoiceInline]
	search_fields = ['question']
	
	# fields = ['pub_date', 'question']
	# list_display is the tuple of field names to display on the admin panel
	list_display = ('question', 'pub_date', 'was_published_recently')

admin.site.register(Poll, PollAdmin)