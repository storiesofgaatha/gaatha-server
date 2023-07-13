FROM python:3.11-buster


ENV PYTHONUNBUFFERED 1

WORKDIR /code

RUN apt-get update -y && \
    apt-get install -y \
        gettext \
        # required for opencv-python for image width, height.
        libgl1-mesa-glx \
        wait-for-it && \
    rm -rf /var/lib/apt/lists/*

COPY pyproject.toml poetry.lock /code/

# Upgrade pip and install python packages for code
RUN pip install --upgrade --no-cache-dir pip poetry \
    && poetry --version \
    # Configure to use system instead of virtualenvs
    && poetry config virtualenvs.create false \
    && poetry install --no-root \
    # Remove installer
    && pip uninstall -y poetry virtualenv-clone virtualenv

COPY . /code/
