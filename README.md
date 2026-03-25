# UI Automation Framework

Набор UI-тестов на Python + Pytest + Selenium (Page Object Model) для проверки логина и дальнейшего расширения тестов по разделам Dashboard / Investigations / Vessels.

## 1. Что внутри

- Язык: Python
- Тест-раннер: Pytest
- UI-автоматизация: Selenium WebDriver
- Паттерн: Page Object Model
- Конфигурация тестовых пользователей: `env.data.yml`

Текущие активные тесты:
- `tests/test_login.py`

Заготовки под следующие тесты:
- `tests/test_dashboard.py`
- `tests/test_investigations.py`
- `tests/test_vessels.py`

## 2. Системные требования

- Python 3.10+
- Google Chrome (последняя стабильная версия)
- Git
- Доступ в интернет для установки зависимостей

Почему 3.10+: в `requirements.txt` есть зафиксированные версии пакетов, которые не поддерживают Python 3.9.

## 3. Установка с нуля

### 3.1. Клонирование репозитория

```bash
git clone <URL_ВАШЕГО_РЕПО>
cd ui_automation_project
```

### 3.2. Создание виртуального окружения

macOS / Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows (PowerShell):

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3.3. Обновление pip и установка зависимостей

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 3.4. Проверка установки

```bash
python -m pytest --collect-only tests
```

Ожидаемый результат: тесты успешно обнаруживаются (без ImportError).

## 4. Подготовка тестовых данных

Файл `env.data.yml` содержит логины/пароли для тестов:

```yaml
urls:
  login: "url_login"

users:
  user_1:
    login: "login"
    password: "password"
  user_2:
    login: "login"
    password: "password"
```

Перед запуском:
- укажите актуальные тестовые учётные данные;
- убедитесь, что эти пользователи существуют в тестовом окружении.

## 5. Запуск тестов

Все тесты:

```bash
python -m pytest tests -v
```

Только логин-тесты:

```bash
python -m pytest tests/test_login.py -v
```

Запуск по маркеру `ui`:

```bash
python -m pytest -m ui -v
```

## 6. Как устроен проект

```text
conftest.py                    # фикстуры pytest (driver, env_data)
env.data.yml                   # тестовые данные (логины/пароли)
requirements.txt               # зависимости

tests/
  test_login.py                # тесты логина
  test_dashboard.py            # заготовка
  test_investigations.py       # заготовка
  test_vessels.py              # заготовка

ui/pages/
  login_page/
    base_element.py            # базовая обертка над WebElement
    locators.py                # локаторы страницы логина
    login_page.py              # Page Object для логина
```

## 7. Важные технические моменты

- В `conftest.py` используется `webdriver.Chrome(...)`.
- Начиная с Selenium 4, Selenium Manager автоматически подбирает драйвер Chrome в большинстве случаев.
- Если запуск на CI или сервере без UI, добавьте headless-настройку в фикстуру `driver`.

## 8. Частые проблемы и решения

### Ошибка: `ModuleNotFoundError: No module named 'yaml'`

Причина: не установлены зависимости в активном окружении.

Решение:

```bash
pip install -r requirements.txt
```

И проверьте, что вы запускаете pytest тем же Python, где ставили пакеты:

```bash
python -m pytest tests -v
```

### Ошибка версий пакетов (Requires-Python)

Причина: используется Python 3.9 или ниже.

Решение: создайте окружение на Python 3.10+ и переустановите зависимости.

### Предупреждение `PytestUnknownMarkWarning: Unknown pytest.mark.ui`

Это предупреждение о незарегистрированном маркере.

Рекомендуется добавить `pytest.ini`:

```ini
[pytest]
markers =
    ui: UI tests
```

## 9. Рекомендации по развитию

- Добавить `pytest.ini` (регистрация маркеров, общие опции).
- Добавить отчётность (`pytest-html` или Allure).
- Вынести URL и окружения в отдельный конфиг.
- Разделить smoke/regression маркеры.
- Добавить поддержку headless-режима через переменную окружения.

