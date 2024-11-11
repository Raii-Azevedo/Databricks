{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "451c49b8-fbc8-4664-a602-cab84d85088a",
     "showTitle": false,
     "title": ""
    }
   },
   "source": [
    "#####Documentação Databricks\n",
    "https://docs.databricks.com/pt/external-data/parquet.html\n",
    "\n",
    "#####Documentação Spark\n",
    "https://spark.apache.org/docs/latest/sql-data-sources-parquet.html\n",
    "\n",
    "Pesquisar no google Parquet Documentação (databricks ou Spark)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "14ed0959-7ba2-4351-9dc7-bb77484a103d",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "#Curiosidades comparado com CSV e Json\n",
    "\"\"\"\n",
    "80% (Aprox) menos armazenamento ao comparar com CSV e Json\n",
    "30x (Aprox) Mais Rápido\n",
    "90% (Aprox) Economia na leitura agiliza o cluster isso resulta em leituras e gravações mais rápidas.\n",
    "Pode ser particionado\n",
    "Quanto menor tamando de armazenamento menos dinheiro a empresa paga em recursos Cloud\n",
    "Pesquise no google , comparação arquivo parquet com CSV \n",
    "\"\"\"\n",
    "\n",
    "#Será que é isso tudo mesmo ? Vamos  ver na pratica"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "7d8c71ee-7fc7-4f7f-a248-374aff59c842",
     "showTitle": false,
     "title": ""
    }
   },
   "source": [
    "######Transformando DataFlame em Parquet\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "e28a75e3-8fa4-4e40-bcca-6930173bb3cd",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "df = spark.read.json(\"dbfs:/FileStore/tables/Anac/V_OCORRENCIA_AMPLA.json\")\n",
    "display(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "352756c3-6ef3-43ed-8767-c410197163ad",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "df.write \\\n",
    "  .format('parquet') \\\n",
    "  .mode(\"overwrite\") \\\n",
    "  .save(\"/FileStore/tables/Anac/V_OCORRENCIA_AMPLAParquet\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "3b113985-97b8-4d88-ad50-7d8b45d431d8",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "#Código em unica linha \n",
    "#df.write.format('parquet').mode(\"overwrite\").save(\"/FileStore/tables/Anac/V_OCORRENCIA_AMPLAParquet\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "ca44cb28-1e81-41b4-9fd3-1f4cc88f2396",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "display(dbutils.fs.ls(\"/FileStore/tables/Anac\"))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "58e6c430-7941-45c1-ae00-8bd700c21265",
     "showTitle": false,
     "title": ""
    }
   },
   "source": [
    "###### Alterando nome do arquivo"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "1b98869a-d4b6-44e3-828a-1b5a5f5d9752",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "#Arquivo antigo =   dbfs:/FileStore/tables/Anac/V_OCORRENCIA_AMPLA-zip/\n",
    "\n",
    "#dbutils.fs.mv(\"/FileStore/tables/Anac/V_OCORRENCIA_AMPLA-zip\", \"/FileStore/tables/Anac/csv_zip\" , recurse = True)\n",
    "\n",
    "# dbutils.fs.mv + arquivo caminho completo do que qer mudaro nome + caminho como novo nome  + recurse=True para alterar tudo dentro da pasta que for nescessário\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "9483489f-856b-40e3-87c0-f9c142baa075",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "display(dbutils.fs.ls(\"/FileStore/tables/Anac/V_OCORRENCIA_AMPLAParquet/\"))\n",
    "#por padrão ele ja vem compactado na estensão snappy"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "b7f544a7-55bc-406c-9563-07b7ef6b38e7",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "#csv =     9869805  Bytes  9MB\n",
    "#json=     20436383 Bytes  20MB\n",
    "#parquet = 3308863  Bytes  3MB\n",
    "\n",
    "#Da para melhorar ainda mais?posso ser promovido por isso? pense em grande escala de economia 20 mil por mes ou 3 mil por mes qual melhor?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "9da11085-106f-4228-91d7-3633cb4d1769",
     "showTitle": false,
     "title": ""
    }
   },
   "source": [
    "###### lendo arquivo Parquet"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "6c0a508b-3ad0-46af-a519-f52a15ce7ad5",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "dfpq = spark.read.parquet(\"/FileStore/tables/Anac/V_OCORRENCIA_AMPLAParquet\")\n",
    "display(dfpq)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "fb86efc1-2c9f-4cc2-8230-c66b85f7a4c1",
     "showTitle": false,
     "title": ""
    }
   },
   "source": [
    "Salvando parquet com Compactado"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "b5faf44a-8e8e-44d0-8a8d-bd2cc5cf325d",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "df.write \\\n",
    "  .format('parquet') \\\n",
    "  .mode(\"overwrite\") \\\n",
    "  .option(\"compression\", \"gzip\") \\\n",
    "  .save(\"/FileStore/tables/Anac/Parquet_zip\")\n",
    "# pegai o mesmo script para salvar apenas inseri  option de compression\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "bb481bc4-2e45-41c2-b155-6d3d44211fe9",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "display(dbutils.fs.ls(\"/FileStore/tables/Anac\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "52a2ad75-c41d-4869-b060-09a33f9149b3",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "display(dbutils.fs.ls(\"dbfs:/FileStore/tables/Anac/Parquet_zip/\"))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "4df4d384-e5f1-4db2-9885-c9088903899b",
     "showTitle": false,
     "title": ""
    }
   },
   "source": [
    "###### Lendo Arquivo Parquet compactado\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "b62222c1-36c1-4582-a6f9-a531a65afa1e",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "dfParquetZip = spark.read\\\n",
    "    .format(\"parquet\")\\\n",
    "    .option(\"compression\", \"gzip\")\\\n",
    "    .load(\"dbfs:/FileStore/tables/Anac/Parquet_zip\")\n",
    "display(dfParquetZip)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "08adb06f-05d0-4f2b-a099-789a3323666a",
     "showTitle": false,
     "title": ""
    }
   },
   "source": [
    "###### tempo de Execução parquet x json"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "90a14761-37b3-4561-84ce-b4ca04d09868",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "#Json\n",
    "df_json = spark.read.json(\"dbfs:/FileStore/tables/Anac/V_OCORRENCIA_AMPLA.json\")\n",
    "display(df_json)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "c27776ee-fb58-43ff-a166-d747a93e2c3a",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "#parquet\n",
    "dfpq = spark.read.parquet(\"/FileStore/tables/Anac/V_OCORRENCIA_AMPLAParquet\")\n",
    "display(dfpq)\n"
   ]
  }
 ],
 "metadata": {
  "application/vnd.databricks.v1+notebook": {
   "dashboards": [],
   "language": "python",
   "notebookMetadata": {
    "pythonIndentUnit": 4
   },
   "notebookName": "06. Arquivo Parquet",
   "widgets": {}
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
