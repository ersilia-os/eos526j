FROM bentoml/model-server:0.11.0-py311
MAINTAINER ersilia

RUN pip install ipywidgets==7.8.5
RUN pip install jinja2==3.1.6
RUN pip install jupyter==1.1.1
RUN pip install jupytext==1.17.0
RUN pip install notebook==6.5.7
RUN pip install networkx==2.8.8
RUN pip install deprecated==1.2.18
RUN pip install pandas==1.5.3
RUN pip install pillow==9.5.0
RUN pip install requests==2.32.3
RUN pip install rdchiral==1.1.0
RUN pip install rdkit==2023.9.6
RUN pip install tables==3.10.1
RUN pip install tqdm==4.67.1
RUN pip install onnxruntime==1.16.3
RUN pip install matplotlib==3.10.1
RUN pip install paretoset==1.2.4
RUN pip install seaborn==0.13.2
RUN pip install numpy==1.26.4


WORKDIR /repo
COPY . /repo