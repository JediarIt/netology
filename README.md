# Сохранение результатов эксперимернта
Цель исследования — определения качества вина по его физико-химическим характеристикам. 
Выбранная модель — случайный лес.
Этапы: 
- удаление пропусков
- работа с выбросами
- создание признака свободных дикосидов
- оверсемплинг
- обучение логистической регресии и случайного леса
- анализ точности и матрицы ошибок 

## Состав репозитория

- *models* -- сохраненные модели
- *notebooks* — Jypiter Notebook с описанием проведения исследования
- *reports* -- отчеты по исследованию
- *scripts/* 
  - *load_data.py* -- скачивание данных с Kaggle в файл, заданный первым аргументом
  - *preprocessing.py* -- обработка csv заданного первым аргументом, на выходе создает в папке train.csv и test.csv
  - *fit.py* -- обучение модели случайного леса на выборке, заданной первым параметром, и в валидация на выборке, заданной вторым параметром; после обучения выводится точность и матрица ошибок, сохраняется файл модели model.joblib
  - *run.py* -- запускает пайплайн скачивания данных, процессинга и обучения модели


## Запуск
Для получения файла модели
```sh
cd ./scripts
python3 ./run.py
```
