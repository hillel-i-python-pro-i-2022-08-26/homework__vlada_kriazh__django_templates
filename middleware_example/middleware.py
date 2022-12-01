import logging
from collections.abc import Callable
from middleware_example.models import RequestData


def update_or_create_request_data(path, user, session_key):
    count_of_visits_last = RequestData.objects.filter(key=f'{path}-{user}-{session_key}').last()

    if count_of_visits_last is not None:
        count_of_visits_new = count_of_visits_last.count_of_visits + 1
    else:
        count_of_visits_new = 1

    values_for_update = {"path": path, "user": user,
                         "session_key": session_key, "count_of_visits": count_of_visits_new}
    data_object, created = RequestData.objects.update_or_create(key=f'{path}-{user}-{session_key}',
                                                                defaults=values_for_update,)
    return f'{data_object}, is created: {created}'


class SimpleLoggingMiddleware:
    def __init__(self, get_response: Callable):
        self.get_response = get_response
        self.logger = logging.getLogger('django')
        self.logger.info('Init')

    def __call__(self, request):
        session = request.session
        if not session.session_key:
            session.save()
        session_key = session.session_key

        response = self.get_response(request)
        if request.user.is_authenticated:
            user = request.user
        else:
            user = None

        self.logger.info(update_or_create_request_data(request.path, user, session_key))

        return response
