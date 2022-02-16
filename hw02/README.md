Вот ссылка на пакет: https://pypi.org/project/drawfunction/

```
sudo docker build -t latex_generation .
sudo docker run -it --name latex_generation_container -v "$(pwd)/artifacts:/playground/artifacts" latex_generation
```
