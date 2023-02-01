echo yes | python ./manage.py collectstatic
gunicorn \
    config.wsgi:application \
    --bind 0.0.0.0:8000 \
    --max-requests 1000 \
    --max-requests-jitter 50
