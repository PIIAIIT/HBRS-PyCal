FROM alpine:latest
MAINTAINER Patrick
LABEL authors="patrick"

# 1. Install the necessary packages
RUN apt-get update && apt-get install -y python3 \
    python3-tk \
    python3-requests \
    python3-bs4

# 3. Copy the source code into the container \
COPY . /app
WORKDIR /app

# 5. Run the application
CMD ["sh", "start.sh"]

# 6. Build the Docker image
# docker build -t studentplanapp .
