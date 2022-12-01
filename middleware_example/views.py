from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Count
from django.shortcuts import render
from middleware_example.models import RequestData
from django_project2.settings import INIT_INFO_MIDDLEWARE


# get data from db
def all_data(request):
    data = RequestData.objects.all()
    return render(request, "middleware/index.html", {"data": data,
                                                     "middleware": INIT_INFO_MIDDLEWARE})


@login_required
def data_by_user(request):
    user_data = RequestData.objects.filter(user=request.user)
    result = user_data.aggregate(amount_of_requests=Sum('count_of_visits'),
                                 amount_of_visiting_page=Count('count_of_visits'))

    return render(request, "middleware/index.html",
                  {"data": user_data,
                   "amount_of_page": result['amount_of_visiting_page'],
                   "amount_of_requests": result['amount_of_requests'],
                   "filter_by": 'user',
                   "middleware": INIT_INFO_MIDDLEWARE})


def data_by_session(request):
    session = request.session
    session_key = session.session_key

    session_data = RequestData.objects.filter(session_key=session_key)
    result = session_data.aggregate(amount_of_requests=Sum('count_of_visits'),
                                    amount_of_visiting_page=Count('count_of_visits'))

    return render(request, "middleware/index.html",
                  {"data": session_data,
                   "amount_of_page": result['amount_of_visiting_page'],
                   "amount_of_requests": result['amount_of_requests'],
                   "filter_by": 'session',
                   "middleware": INIT_INFO_MIDDLEWARE})
