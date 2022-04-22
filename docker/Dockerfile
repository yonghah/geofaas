ARG FUNCTION_DIR="/function"

FROM osgeo/gdal:ubuntu-small-latest as build-image
# gdal/ogr binaries are located at /usr/bin

RUN apt-get update && \
  apt-get install -y \
  g++ \
  make \
  cmake \
  unzip \
  libcurl4-openssl-dev

ARG FUNCTION_DIR
RUN mkdir -p ${FUNCTION_DIR}

RUN apt-get update && apt-get install -y software-properties-common gcc && \
    add-apt-repository -y ppa:deadsnakes/ppa
RUN apt-get update && apt-get install -y \
    python3.8 python3-distutils python3-pip python3-apt libpq-dev 

RUN python3 -m pip install --target ${FUNCTION_DIR} boto3 
RUN python3 -m pip install --target ${FUNCTION_DIR} awslambdaric
RUN python3 -m pip install --target ${FUNCTION_DIR} geopandas
RUN python3 -m pip install --target ${FUNCTION_DIR} psycopg2 

FROM osgeo/gdal:ubuntu-small-latest

ARG FUNCTION_DIR
WORKDIR ${FUNCTION_DIR}

# setup lambda run time emulator
COPY --from=build-image ${FUNCTION_DIR} ${LAMBDA_TASK_ROOT}
COPY ./entry_script.sh /entry_script.sh
ADD aws-lambda-rie /usr/local/bin/aws-lambda-rie
RUN ["chmod", "+x", "/usr/local/bin/aws-lambda-rie"]

# COPY app/* ${FUNCTION_DIR}
COPY app/* ${LAMBDA_TASK_ROOT}

ENTRYPOINT [ "/entry_script.sh" ]
CMD [ "app.handler" ]
