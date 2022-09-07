from django.urls import include
from django.urls import path
from . import views

urlpatterns = [
    path("", views.addCohort),
    path("cohortIndex/<cID>", views.cohortIndex),
    path("cohortIndex/<cID>/addMember/", views.addMember),
    path("cohortIndex/<cID>/createexam/", views.createExam),
    path("cohortIndex/<cID>/examIndex/<eID>/", views.examIndex),
    path("cohortIndex/<cID>/examIndex/<eID>/createquestion/", views.createQuestion),
    path("audio/delete/<cID>/<eID>/<uuid:id>/", views.delete_viva, name="audio_delete"),
    path(
        "question/delete/<cID>/<eID>/<id>/", views.delete_questions, name="viva_delete"
    ),
    path("viva/evaluate/<uuid:rID>/", views.viva_evaluate, name="viva_evaluate"),
    path("viva/evaluate/result/", views.show_viva_result, name="viva_evaluate_result"),
]
