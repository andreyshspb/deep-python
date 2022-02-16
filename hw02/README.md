```
sudo docker build -t latex_generation .
sudo docker run -it --name latex_generation_container -v "$(pwd)/artifacts:/playground/artifacts" latex_generation
```
## [PyPi Repository](https://pypi.org/project/drawfunction/)
