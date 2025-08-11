
"""
========================================================================
Nugroho Wicaksono
HCK 029


Kode ini mendefinisikan sebuah **DAG (Directed Acyclic Graph)** di Apache Airflow bernama `etl_csv_files` yang bertujuan untuk mengotomatisasi proses **ETL (Extract, Transform, Load)** dari data CSV yang diambil dari PostgreSQL, diproses (dibersihkan), dan kemudian dimuat ke Elasticsearch. Alur kerja ini dijadwalkan berjalan setiap hari Sabtu pada pukul 09:10, 09:20, dan 09:30, dan terdiri dari tiga tugas utama:

1. **Extract**: Mengambil data dari database PostgreSQL dan menyimpannya sebagai file CSV.
2. **Transform (Preprocessing)**: Melakukan pembersihan data, seperti menghapus nilai kosong, duplikat, dan standarisasi nama kolom.
3. **Load**: Memuat data yang sudah dibersihkan ke dalam indeks Elasticsearch.

Proses ini berguna dalam pipeline data modern untuk memastikan data siap digunakan untuk keperluan analisis lebih lanjut atau pencarian cepat menggunakan Elasticsearch.
=========================================================================
"""




import pandas as pd
from datetime import datetime
from sqlalchemy import create_engine
from airflow import DAG
from airflow.decorators import task
from airflow.operators.empty import EmptyOperator
from airflow.models import Variable

from elasticsearch import Elasticsearch




default_args= {
    'owner': 'Damar',
    'start_date': datetime(2024, 11, 1)  # Start date diubah ke 1 November 2024
}

with DAG(
    'etl_csv_files',
    description='from gdrive to postgres',
    schedule_interval='10,20,30 9 * * 6',
    default_args=default_args, 
    catchup=False) as dag:

    start = EmptyOperator(task_id='start')
    
    """
    =======================================================================================
    # Konfigurasi DAG Airflow: `etl_csv_files`

    - **Nama DAG**: `etl_csv_files`  
    Nama ini akan muncul di Airflow UI sebagai identitas DAG.

    - **Deskripsi**: `'from gdrive to postgres'`  
    Menjelaskan bahwa alur kerja ini bertugas memindahkan data dari Google Drive ke PostgreSQL.

    - **Jadwal Eksekusi**: `'10,20,30 9 * * 6'`  
    DAG ini akan berjalan:
    - **Hari**: Setiap hari **Sabtu** (`6`)
    - **Jam**: Pada pukul **09:10**, **09:20**, dan **09:30** (waktu server)

    - **Parameter Default**: `default_args`  
    Berisi konfigurasi seperti `start_date`, `email`, `retries`, dan lainnya (tidak ditampilkan dalam potongan ini).

    - **catchup**: `False`  
    Menonaktifkan eksekusi otomatis untuk jadwal yang terlewat (backfill), sehingga DAG hanya berjalan untuk jadwal yang akan datang.
    =======================================================================================

    """


    @task()
    def extract_from_db():
        database = "airflow"
        username = "airflow"
        password = "airflow"
        host = "host.docker.internal"
        port = "5434"

        postgres_url = f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}"

        engine = create_engine(postgres_url)
        conn = engine.connect()


        # df = pd.read_csv('/opt/airflow/data/data_combine_preprocessed.csv')
        df = pd.read_sql('select * from table_m3',conn)
        print("Success READ")

        # df.to_sql('data_customer', conn, index=False, if_exists='replace')
        #  .... isi nama csv data kita 
        df.to_csv('/opt/airflow/data/P2M3_Nugroho_wicaksono_data_raw.csv', index=False) 
        print("Success EXTRACT")

        ## Penjelasan Fungsi `extract_from_db`
    """
    ======================================================================================================
    Fungsi ini menjalankan proses **Extract** dalam pipeline ETL, dengan langkah-langkah berikut:

    - **Mendefinisikan Parameter Koneksi Database**:
    - **Database**: `airflow`
    - **Username**: `airflow`
    - **Password**: `airflow`
    - **Host**: `host.docker.internal` (digunakan untuk koneksi antar kontainer Docker)
    - **Port**: `5434`

    - **Membuat URL Koneksi PostgreSQL**:
    - Format: `postgresql+psycopg2://<username>:<password>@<host>:<port>/<database>`

    - **Membuat SQLAlchemy Engine dan Koneksi ke Database**:
    - Menggunakan `create_engine` dari SQLAlchemy
    - Membuka koneksi menggunakan `engine.connect()`

    - **Mengekstrak Data dari Tabel PostgreSQL**:
    - Menggunakan perintah SQL `SELECT * FROM table_m3`
    - Hasil query disimpan ke dalam `pandas.DataFrame`

    - **Menampilkan Status Keberhasilan**:
    - Mencetak `"Success READ"` setelah data berhasil dibaca dari database

    - **Menyimpan Data ke File CSV**:
    - Path file: `/opt/airflow/data/P2M3_Nugroho_wicaksono_data_raw.csv`
    - Parameter `index=False` digunakan agar indeks DataFrame tidak ikut disimpan

    - **Menampilkan Status Keberhasilan**:
    - Mencetak `"Success EXTRACT"` setelah data berhasil diekspor ke CSV
    ======================================================================================================

    """

    @task()
    def preprocess_data():
        #  .... isi nama csv data kita 
        df = pd.read_csv('/opt/airflow/data/P2M3_Nugroho_wicaksono_data_raw.csv')
        
        # handling missing value 
        df = df.dropna().reset_index(drop=True)

        # handling duplicates
        df = df.drop_duplicates().reset_index(drop=True)

        # handling coloumn name
        df.columns = df.columns.str.strip().str.lower().str.replace(r'[\s/()]+', '_', regex=True)

        # Any other preprocessing steps can be added here

        print("Preprocessed data is Success")
        df.to_csv('/opt/airflow/data/P2M3_Nugroho_wicaksono_data_clean.csv', index=False)

    """
    ======================================================================================================

    # Data Cleaning: Raw to Clean CSV

    ## 1. Membaca Data Mentah
    - Membaca file CSV mentah yang merupakan hasil dari proses ekstraksi sebelumnya.
    - Format data: `.csv`

    ## 2. Penanganan Missing Values
    - Menghapus seluruh baris yang memiliki nilai kosong (`NaN`) menggunakan `dropna()`.
    - Mengatur ulang index dengan `reset_index(drop=True)` agar index lama tidak disimpan.

    ## 3. Penanganan Data Duplikat
    - Menghapus baris-baris duplikat menggunakan `drop_duplicates()`.
    - Mengatur ulang kembali index setelah penghapusan duplikat.

    ## 4. Standardisasi Nama Kolom
    - `strip()`: Menghapus spasi di awal dan akhir nama kolom.
    - `lower()`: Mengubah semua nama kolom menjadi huruf kecil.
    - `replace()`: Mengganti karakter seperti spasi, garis miring (`/`), dan tanda kurung (`()`) dengan garis bawah (`_`).
    - Contoh: `"Customer Name"` → `"customer_name"`

    ## 5. Penyimpanan Hasil
    - Menyimpan dataframe hasil pembersihan ke dalam file CSV baru.
    - Parameter `index=False` digunakan agar index tidak ikut disimpan ke dalam file CSV.
    ======================================================================================================

    """


    @task()
    def load_to_elastic():

        es = Elasticsearch(["http://elasticsearch:9200"])

        df = pd.read_csv('/opt/airflow/data/P2M3_Nugroho_wicaksono_data_clean.csv')

        for i, row in df.iterrows():
            res = es.index(index='ebay', id=i+1, body=row.to_json())
            print(res)


    
    end = EmptyOperator(task_id='end')

    start >> extract_from_db( ) >> preprocess_data() >> load_to_elastic() >> end

    """
    ======================================================================================================

    # Fungsi: load_to_elastic()

    ## Deskripsi
    Fungsi ini bertanggung jawab untuk melakukan proses *indexing* data bersih ke dalam Elasticsearch sebagai salah satu tahap akhir pipeline.

    ## Detail Proses

    ### Dekorator
    - `@task()`: Mengubah fungsi Python menjadi Airflow Task untuk dijalankan dalam DAG.

    ### Koneksi Elasticsearch
    - Membuat koneksi ke instance Elasticsearch melalui URL: `http://elasticsearch:9200`, dengan asumsi service name berada di jaringan Docker yang sama.

    ### Membaca Data Bersih
    - Membaca file CSV hasil dari tahap preprocessing: `P2M3_Nugroho_wicaksono_data_clean.csv`.

    ### Proses Indexing ke Elasticsearch
    - Melakukan iterasi baris per baris menggunakan `df.iterrows()`.
    - Untuk setiap baris, data di-*index* ke Elasticsearch menggunakan:
    - `index='ebay'`: Nama index Elasticsearch.
    - `id=i+1`: ID unik dokumen dimulai dari 1.
    - `body=row.to_json()`: Data dikonversi ke format JSON.
    - `print(res)`: Menampilkan respons hasil indexing untuk keperluan monitoring.

    ---

    # Task Akhir dan Dependencies

    ## EmptyOperator
    - Task kosong dengan nama `'end'`, digunakan sebagai penanda akhir alur eksekusi DAG.

    ## Alur Eksekusi
    - Menyusun urutan task dalam pipeline sebagai berikut:

    - Menjamin eksekusi yang terstruktur dan berurutan sesuai dependensi antar task.

    ## Fungsi
    - Memberikan kejelasan struktur eksekusi dan batas logis antara tahap awal, tengah (transformasi & loading), dan akhir dalam workflow ETL.
    ======================================================================================================

    """
    