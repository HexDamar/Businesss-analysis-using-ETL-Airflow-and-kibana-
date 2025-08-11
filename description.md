# Judul Project
## Preprocessing data using ETL Pipeline

---

## Repository Outline

  ```
  |
  ├── description.md --> berisi keterangan tentang project yang dikerjakan 
  ├── P2M3_Nugroho_Wicaksono_ddl.txt --> berisi query untuk memasukkan data raw ke dalam postgre
  ├── P2M3_Nugroho_Wicaksono_data_raw.csv --> berisi data raw hasil ektraksi dari proses ETL
  ├── P2M3_Nugroho_Wicaksono_data_clean.csv --> berisi data clean hasil cleaning dari proses ETL
  ├── P2M3_Nugroho_Wicaksono_DAG.py --> berisi proses ETL pipeline
  ├── P2M3_Nugroho_Wicaksono_DAG_graph.png --> berisi graph jalan kerja DAG yang dibuat
  ├── P2M3_Nugroho_Wicaksono_conceptual.txt --> menjawab pertanyaan conceptual yang diberikan berkaitan denga project 
  ├── P2M3_Nugroho_Wicaksono_GX.ipynb --> berisi proses validasi data menggunakan greater expectation
  ├── P2M3_Nugroho_Wicaksono_GX_Results.png --> gambar hasil dari proses validasi.
  ├── README.md --> berisi rubriks dan cara pengerjaan project
  ├── /images --> berisi gambar EDA untuk keperluan analysis
        ├── introduction & objective.png --> berisi perkenalan dan objektif dari analysis yang dilakukan 
        ├── plot & insight 01.png --> analysis menggunakan visual plot 
        ├── plot & insight 02.png --> analysis menggunakan visual plot 
        ├── plot & insight 03.png --> analysis menggunakan visual plot 
        ├── plot & insight 04.png --> analysis menggunakan visual plot 
        ├── plot & insight 05.png --> analysis menggunakan visual plot 
        ├── plot & insight 06.png --> analysis menggunakan visual plot 
        └── kesimpulan.png --> berisi kesimpulan dari analysis menggunakan plot 
  ```
    
---
## Problem Background

```
Perkembangan teknologi informasi dan komunikasi telah membawa perubahan besar dalam pola hidup dan kebutuhan masyarakat global. Perangkat komputasi seperti kini menjadi bagian penting dalam menunjang berbagai aktivitas, mulai dari pendidikan, pekerjaan, hingga hiburan. Kemampuan untuk menjalankan aplikasi kompleks, bekerja secara mobile, dan mengakses layanan berbasis internet menjadikan perangkat ini semakin dibutuhkan di berbagai sektor.
Namun, meskipun kebutuhan terhadap laptop dan PC masih tinggi, pasar perangkat komputer menunjukkan dinamika yang semakin kompleks. Menurut laporan dari Gartner (2024), terjadi fluktuasi dalam tren penjualan global, dengan segmen tertentu seperti laptop gaming dan ultrabook masih mengalami pertumbuhan, sementara perangkat desktop mengalami penurunan permintaan di beberapa wilayah 1. Selain itu, laporan dari Statista juga menunjukkan bahwa faktor seperti spesifikasi perangkat, harga, dan reputasi merek sangat memengaruhi keputusan konsumen dalam membeli laptop atau PC 2 

Tujuan :
Sebagai seorang data analyst di EBAY , tujuan utama dari analisis data penjualan laptop dan PC ini adalah untuk menghasilkan wawasan berbasis data yang dapat mendukung pengambilan keputusan strategis oleh pihak manajemen atau tim bisnis. Secara khusus, analisis ini bertujuan untuk:
1.	Mengidentifikasi tren penjualan berdasarkan waktu (bulanan, kuartalan, tahunan) guna memahami pola fluktuasi permintaan terhadap laptop dan PC.
2.	Menganalisis performa penjualan berdasarkan kategori produk seperti tipe perangkat (laptop vs desktop), merek, seri/model, dan rentang harga.
3.	Mengevaluasi segmentasi pasar berdasarkan perilaku konsumen, seperti kelompok usia, lokasi geografis, dan jenis penggunaan (pendidikan, profesional, gaming, dll).
```
---
## Project Output
```
hasil akhir project ini menghasilkan 
1. DAG structure airflow scheduler untuk ekstrak data , olah data dan visualisasikan data.
2. hasil analisa dan visualisasi dari dataset untuk keperluan business insight.
3. analisa menggunakan Greater_expectations untuk menmvalidasi data yang sudah clean.  

```
---
## Data
```
data yang diambil memiliki info sebagai berikut:
1. dataset diambil dari website kaggle 
setelah dilakukan cleaning 
1. jumlah baris ada +-500
2. terdapat 25 kolom
3. terdapat 6 float, 1 int, dan 18 object data type
```
---
## Method
```
metode utama yang dilakukan di project ini antara lain:
1. ETL pipeline
melakukan pengambilan data dari postgre, proses data, lalu load ke elastic-kibana
2. validation
menggunakan Greater expectation untuk memvalidasi data setelah data di clean
3. visualisation
menggunakan elastic-kibana untuk menampilkan plot hasil analisa untuk keperluan business insight
```
---
## Stacks
```
Bahasa pemrograman:
1. python 
2. SQL query
3. pandas

tools yang digunakan:
1. visual studio code
2. elastic kibana
3. airflow webserver
4. postgre
```

library yang digunakan :
```python

import pandas as pd
from datetime import datetime
from sqlalchemy import create_engine
from airflow import DAG
from airflow.decorators import task
from airflow.operators.empty import EmptyOperator
from airflow.models import Variable

from elasticsearch import Elasticsearch

# Import Libraries
import pandas as pd
import great_expectations as gx 
from great_expectations.checkpoint import Checkpoint
from great_expectations.core.batch import RuntimeBatchRequest
```
---


## Reference
https://greatexpectations.io/expectations/