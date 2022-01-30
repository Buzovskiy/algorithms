# Мои алгоритмы
Алгоритмы находятся в папке app
### Запуск тестов
Для запуска всех тестов в коммандной строке в корне приложения вызвать модуль `unittest`
```
python -m unittest
```
Запуск тестов в одного файла, например (если в файле есть вызов unittest.main())
```
python -m test.test_fibonacci
```
Если нет вызова
```
python -m unittest test.test_fibonacci
```
Вызвать только один тест
```
python -m test.test_fibonacci TestFibonacci.test_fib
```


