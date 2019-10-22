FROM python
RUN pip3 install flask
RUN pip3 install pymongo
COPY . /app
WORKDIR /app
SHELL ["/bin/bash", "-c"]
EXPOSE 9090
CMD ["python3","app.py"]