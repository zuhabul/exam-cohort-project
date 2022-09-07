
from django.contrib.auth.models import User
from django.db.models import Q

from django.http import HttpResponse
from django.shortcuts import render

from cohort.models import cohortInfos,cohort




# Create your views here.
def dashboard(request):
    useer = request.user
    cohortsForUser = cohort.objects.filter(cohortinfos__Member=useer)
    return render(request,'dashboard/dashboard.html',{'cohorts':cohortsForUser})

