from django.contrib import messages
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, render

from .models import Record
from cohort.models import cohort, ExamInfo


def record(request, cID, eID):
    if request.method == "POST":
        chrt = cohort.objects.get(CohortID=cID)
        exxam = ExamInfo.objects.get(examID=eID)
        audio_file = request.FILES.get("recorded_audio")
        language = request.POST.get("language")
        record = Record.objects.create(
            language=language, voice_record=audio_file, cohort_id=chrt, exam_id=exxam
        )
        record.save()
        messages.success(request, "Audio recording successfully added!")
        print(record.id)
        return JsonResponse(
            {"url": record.get_absolute_url(), "success": True, "record_id": record.id}
        )
    context = {
        "page_title": "Record Audio Page",
        # "record_id": record.id,
        "cid": cID,
        "eid": eID,
    }
    return render(request, "core/record.html", context)


def record_answer(request, id):
    if request.method == "POST":
        # chrt = cohort.objects.get(CohortID=cID)
        # exxam = ExamInfo.objects.get(examID=eID)
        record = Record.objects.get(id=id)
        audio_file = request.FILES.get("recorded_audio")
        record.answer_record = audio_file
        # language = request.POST.get("language")
        # record = Record.objects.create(
        #      voice_record=audio_file, cohort_id=chrt, exam_id=exxam
        # )
        record.save()
        messages.success(request, "Audio answer recording successfully added!")
        return JsonResponse({"url": record.get_absolute_url(), "success": True})
    context = {"page_title": "Record Audio Page"}
    return render(request, "core/record_answer.html", context)


def record_detail(request, id):
    record = get_object_or_404(Record, id=id)
    context = {
        "page_title": "Recorded audio detail",
        "record": record,
    }
    return render(request, "core/record_detail.html", context)


def index(request, cID, eID):
    print(cID)
    print(eID)
    chrt = cohort.objects.get(CohortID=cID)
    exxam = ExamInfo.objects.get(examID=eID)
    print(chrt)
    print(exxam)
    records = Record.objects.all()
    context = {"page_title": "Voice records", "records": records}
    return render(request, "core/index.html", context)


def micro_viva_exam(request, cID, eID):
    chrt = cohort.objects.get(CohortID=cID)
    exxam = ExamInfo.objects.get(examID=eID)
    records = Record.objects.filter(exam_id=exxam, cohort_id=chrt).last()
    context = {"page_title": "Voice records", "records": [records]}
    return render(request, "exam/microVivaExam.html", context)
