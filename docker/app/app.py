# type: ignore
import json
import sys
import boto3
from osgeo import gdal
import geopandas
import psycopg2 
from subprocess import run, PIPE, call

def handler(event, context):
    
    cmd = run(
        ['ogr2ogr'],
        stdout=PIPE, stderr=PIPE, universal_newlines=True)
    print("Error:: ", cmd.stderr)
    print("Out:: ", cmd.stdout)

    msg = (
        "Run from Dockerized Container with "
        f"Python {sys.version}, "
        f"Boto3 {boto3.__version__}, "
        f"GDAL {gdal.__version__}, "
        f"GeoPandas {geopandas.__version__} "
        f"psycopg2 {psycopg2.__version__} "
        f"ls {cmd.stderr} {cmd.stdout}"
    )

    return msg 
