# syntax=docker/dockerfile:1.2
FROM python:3.12

WORKDIR /app

RUN --mount=type=bind,target=/tmp/requirements.txt,source=requirements.txt \
    pip install -r /tmp/requirements.txt

COPY todo/ /app/todo
COPY entrypoint.sh /app/
RUN chmod +x /app/entrypoint.sh

EXPOSE 5555

ENTRYPOINT ["/app/entrypoint.sh"]
CMD ["run"]
