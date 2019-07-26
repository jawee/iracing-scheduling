FROM python:3
WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
#ENV FLASK_APP=app.py
#ENV FLASK_DEBUG=1
#ENV FLASK_ENV=development
#EXPOSE 5000
#CMD ["python", "-m", "flask", "run"]
COPY . .
#CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]

#CMD ["python", "app.py"]