from functools import wraps

import flask
import werkzeug
import werkzeug.wrappers


def response(*, mimetype=None, template_file=None):
    def response_inner(f):

        @wraps(f)
        def view_method(*args, **kwargs):
            response_val = f(*args, **kwargs)

            if isinstance(response_val, werkzeug.wrappers.Response):
                return response_val

            if isinstance(response_val, flask.Response):
                return response_val

            if isinstance(response_val, dict):
                model = dict(response_val)
            else:
                model = dict()

            if template_file and not isinstance(response_val, dict):
                raise Exception(
                    f"Invalid return type {type(response_val)}, expected a dict as return val"
                 )

            if template_file:
                response_val  = flask.render_template(template_file, **response_val)

            resp = flask.make_response(response_val)
            resp.model = model
            if mimetype:
                resp.mimetype = mimetype

            return resp
        return view_method
    return response_inner
