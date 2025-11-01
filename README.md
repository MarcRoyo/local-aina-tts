This project is a text-to-speech (TTS) application that utilizes Docker for containerization. The application is designed to convert text input into speech using machine learning models.

## Project Structure

The project consists of the following files and directories:

- **docker-compose.yml**: Defines the services, networks, and volumes for the Docker Compose application.
- **.dockerignore**: Specifies which files and directories should be ignored by Docker when building images.
- **services/tts/Dockerfile**: Contains instructions to build the Docker image for the "tts" service, setting up the environment and installing dependencies.
- **services/tts/requirements.txt**: Lists the Python dependencies required for the application.
- **services/tts/infer_onnx.py**: The main Python script that will be executed when the container runs.

## Getting Started

To get started with the project, follow these steps:

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd local-aina-tts
   ```

2. **Build and run the application**:
   ```
   docker-compose up --build
   ```

3. **Access the application**:
   The application will be accessible at `http://localhost:7860`.

## Dependencies

Make sure to check the `requirements.txt` file for the list of Python dependencies required for the application.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

---
title: Catalan Text-to-Speech
emoji: 🍵+🥑
colorFrom: purple
colorTo: yellow
sdk: docker
pinned: true
license: apache-2.0
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference

## Preparar l'entorn

```bash
py -m venv venv
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser 
.\venv\Scripts\activate 
```

## Arrancar el docker

Instruccions per arrancar el docker:
```bash
docker build .
docker run -p 7860:7860 --gpus=all 33c08f7c6fff
```
despres obrir el browser i posar: http://localhost:7860/


docker volume create --opt type=none --opt o=bind --opt device=./data/tts data-tts
docker volume create --opt type=none --opt o=bind --opt device="C:\root\code\github.com\MarcRoyo\local-aina-tts\data\tts" data-tts

docker exec -it 04eaa0b6f23f bash

docker compose ps

docker cp "C:\root\code\github.com\MarcRoyo\local-aina-tts\services\tts\infer_onnx.py" 04eaa0b6f23f:/home/user/app/infer_onnx.py

docker exec -u root 04eaa0b6f23f chown user:user /home/user/app/infer_onnx.py

docker cp "C:\root\code\github.com\MarcRoyo\local-aina-tts\services\tts\requirements.txt" 04eaa0b6f23f:/home/user/app/requirements.txt

docker exec -u user 04eaa0b6f23f pip install -r requirements.txt

docker restart 04eaa0b6f23f