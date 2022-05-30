FROM python:3.9.13-slim-bullseye
COPY service/app.py requirements.txt /app/
WORKDIR /app
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
RUN rm -f requirements.txt
EXPOSE 8080
CMD python -u app.py
