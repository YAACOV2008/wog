FROM python:3.13-alpine
WORKDIR /app
COPY ./utilities ./utilities
COPY ./templates ./templates
RUN pip install flask
RUN chmod +x ./utilities/entrypoint.sh
VOLUME /app
EXPOSE 5000
ENTRYPOINT ["./utilities/entrypoint.sh"]
CMD python utilities/main_score.py
