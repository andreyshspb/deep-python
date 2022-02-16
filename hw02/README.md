* Вот ссылка на пакет: https://pypi.org/project/drawfunction/

* Сборка образа:
```shell
docker build -t latex_generation .
```

* Запуск пакета:
```shell
sudo docker run -it -v "$(pwd)/artifacts:/playground/artifacts" latex_generation
```
