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