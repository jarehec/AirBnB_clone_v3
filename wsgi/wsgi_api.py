#!/usr/bin/python3
"""
imports API App for gunicorn configurations
gunicorn --bind 127.0.0.1:8003 wsgi.wsgi_hbnb:web_flask.app
"""
app = __import__('api.v1.views.app', globals(), locals(), ['*'])

if __name__ == "__main__":
    """runs the main flask app"""
    app.run_main_app()
