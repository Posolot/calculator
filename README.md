# Calculator

Простая утилита для выполнения арифметических операций.

## Установка

1. Сначала склонируйте репозиторий на вашем компьютере с помощью команды:

    ```bash
    git clone https://github.com/Posolot/calculator.git
    ```

2. Перейдите в каталог с проектом:

    ```bash
    cd calculator
    ```

3. Установите утилиту с помощью `setup.py`:

    ```bash
    python setup.py install
    //pip install .
    ```

## Использование

После установки утилиты, вы можете вызвать её.

Пример использования:
```bash
cd main
python calculator.py
```

Утилита предложит выбрать операцию (сложение, вычитание, умножение или деление), а затем попросит ввести два числа.

## Тестирование

Для запуска тестов, установите дополнительные зависимости из файла `requirements.txt`:

```bash
pip install -r requirements.txt
```

Затем запустите тесты с помощью `pytest`:

```bash
pytest
```

## Автор

[Posolot](https://github.com/Posolot)

