from flask import request, jsonify
from pydantic import ValidationError
from functools import wraps

def validate_request(model):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            try:
                if not request.is_json:
                    return jsonify({"error": "Request must be JSON"}), 415

                # Validate JSON body
                data = model(**request.get_json())

                # Attach validated data to request
                request.data = data # type: ignore

            except ValidationError as e:
                return jsonify({"errors": e.errors()}), 422

            return f(*args, **kwargs)
        return wrapper
    return decorator

