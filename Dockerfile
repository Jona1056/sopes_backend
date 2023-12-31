FROM alpine:3.19.0
RUN apk add --no-cache python3-dev py3-pip
RUN python3 -m venv /venv
ENV PATH="/venv/bin:$PATH"
RUN pip3 install --upgrade pip
RUN pip3 install --upgrade Flask 
RUN pip3 install --upgrade Flask-Cors
RUN pip3 install  mysql-connector-python
RUN apk add --no-cache bash
WORKDIR /app
COPY app.py /app
EXPOSE 5000
RUN ls
CMD ["python3", "app.py"]