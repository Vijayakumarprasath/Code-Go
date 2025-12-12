rm -rf ~/airflow_venv
rm -rf ~/airflow


sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt update
sudo apt install python3.9 python3.9-venv python3.9-dev -y


python3.9 -m venv airflow_venv
source airflow_venv/bin/activate


sudo apt install build-essential libssl-dev libffi-dev libpq-dev -y
pip install --upgrade pip setuptools wheel

export AIRFLOW_VERSION=2.6.2
export PYTHON_VERSION=3.9
export CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"

pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"

export AIRFLOW_HOME=~/airflow
airflow db init
airflow webserver --port 8085


airflow scheduler


source ~/airflow_venv/bin/activate

export AIRFLOW_HOME=~/airflow


airflow scheduler



import pymysql
import pandas as pd
from datetime import datetime
import os

def fetch_data_from_mysql():
    mysql_config = {
        'host': 'localhost',
        'user': 'root',
        'password': '1234',
        'database': 'etl_example'
    }

    connection = pymysql.connect(**mysql_config)
    query = 'SELECT * FROM sample_data'
    df = pd.read_sql(query, connection)
    connection.close()
    return df

def transform_data(df):
    df_transformed = df[df['age'] > 30]
    return df_transformed

def write_data_to_file(df):
    output_dir = '/home/vijay/extract'
    os.makedirs(output_dir, exist_ok=True)
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    file_name = f'etl_output_{timestamp}.csv'
    file_path = os.path.join(output_dir, file_name)
    df.to_csv(file_path, index=False)
    print(f'Data written to {file_path}')

def etl_process():
    df = fetch_data_from_mysql()
    df_transformed = transform_data(df)
    write_data_to_file(df_transformed)

if __name__ == "__main__":
    etl_process()