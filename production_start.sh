uvicorn settings.asgi:application --workers 4 --host=0.0.0.0 --port=${PORT:-5000} --loop uvloop --reload
