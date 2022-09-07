from django.contrib import admin
from .models import ExamInfo, QuesModel, cohortInfos, cohort

# Register your models here.
##class cohortInfoAdmin(admin.ModelAdmin):
  ##  list_display = ('CohortID', 'CohortName','CohortAdminEmail')

admin.site.register(cohortInfos)

##class cohortMembersDB(admin.ModelAdmin):
  ##  list_display = ('id', 'CohortName', 'Member', 'Admin')

admin.site.register(cohort)

admin.site.register(QuesModel)
admin.site.register(ExamInfo)