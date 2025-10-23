FROM alpine:3.14

WORKDIR /app

RUN apk add --no-cache python3 py3-pip tzdata ffmpeg

COPY src/ ./src/

RUN python3 -m venv /app/.venv
ENV PATH="/app/.venv/bin:$PATH"

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r src/requirements.txt

RUN /app/.venv/bin/python3 src/manage.py migrate

EXPOSE 8000

CMD ["python3", "src/manage.py", "runserver", "0.0.0.0:8000"]

