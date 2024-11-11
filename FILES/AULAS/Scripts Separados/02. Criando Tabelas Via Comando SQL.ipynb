{
 "cells": [
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
     "nuid": "ede20b8a-9f2a-4882-9173-2e6cf95825a4",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "#Obs quando seu Cluster Desligar vai perder os dados do Banco de dados e tabelas criadas (Database Tables)\n",
    "# Dados do DBFS não sao perdidos"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "8aa963af-7eee-4b8d-826e-2baae7ac89e6",
     "showTitle": false,
     "title": ""
    }
   },
   "source": [
    "##### Criando Banco de dados "
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
     "nuid": "c98fe9a5-1270-4fc6-9a38-f5f1fc9f779d",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "display(dbutils.fs.ls('/FileStore/tables/Bikes/'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "implicitDf": true,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "29c0ae81-ebe1-4de0-9291-9702222e9d2a",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "%sql\n",
    "CREATE DATABASE IF NOT EXISTS Teste;\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "f3168ddb-640f-420b-9124-0e2169d64a31",
     "showTitle": false,
     "title": ""
    }
   },
   "source": [
    "##### Criando tabela de Produtos"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "implicitDf": true,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "a0af5ce0-b376-49ba-9657-d207e68d0b6e",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "%sql\n",
    "\n",
    "use teste;\n",
    "CREATE TABLE IF NOT EXISTS Produtos\n",
    "USING csv\n",
    "OPTIONS (\n",
    "  'path' '/FileStore/tables/Bikes/products.csv',  -- Caminho para o arquivo no DBFS\n",
    "  'header' 'true',                               -- Se a primeira linha do arquivo contém cabeçalho\n",
    "  'inferSchema' 'true'                           -- Inferir automaticamente os tipos de dados das colunas\n",
    ")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "implicitDf": true,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "82f4e886-1ee3-4fbb-9039-365878b433f3",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "%sql\n",
    "-- ver todos os dados \n",
    "use Teste;\n",
    "SELECT * FROM Produtos\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "implicitDf": true,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "94222a86-dee3-48bc-a2af-5c69630845ca",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "%sql\n",
    "use Teste;\n",
    "\n",
    "SELECT count(*) FROM Produtos"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "implicitDf": true,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "950b8924-3ded-45d4-b3e2-bd14813460e5",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "%sql\n",
    "-- Quantidade de Bikes por ano do modelo produzido \n",
    "select \n",
    "model_year as Ano\n",
    ",count(product_id) QNT\n",
    "from produtos\n",
    "group by model_year\n",
    "order by  QNT desc\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "d6de5a08-bf40-4dad-9276-5802ddbde014",
     "showTitle": false,
     "title": ""
    }
   },
   "source": [
    "##### Criando tabela de Clientes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "implicitDf": true,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "601d80d6-bb00-4848-9ce9-a1046f826187",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "%sql\n",
    "\n",
    "use Teste;\n",
    "CREATE TABLE IF NOT EXISTS Clientes\n",
    "USING csv\n",
    "OPTIONS (\n",
    "  'path' '/FileStore/tables/Bikes/customers.csv',  -- Caminho para o arquivo no DBFS\n",
    "  'header' 'true',                               -- Se a primeira linha do arquivo contém cabeçalho\n",
    "  'inferSchema' 'true'                           -- Inferir automaticamente os tipos de dados das colunas\n",
    ")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "implicitDf": true,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "34ac938e-bab8-40c1-b445-cd2e6eeccb9a",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "%sql\n",
    "use Teste;\n",
    "select * from Clientes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "implicitDf": true,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "2a162e28-8b34-47e3-ae80-70e9f128ebb2",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "%sql\n",
    "use Teste;\n",
    "--  quantos Clientes Por Estado\n",
    "select count(*) from clientes\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "implicitDf": true,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "067cace7-485b-448c-812c-632709095b41",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "%sql\n",
    "use Teste;\n",
    "--  quantos Clientes Por Estado\n",
    "select  \n",
    "count(customer_id) Quantidade\n",
    ",city as Cidade\n",
    "from clientes\n",
    "group by city\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "implicitDf": true,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "bcf447ac-378e-49d0-b8a9-f54711940ebd",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "%sql\n",
    "use Teste;\n",
    "--  quantos Clientes Por Estado\n",
    "select  \n",
    "state\n",
    ",count(customer_id) Quantidade\n",
    "from clientes\n",
    "group by state\n",
    "order by 2 desc"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "dec27f8b-fb05-48b8-830e-3858ef5f5ce9",
     "showTitle": false,
     "title": ""
    }
   },
   "source": [
    "##### Criando outras tabelas"
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
     "nuid": "244c8ae9-2620-4945-885f-238b82aabfca",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "display(dbutils.fs.ls('/FileStore/tables/Bikes/'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "implicitDf": true,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "c64025a7-9d73-4e63-af8c-fe66e0a4ad2a",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "%sql\n",
    "use Teste;\n",
    "CREATE TABLE IF NOT EXISTS brands\n",
    "USING csv OPTIONS ('path' '/FileStore/tables/Bikes/brands.csv','header' 'true','inferSchema' 'true');\n",
    "\n",
    "CREATE TABLE IF NOT EXISTS categories\n",
    "USING csv OPTIONS ('path' '/FileStore/tables/Bikes/categories.csv','header' 'true','inferSchema' 'true');\n",
    "\n",
    "CREATE TABLE IF NOT EXISTS order_items\n",
    "USING csv OPTIONS ('path' '/FileStore/tables/Bikes/order_items.csv','header' 'true','inferSchema' 'true');\n",
    "\n",
    "CREATE TABLE IF NOT EXISTS orders\n",
    "USING csv OPTIONS ('path' '/FileStore/tables/Bikes/orders.csv','header' 'true','inferSchema' 'true');\n",
    "\n",
    "CREATE TABLE IF NOT EXISTS staffs\n",
    "USING csv OPTIONS ('path' '/FileStore/tables/Bikes/staffs.csv','header' 'true','inferSchema' 'true');\n",
    "\n",
    "CREATE TABLE IF NOT EXISTS stocks\n",
    "USING csv OPTIONS ('path' '/FileStore/tables/Bikes/stocks.csv','header' 'true','inferSchema' 'true');\n",
    "\n",
    "CREATE TABLE IF NOT EXISTS stores\n",
    "USING csv OPTIONS ('path' '/FileStore/tables/Bikes/stores.csv','header' 'true','inferSchema' 'true');\n",
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
      "implicitDf": true,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "b41b9a85-2020-4f11-9b61-869000b528bd",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "%sql\n",
    "use teste;\n",
    "select * from stores"
   ]
  }
 ],
 "metadata": {
  "application/vnd.databricks.v1+notebook": {
   "dashboards": [],
   "language": "python",
   "notebookMetadata": {
    "mostRecentlyExecutedCommandWithImplicitDF": {
     "commandId": 3439702354161202,
     "dataframes": [
      "_sqldf"
     ]
    },
    "pythonIndentUnit": 4
   },
   "notebookName": "02. Criando Tabelas Via Comando SQL",
   "widgets": {}
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
