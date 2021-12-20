FROM python:3.8-slim-buster
COPY . /app
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install flask flask_cors dapr
ENTRYPOINT ["python"]
EXPOSE 8080
ENV APP_VERSION="0.0.1"
CMD ["app.py"]
