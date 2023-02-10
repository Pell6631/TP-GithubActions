FROM python:3.9

WORKDIR /app

COPY test_simplemath.py .
COPY simplemath.py .

CMD [ "python", "-m", "unittest", "test_simplemath.py" ]