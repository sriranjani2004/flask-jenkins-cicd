FROM python:3.9
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 5055
ENV FLASK_APP=app.py
CMD ["python", "app.py"]
