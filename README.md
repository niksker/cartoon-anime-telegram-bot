
# Cartoon + Anime Telegram Bot

Этот Telegram-бот позволяет преобразовывать фотографии в мультяшный или аниме-стиль.

## Поддерживаемые стили:
- 🎨 Cartoon (OpenCV)
- 🌸 Hayao
- 🎬 Shinkai
- 🎥 Paprika
- ✨ Pixar

## Установка

1. Установите зависимости:

```
pip install -r requirements.txt
```

2. Создайте папку `models` и добавьте туда .onnx модели:
- `hayao.onnx`
- `shinkai.onnx`
- `pixar.onnx`
- `paprika.onnx`

3. Запустите бота:

```
BOT_TOKEN=your_token_here python main.py
```

## Деплой

Для Render или Railway добавьте переменную окружения `BOT_TOKEN` и укажите `Procfile`.
