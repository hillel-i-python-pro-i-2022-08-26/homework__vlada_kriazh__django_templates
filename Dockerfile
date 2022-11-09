# Dockerfile сборка образа
# установка базового образа
FROM python:3.10

# не позволяет Python буферизовать выходные данные
ENV PYTHONUNBUFFERED=1

# переменные сборки
ARG WORKDIR=/wd
ARG USER=user

WORKDIR ${WORKDIR}

# создание системного пользователя и установка владельца каталога WORKDIR
RUN useradd --system ${USER} && \
    chown --recursive ${USER} ${WORKDIR}

RUN apt update && apt upgrade -y

# копирование файлов
# не копир служебные файлы
COPY --chown=${USER} requirements.txt requirements.txt

# установка зависимостей
RUN pip install --upgrade pip && \
    pip install --requirement requirements.txt

COPY --chown=${USER} --chmod=755 ./docker/app/start.sh /start.sh
COPY --chown=${USER} --chmod=755 ./docker/app/entrypoint.sh /entrypoint.sh

# копирование файлов
COPY --chown=${USER} ./contacts contacts
COPY --chown=${USER} ./django_project2 django_project2
COPY --chown=${USER} ./get_sessions_info get_sessions_info
COPY --chown=${USER} ./main main
COPY --chown=${USER} ./say_hello say_hello
COPY --chown=${USER} ./templates templates
COPY --chown=${USER} ./users users
COPY --chown=${USER} ./users_app users_app
COPY --chown=${USER} ./Makefile Makefile
COPY --chown=${USER} ./manage.py manage.py

RUN mkdir "db"

# переключение на пользователя
USER ${USER}

EXPOSE 8000

# запуск
ENTRYPOINT ["/entrypoint.sh"]

CMD ["/start.sh"]
