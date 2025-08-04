FROM debian:bookworm

RUN apt update && apt install -y \
    ocaml \
    opam \
    make \
    python3 \
    python3-pip \
    curl \
    && apt clean

RUN opam init -y --disable-sandboxing
SHELL ["/bin/bash", "-c"]
RUN eval $(opam env) && opam install ocamlfind ounit2 -y

WORKDIR /app/marina
COPY marina/ .
RUN eval $(opam env) && make

WORKDIR /app
COPY app.py requirements.txt ./
# COPY certs ./certs

RUN pip3 install --no-cache-dir --break-system-packages -r requirements.txt

EXPOSE 5000

CMD ["python3", "app.py"]