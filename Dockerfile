FROM python:3.11.0-slim
COPY . /app
WORKDIR /app
RUN python3 -m venv /opt/venv
RUN pip install pip --upgrade
RUN ls /opt/venv/bin
RUN ls /app/requirement.txt
RUN chmod +x /app/requirement.txt
RUN /opt/venv/bin/pip install -r /app/requirement.txt
RUN chmod +x /app/entrypoint.sh
CMD ["/app/entrypoint.sh"]

