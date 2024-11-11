{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "415eb5aa-600f-4f0e-bb32-12c713593175",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "# pesquisar google dados gov dados publicos\n",
    "# https://dados.gov.br/dados/conjuntos-dados\n",
    "# Defesa e segurança Formato Json > Recursos\n",
    "# https://dados.gov.br/dados/conjuntos-dados/ocorrncias-aeronuticas"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "160e5382-b237-4673-b19b-4fee3c095827",
     "showTitle": false,
     "title": ""
    }
   },
   "source": [
    "#####Sites\n",
    "https://jsonviewer.stack.hu/\n",
    "\n",
    "https://codebeautify.org/jsonviewer\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "c949475d-2411-449d-a9e8-461f89022627",
     "showTitle": false,
     "title": ""
    }
   },
   "source": [
    "#####Ler um arquivo json\n",
    "https://spark.apache.org/docs/latest/sql-data-sources-json.html"
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
     "nuid": "c282ccce-d940-4362-bff8-5e9ef3b38dcf",
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
   "cell_type": "markdown",
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "d603a1e2-51d7-4fd7-8bb2-ba6797db84aa",
     "showTitle": false,
     "title": ""
    }
   },
   "source": [
    "##### Renomear Colunas"
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
     "nuid": "a7cbc6ee-200f-4773-a2a7-6968b082956c",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "#Renomear colunas caso necessário , obs eu subresqcrevi o df original , poderiar criar um novo passando outro nome no inio\\\n",
    "    #df_novo = df.withCo...................... e por ai vai \n",
    "        \n",
    "df = df.withColumnRenamed(\"Aerodromo_de_Destino\",\"Destino\") \\\n",
    "            .withColumnRenamed(\"Aerodromo_de_Origem\", \"Origem\")\\\n",
    "            .withColumnRenamed(\"Classificacao_da_Ocorrência\",\"Classificação\") \n",
    "display (df)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "4a22ad1d-0d10-455e-8591-13b51946b7b0",
     "showTitle": false,
     "title": ""
    }
   },
   "source": [
    "#####Salvar arquivo json zipado"
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
     "nuid": "78176006-7eb7-4af1-96af-6832d0e343af",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    " # write = Escrever\\Gravar |||   Read = Ler\n",
    "df.write \\\n",
    "    .format(\"json\") \\\n",
    "    .option(\"compression\", \"gzip\") \\\n",
    "    .mode(\"overwrite\") \\\n",
    "    .save(\"/FileStore/tables/Anac/json_zip\")\n"
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
     "nuid": "1784362d-4f42-4536-aeca-e8489a3c6e04",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "display(dbutils.fs.ls(\"/FileStore/tables/Anac\"))\n",
    "#json 20 MB\n",
    "#Json compromido 3 MB\n",
    "#pesquisar no google por conversor de bytes para mb mais basicamente 1 milhao de Byte = 1 Megabyte"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "53573172-2c91-400e-920e-9dd34a3b4d11",
     "showTitle": false,
     "title": ""
    }
   },
   "source": [
    "##### Lendo Json Compactado"
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
     "nuid": "cda6873d-0332-445b-bf7d-05c5a8175a97",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    " # write = Escrever\\Gravar |||   Read = Ler\n",
    "dfCompresao = spark.read \\\n",
    "        .option(\"compression\", \"gzip\") \\\n",
    "        .json(\"/FileStore/tables/Anac/json_zip/\") \n",
    "\n",
    "display(dfCompresao)"
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
     "nuid": "ce549cdb-e217-4ad6-9be1-89cd784e17fe",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "#Obs poderia passar o caminho do arquivo em uma variavel\n",
    "Caminho=\"/FileStore/tables/Anac/json_zip/\"\n",
    "df = spark.read \\\n",
    "        .option(\"compression\", \"gzip\") \\\n",
    "        .json(Caminho) \n",
    "\n",
    "display(df)"
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
   "notebookName": "05. Arquivos Json",
   "widgets": {}
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
