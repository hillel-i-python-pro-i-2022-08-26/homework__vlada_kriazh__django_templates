from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from datetime import datetime


def get_session(request: HttpRequest) -> HttpResponse:
    session = request.session

    count_of_visits = session.get('count_of_visits', 0)
    count_of_visits += 1
    session['count_of_visits'] = count_of_visits

    datatime = session.get('datatime', '-')
    session['datatime'] = str(datetime.now().strftime("%m.%d.%Y, %H:%M:%S"))

    return render(
        request,
        'sessions.html',
        {
            'session_id': session.session_key,
            'session_datetime': datatime,
            'count_of_visits': count_of_visits
        }
    )
