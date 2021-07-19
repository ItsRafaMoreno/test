FROM python:3.7-slim
WORKDIR /weather
COPY . /weather
RUN python3 -m pip install -U pip && \
    python3 -m pip install -r /weather/requirements.txt
ENTRYPOINT ["python3", "/weather/getweather.py"]
