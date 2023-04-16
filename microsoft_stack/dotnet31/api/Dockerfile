FROM alpine:3.8

WORKDIR /home/app

RUN apk update && apk add \
    curl \
    bash \
    icu \
    libintl \
    libgcc \
    libssl1.0 \
    libstdc++ \
    wget

RUN curl -sL https://dot.net/v1/dotnet-install.sh -O dotnet-install.sh

RUN chmod +x ./dotnet-install.sh

RUN ./dotnet-install.sh --channel 3.1

ENV PATH="$PATH:/root/.dotnet"
