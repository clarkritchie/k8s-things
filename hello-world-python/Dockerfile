FROM python:3.8-slim
WORKDIR /app
COPY app.py /app
RUN pip install flask
RUN apt update && apt install curl --assume-yes
EXPOSE 5000
CMD ["python", "app.py"]
