FROM python:3.6-slim
MAINTAINER shihabyasin@gmail.com
COPY . /python-project-compute
WORKDIR /python-project-compute
RUN pip install --no-cache-dir -r requirements.txt
RUN ["pytest", "-v", "--junitxml=reports/result.xml"]
CMD tail -f /dev/null