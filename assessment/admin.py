from django.contrib import admin

from assessment.models import Assessment, TesteeAssessment, TesteeResponse

class TesteeResponseInline(admin.StackedInline):
    model = TesteeResponse
    extra = 0

class TesteeAssessmentAdmin(admin.ModelAdmin):
    inlines = [TesteeResponseInline] 

admin.site.register(Assessment)
admin.site.register(TesteeAssessment, TesteeAssessmentAdmin)
# admin.site.register(TesteeResponse)
