FROM python:3.9-slim
WORKDIR /playground
COPY main.py main.py
RUN mkdir -p /app/artifacts
RUN python3 -m pip install -i https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple drawfunction==1.0.6
RUN apt update
RUN apt install -y texlive
RUN apt install -y graphviz

CMD python3 /playground/main.py
