FROM python:3.12.7-alpine3.20

WORKDIR /usr/workspace

COPY ./ /usr/workspace

RUN pip install --no-cache-dir -r requirements.txt

CMD ["pytest", "-m", "smoke", "--reruns=2", "--reruns-delay=2"]