import logging
import json
import uuid
import datetime


def access_log_middleware(get_response):
    logger = logging.getLogger("access_logger")
    date = datetime.datetime

    def now():
        return date.utcnow()

    def format_time(time):
        return time.isoformat('T') + 'Z'

    def middleware(request):

        request_id = str(uuid.uuid4())

        start = now()

        info = {
            'timestamp': format_time(start),
            'request_id': request_id,
            'method': request.method,
            'path': request.path,
            'body': request.body.decode("utf-8")[:500],
        }

        logger.info(json.dumps(info))

        response = get_response(request)

        finish = now()
        diff = finish - start
        info = {
            'timestamp': format_time(finish),
            'request_id': request_id,
            'status_code': response.status_code,
            'response_time': "{}ms".format(int((diff.seconds * 1_000_000 + diff.microseconds) / 1000)),
            'body': response.content.decode("utf-8")[:500],
        }

        if response.status_code >= 500:
            logger.error(info)
        else:
            logger.info(info)

        return response

    return middleware
