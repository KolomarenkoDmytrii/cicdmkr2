FROM python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
RUN python manage.py collectstatic --noinput
CMD gunicorn company.wsgi:application --bind 0.0.0.0:${PORT}
EXPOSE 8000
