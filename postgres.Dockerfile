FROM postgres:latest

RUN addgroup  scratch
RUN useradd -g scratch scratch

ENV POSTGRES_DB scratch

COPY data.csv /tmp/data.csv
RUN chown -R scratch:scratch /tmp/data.csv
RUN chown -R scratch:scratch /var/lib/postgresql/

EXPOSE 5432

USER scratch
COPY script.sql /docker-entrypoint-initdb.d/script.sql

