import json

_RESPONSES = {
    19: "Unexpected error. We are warned.",
    20: "Success.",
}


class JSONEncoder(json.JSONEncoder):
    """
    This is a monkey patch to extend the serialization ability of the json
    library. Most of time your data includes arbitrary objects which are not
    json serializable. This patch try to serialize data with the default
    methods. If it failds, then, it tries to serilalize them as string.
    """
    def default(self, o):
        try:
            return getattr(o.__class__, "__publicJson__", "__json__")(o)
        except Exception, e:
            return str(o)


def make(responseCode, data=None):
    return makeRaw(responseCode, _RESPONSES[responseCode], data)


def makeRaw(statusCode, statusMessage, data=None):
    response = {}
    response['status'] = {
        'code': statusCode,
        'message': statusMessage}

    if data:
        response['data'] = data

    return JSONEncoder().encode(response)