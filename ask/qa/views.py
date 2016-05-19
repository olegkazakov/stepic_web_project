from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage
from qa.models import Question

def test(request, *args, **kwargs):
    return HttpResponse('OK')

def paginate(request, questions):
    try:
        limit = int(request.GET.get('limit', 10))
    except ValueError:
        limit = 10
    if limit > 100:
        limit = 10

    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404

    paginator = Paginator(questions, limit)

    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return page, paginator

def list(request):
    questions = Question.objects.all()
    questions = questions.order_by('-added_at')
    page, paginator = paginate(request, questions)
    paginator.baseurl = reverse('list') + '?page='

    return render(request, 'list.html', {
        'questions': page.object_list,
        'page': page,
        'paginator': paginator,
    })

def popular(request):
    questions = Question.objects.all()
    questions = questions.order_by('-rating')
    page, paginator = paginate(request, questions)
    paginator.baseurl = reverse('popular') + '?page='

    return render(request, 'list_popular.html', {
        'questions': page.object_list,
        'page': page,
        'paginator': paginator,
    })

def question_detail(request, pk):
    question = get_object_or_404(Question, id=pk)
    answers = question.answer_set.all()

    return render(request, 'detail.html', {
        'question': question,
        'answers': answers,
    })
