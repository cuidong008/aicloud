FROM tensorflow/tensorflow:2.5.0
#FROM tf:2.5.0

RUN pip install minio matplotlib --no-cache-dir
RUN pip install aicloudx --index-url https://pypi.org/simple/ --no-deps --no-cache-dir
