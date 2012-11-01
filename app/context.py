from datetime import datetime
from flask import url_for

def static(filename, **kwargs):
    return url_for('.static', filename=filename, **kwargs)

def context_processors():
    return {
        'now': datetime.now,
        'static': static,
    }
