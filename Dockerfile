FROM bentoml/model-server:0.11.0-py37
MAINTAINER ersilia

RUN conda install -c anaconda pymongo=3.12.0
RUN conda install -c anaconda networkx=2.2
RUN conda install -c anaconda jinja2=3.0.3
RUN conda install tqdm=4.64.0
RUN conda install pyyaml=6.0
RUN conda install -c conda-forge xorg-libxrender xorg-libxtst

RUN pip install rdkit==2023.3.1
RUN pip install pandas==1.3.5
RUN pip install tensorflow==2.9.1
RUN pip install rdchiral==1.1.0
RUN pip install tensorflow_serving_api==2.9.1
RUN pip install https://github.com/MolecularAI/route-distances/archive/refs/tags/v0.2.0.tar.gz


WORKDIR /repo
COPY . /repo
