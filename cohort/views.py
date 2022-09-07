# from asyncio.windows_events import NULL
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render
from core.models import Record, RecordAnswer


from .models import cohortInfos, cohort

from .forms import createCohortForm, addMemberForm
from django.contrib.auth.models import User
from .models import QuesModel, ExamInfo
from .forms import addQuestionform, addExamForm
from django.http.response import JsonResponse


# -------------

import utils

from decouple import config


# Create your views here.


def addCohort(request):
    if request.method == "POST":
        form = createCohortForm(request.POST)
        if form.is_valid():
            u = request.user
            name = form.cleaned_data["name"]
            chrt = cohort(CohortName=name, Admin=u.email)
            chrt.save()
            chrtInfo = cohortInfos(cohort=chrt, Member=u, MemberStatus="admin")
            chrtInfo.save()
            return HttpResponseRedirect("/dashboard")
    else:
        form = createCohortForm()
    return render(request, "cohort/createcohort.html", {"f": form})


def cohortIndex(request, cID):
    chrt = cohort.objects.get(CohortID=cID)
    cohortInformation = cohortInfos.objects.get(cohort=chrt, Member=request.user)
    exams = ExamInfo.objects.filter(cohort=chrt)

    if request.user.email == cohortInformation.cohort.Admin:
        return render(
            request,
            "cohort/cohortIndexAdmin.html",
            {"Info": cohortInformation, "exams": exams},
        )
    else:
        return render(
            request,
            "cohort/cohortIndexExaminee.html",
            {"Info": cohortInformation, "exams": exams},
        )


def addMember(request, cID):
    chrt = cohort.objects.get(CohortID=cID)
    cohortInformation = cohortInfos.objects.get(cohort=chrt, Member=request.user)
    if request.method == "POST":
        form = addMemberForm(request.POST)
        messages.success(request, "Examinee added successfully")
        if form.is_valid():
            email = form.cleaned_data["memberEmail"]
            member = User.objects.get(email__exact=email)
            # member.save()
            cohortadd = cohortInfos(cohort=chrt, Member=member, MemberStatus="examinee")

            cohortadd.save()
            form = addMemberForm()
    else:
        form = addMemberForm()

    memberlist = cohortInfos.objects.filter(cohort=chrt)

    return render(
        request, "cohort/addMember.html", {"f": form, "memberlist": memberlist}
    )


def createExam(request, cID):
    chrt = cohort.objects.get(CohortID=cID)
    if request.method == "POST":
        form = addExamForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["examName"]
            type = form.cleaned_data["examType"]
            exam = ExamInfo(examName=name, cohort=chrt, examType=type)
            exam.save()
            url = "/cohort/cohortIndex/" + cID
            return HttpResponseRedirect(url)
    else:
        form = addExamForm()

    return render(
        request,
        "exam/addExam.html",
        {
            "f": form,
        },
    )


def examIndex(request, cID, eID):
    chrt = cohort.objects.get(CohortID=cID)
    exxam = ExamInfo.objects.get(examID=eID)
    member = cohortInfos.objects.get(cohort=chrt, Member=request.user)

    questions = QuesModel.objects.filter(examID=exxam.examID)

    records = Record.objects.filter(cohort_id=chrt, exam_id=exxam)
    # context = {"page_title": "Voice records", "records": records}
    # return render(request, "core/index.html", context)

    if request.user.email == chrt.Admin:
        return render(
            request,
            "exam/examIndexAdmin.html",
            {"questions": questions, "Info": chrt, "exam": exxam, "records": records},
        )
    if request.user == member.Member and member.MemberStatus == "examinee":
        if request.method == "POST":
            print(request.POST)
            score = 0
            wrong = 0
            correct = 0
            total = 0
            for q in questions:
                total += 1
                if q.ans == request.POST[q.question]:
                    score += 1
                    correct += 1
                else:
                    wrong += 1
            context = {
                "score": score,
                "correct": correct,
                "wrong": wrong,
                "total": total,
            }
            return render(request, "exam/result.html", context)
        else:
            return render(
                request,
                "exam/index.html",
                {
                    "questions": questions,
                    "Info": chrt,
                    "exam": exxam,
                    "records": records,
                },
            )


def createQuestion(request, cID, eID):
    chrt = cohort.objects.get(CohortID=cID)
    exxam = ExamInfo.objects.get(examID=eID)
    c = chrt.CohortID
    e = exxam.examID
    if exxam.examType == "Quiz":
        if request.method == "POST":
            form = addQuestionform(request.POST)
            if form.is_valid():
                ques = form.cleaned_data["question"]
                opt1 = form.cleaned_data["op1"]
                opt2 = form.cleaned_data["op2"]
                opt3 = form.cleaned_data["op3"]
                opt4 = form.cleaned_data["op4"]
                ansr = form.cleaned_data["ans"]
                questions = QuesModel(
                    question=ques,
                    op1=opt1,
                    op2=opt2,
                    op3=opt3,
                    op4=opt4,
                    ans=ansr,
                    examID=eID,
                )
                questions.save()
                url = (
                    "/cohort/cohortIndex/"
                    + cID
                    + "/examIndex/"
                    + eID
                    + "/createquestion/"
                )
                return HttpResponseRedirect(url)
        else:
            form = addQuestionform()
    elif exxam.examType == "Micro-Viva":
        return render(request, "exam/addViva.html", {"eID": e})
    return render(request, "exam/addquestion.html", {"form": form})


def delete_questions(request, cID, eID, id):
    member = QuesModel.objects.get(id=id)
    member.delete()
    url = "/cohort/cohortIndex/" + cID + "/examIndex/" + eID + "/"
    return HttpResponseRedirect(url)


def delete_viva(request, cID, eID, id):
    member = Record.objects.get(id=id)
    member.delete()
    url = "/cohort/cohortIndex/" + cID + "/examIndex/" + eID + "/"
    return HttpResponseRedirect(url)


from pathlib import Path


def viva_evaluate(request, rID):

    if request.method == "POST":
        record = Record.objects.get(id=rID)
        audio_file = request.FILES.get("recorded_audio")
        language = "ENG"
        record_ans = RecordAnswer.objects.create(
            language=language, voice_record=audio_file
        )
        record_ans.save()
        file_answer_supplied = Path(record_ans.voice_record.path)
        file_answer = Path(record.answer_record.path)

        # ans_url = record.answer_record.url
        AAI_API_KEY = config("AAI_API_KEY")

        header = {"authorization": AAI_API_KEY, "content-type": "application/json"}
        BASE_URL = config("BASE_URL")
        # file submitted
        upload_url = utils.upload_file(file_answer, header)
        print(upload_url)
        transcript_response = utils.request_transcript(upload_url, header)

        polling_endpoint = utils.make_polling_endpoint(transcript_response)
        print(polling_endpoint)
        utils.wait_for_completion(polling_endpoint, header)
        paragraphs = utils.get_paragraphs(polling_endpoint, header)
        print(paragraphs)
        print(paragraphs)
        answer_text = ""
        for para in paragraphs:
            print(para["text"])
            answer_text = para["text"]

        upload_url = utils.upload_file(file_answer_supplied, header)
        print(upload_url)
        transcript_response = utils.request_transcript(upload_url, header)

        polling_endpoint = utils.make_polling_endpoint(transcript_response)
        print(polling_endpoint)
        utils.wait_for_completion(polling_endpoint, header)
        paragraphs = utils.get_paragraphs(polling_endpoint, header)
        print(paragraphs)
        answer_supplied = ""
        for para in paragraphs:
            print(para["text"])
            answer_supplied = para["text"]
        messages.success(request, "Audio recording successfully added!")
        url = "/cohort/viva/evaluate/result/"
        answer_text = answer_text[-1]
        answer_supplied = answer_supplied[-1]
        print(answer_text)
        print(answer_supplied)

        print(answer_supplied in answer_text)
        isPassed = "did not passed"
        if answer_supplied in answer_text:
            isPassed = "passed"

        return JsonResponse({"url": url, "success": True, "result": isPassed})


def show_viva_result(request):
    return render(
        request,
        "exam/microVivaResult.html",
    )
