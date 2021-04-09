## Ставим зависимости conda
conda env create -f environment.yml

## Классификация без детекции - cats vs dogs
Скачиваем датасет https://download.microsoft.com/download/3/E/1/3E1C3F21-ECDB-4869-8368-6DEBA77B919F/kagglecatsanddogs_3367a.zip

Распаковываем в текущей дирректории папку `PetImages` и её содержимое


## Разметка датасета labelme
https://github.com/wkentaro/labelme
```
conda install labelme -c conda-forge
```

Запуск `labelme`


## Детекция касок с разметкой


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

## Простой трекер персон на YOLO-3/4 tiny

Статья https://habr.com/ru/company/recognitor/blog/505694/
Описание SORT и как работает http://cv-blog.ru/?p=322
Источник https://github.com/ZlodeiBaal/SimpleTrackSample
Адаптация https://github.com/akumidv/SimpleTrackSample


```
cd ./simple-track
```

Скачиваем веса модели YOLO3 https://pjreddie.com/media/files/yolov3-tiny.weights
Скачиваем веса модели YOLO4 https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v4_pre/yolov4-tiny.weights

Запускаем по умолчанию YOLO3-tiny с видеокарты 0
```
python.exe Demo_Tracking.py
```
Вебкамера 1 и YOLO4-tiny
```
python Demo_Tracking.py --video 1 --version 4
```


Вебкамера 1 и YOLO4
```
python Demo_Tracking.py --video 1 --version 4 --type full
```


# Human Pose Estimation
Источник https://github.com/leoxiaobin/deep-high-resolution-net.pytorch

В папаке `human-pose`

Установка Pytorch https://pytorch.org/
```
conda install pytorch torchvision torchaudio cpuonly -c pytorch
```
Переходим в папку `lib` и выполняем в ней
```
make
```

