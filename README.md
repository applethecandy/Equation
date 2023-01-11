# Equation
[![CI/CD GitHub Actions](https://github.com/applethecandy/Equation/actions/workflows/python-app.yml/badge.svg)](https://github.com/applethecandy/Equation/actions/workflows/python-app.yml)
[![Coverage Status](https://coveralls.io/repos/github/applethecandy/Equation/badge.svg?branch=main)](https://coveralls.io/github/applethecandy/Equation?branch=main)

## План тестирования:
1. Объект тестирования: функция, вычисляющая корни квадратного уравнения.
2. Необходимо протестировать:
    - Выдачу верных корней при положительном дискриминанте
    - Выдачу верных корней при нулевом дискриминанте
    - Отсутствие корней при отрицательном дискриминанте
3. Используемые виды тестирования:
    - Юнит тесты (тестирование выдачи верных корней)
    - Автоматическое тестирование (github actions)
    - Оценка покрытия кода тестами (coveralls.io)
    - Статическое тестирование (sonarcloud.io)
4. Проведение работ:
    - подготовка
    - тестирование
    - анализ результатов
5. Критерии начала тестирования:
    - готовность функции к тестированию
    - работоспособность функции
6. Критерии окончания тестирования:
    - разработка функции закончена
    - результаты тестирования удовлетворительны
