from django.urls import path

from . import views


app_name = "core"

urlpatterns = [
    path("micro/<cID>/examIndex/<eID>/", views.index, name="index"),
    path("micro/viva/exam/<cID>/examIndex/<eID>/", views.micro_viva_exam, name="index"),
    path("record/<cID>/examIndex/<eID>/", views.record, name="record"),
    path(
        "record/answer/<uuid:id>/",
        views.record_answer,
        name="record_detail",
    ),
    path("record/detail/<uuid:id>/", views.record_detail, name="record_detail"),
]
