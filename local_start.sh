uvicorn settings.asgi:application --workers 4 --host=0.0.0.0 --port=${PORT:-8000} --loop uvloop --reload
