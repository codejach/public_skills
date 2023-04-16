# Project description

This is an API test project whose purpose is to show how .NET SDK 3.1 platform is implemented on top of the Docker system.

## Requirements

- Docker
- docker-compose

## How to setup

To run the project, follow the steps below:

1. Clone this repository to your local machine running the following command:
```bin/bash
git clone https://github.com/codejach/public_skills.git
```

2. In the terminal, navigate to the project folder and run the following command:
```bin/bash
make install
```

3. After the image has been successfully created, run the following command:
```bin/bash
make run
```
This statement will run the project and expose ports 5000 and 5001.

4. Send a HTTP request to the following url:
```bin/bash
http://localhost:5000/weatherforecast
```

5. To stop the container, running the following command:
```bin/bash
make stop
```

If you need to connect to the container, can you run the following command:
```bin/bash
make dev
```

## Points to consider

1. The container cannot be attached via Visual Studio Code because the minimum requirements for it to run are Alpine 3.9
2. The container is built with Alpine 3.8 because this version includes libssl1.0
3. The container is built with libssl1.0 because .NET SDK 3.1 is not supported in higher versions.

If you want to use Visual Studio Code in this project, please configure Dockerfile and manually download libssl1.0 and build the container using Alpine 3.9 or higher, the detailed process will not be covered in this project.
