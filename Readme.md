# Решение команды 200 OK  
Трек 3: RAG - поисковые системы  

## Обзор  

Данный проект реализует один из способов работы с многомодельной архитектурой Retrieval-Augmented Generation (RAG). Приложение обрабатывает PDF-файл, извлекает релевантный контент с помощью Colpali и генерирует ответы, используя мультимодальную систему RAG. Процесс включает индексацию документа, выполнение запросов и суммаризацию с использованием визуальной модели Llama версии 3.2.  

## Мотивация  

Цель проекта — обеспечить эффективный поиск и генерацию контента из мультимодальных документов (PDF, DOCX, PPTX, содержащих текст и изображения) в ответ на запросы на естественном языке.  

### Преимущества  

- Поддержка мультимодальных данных: как текста, так и изображений.  
- Упрощённый процесс извлечения и суммаризации данных.  
- Гибкость в генерации контента с использованием передовых языковых моделей (Llama).  

## Реализация  

1. PDF-файл индексируется, после чего его содержимое разделяется на текстовые и графические сегменты.  
2. Выполняется запрос к проиндексированному документу для получения релевантных результатов.  
3. Извлечённое изображение кодируется и передаётся в модель Llama для генерации ответа.  

## Итог  

Проект объединяет индексацию документов, поиск и генерацию контента в мультимодальной среде, что позволяет эффективно работать с комплексными документами, такими как коммерческие отчёты.

## Пайплайн

![Static Image](http://d.zaix.ru/Km79.png)

## Демонстрация

<a href="https://gifyu.com/image/SJIDD"><img src="https://s7.gifyu.com/images/SJIDD.gif" alt="Colpali RAG demo ezgif.com speed" border="0" /></a>

![GIF Demo](https://s7.gifyu.com/images/SJIDD.gif)


## Cold Start
перед запуском загрузить тестовый датасет:
https://disk.yandex.com/d/5i24L_kpgaWYJA

и индекс:
https://disk.yandex.com/d/dF7eBlPtJs9GNA

файлики разархивировать в папку с проектом,
byaldi переименовать в .byaldi

```
streamlit run main.py
```

## Requirements

### Drivers & libs
```
Docker version 24.0.7, build afdd53b
NVIDIA Container Runtime Hook version 1.17.2
NVIDIA Driver Version: 535.113.01
CUDA Version: 12.2  
Linux COMP 6.2.0-33-generic #33~22.04.1-Ubuntu SMP PREEMPT_DYNAMIC Thu Sep  7 10:33:52 UTC 2 x86_64 x86_64 x86_64 GNU/Linux

```


### Hardware
 
```
Ryzen 1700
Ram: 16GB
GPU: RTX2070 8gb -> Colpali

GPU: RTX4090 24gb -> инференс LlaMA3.2

```



