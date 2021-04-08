

## YOLO-4 на tensorflow
Статья https://habr.com/ru/post/531786/ (с другими фреймворками в т.ч.)
Источник https://github.com/hunglc007/tensorflow-yolov4-tflite
Адаптация https://github.com/akumidv/tensorflow-yolov4-tflite
```
cd ./tensorflow-yolov4-tflite
```

Скачиваем веса модели в папку `data` https://drive.google.com/open?id=1cewMfusmPjYWbrnuJRuKhPMwRe_b9PaT

Конвертируем модель
```
python save_model.py --weights ./data/yolov4.weights --output ./checkpoints/yolov4-416 --input_size 416 --model yolov4
```

Запуск на изображении
```
python detect.py --weights ./checkpoints/yolov4-416 --size 416 --model yolov4 --image ./data/kite.jpg
```

Смотрим в файле `./result.png`

Запуск на видео
```
python detectvideo.py --weights ./checkpoints/yolov4-416 --size 416 --model yolov4 --video ./data/road.mp4 --output ./output.avi
```
Результат в файле `./output.avi`

Запуск камера 0
```
python detectvideo.py --weights ./checkpoints/yolov4-416 --size 416 --model yolov4 --video 0
```

## Простой трекер на YOLO-3 tiny

Статья https://habr.com/ru/company/recognitor/blog/505694/
Описание SORT и как работает http://cv-blog.ru/?p=322
Источник https://github.com/ZlodeiBaal/SimpleTrackSample
Адаптация https://github.com/akumidv/SimpleTrackSample


```
cd ./simple-track
```

Скачиваем веса модели https://pjreddie.com/media/files/yolov3-tiny.weights

Запускаем
```
python.exe Demo_Tracking.py
```