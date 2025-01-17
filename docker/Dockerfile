ARG PYTHON_VERSION=3.13.1
FROM python:${PYTHON_VERSION}-slim

# Prevents Python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1

# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1

WORKDIR /docker_template

COPY ../requirements.txt .

RUN pip install --no-cache --upgrade pip setuptools \
    && pip install -r requirements.txt \
    && pip install "psycopg[binary]"


# Create a non-privileged user that the app will run under.
# See https://docs.docker.com/go/dockerfile-user-best-practices/
ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/home/appuser" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    appuser \
    && mkdir -p /home/appuser/.vscode-server/bin \
    && chown -R appuser:appuser /home/appuser

# Switch to the non-privileged user to run the application.
USER appuser

# Copy the source code into the container.
COPY .. .

# Expose port 8000 that the application listens on.
EXPOSE 8000

# Run the application.
ENTRYPOINT ./entrypoint.sh --dev


