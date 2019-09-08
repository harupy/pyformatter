FROM python:3.7

ENV PIPENV_VENV_IN_PROJECT=1
WORKDIR /app

COPY Pipfile Pipfile.lock ./
RUN pip install pipenv && pipenv install

CMD ["pipenv", "run", "python", "run.py"]