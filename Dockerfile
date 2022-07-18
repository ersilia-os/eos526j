FROM bentoml/model-server:0.11.0-py37
MAINTAINER ersilia

RUN conda install -c conda-forge rdkit=2021.03.4
RUN conda install -c anaconda pymongo
RUN conda install -c conda-forge tensorflow
RUN conda install -c anaconda networkx
RUN conda install -c anaconda jinja2
RUN conda install tqdm
RUN conda install pyyaml
RUN conda install pytables==3.7.0

RUN pip install scikit-learn
RUN pip install rdchiral
RUN pip install tensorflow_serving_api
RUN pip install https://github.com/MolecularAI/route-distances/archive/refs/tags/v0.2.0.tar.gz



WORKDIR /repo
COPY . /repo
