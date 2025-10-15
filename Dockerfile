FROM python:3.10

RUN apt-get update && apt-get install -y git 
RUN apt install -y qt6-base-dev && apt-get install -y libxcb-cursor-dev

RUN pip install PySide6 && pip install pyqtgraph
