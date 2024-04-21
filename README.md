# D-building-4.1
# Голосовой банковский ассистент

Добро пожаловать в репозиторий проекта "Голосовой банковский ассистент" команды D-building 4.1! 

## Описание

Наш проект представляет собой голосового ассистента, специализированного на обслуживании банковских клиентов. Ассистент обеспечивает пользователей информацией о балансе счетов, последних операциях, переводах и других банковских услугах.

## Файловая система

api/app.py - основной файл бэкенда
`python app.py`
api/requirements.txt - зависимости бэкенда
`pip install -r requirements.txt`

## Реализация бэкенда

Архитектура бэкенда:
Фреймворк Flask  
Для работы с базой данных PostGRE используется SQLAlchemy, что обеспечивает удобство и безопасность операций с базой данных.  
Выбрана архитектура REST API  

Основные черты и преимущества:  
Модульность: Бэкенд реализует архитектуру MVC, представлены модели и контроллеры.  
Работа с аудио: Есть функционал конвертации текста в аудио с помощью нейросети и из аудио в текст  
