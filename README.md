# 📊 ETL Data Pipeline (Python + SQL Server)

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-green.svg)
![SQL Server](https://img.shields.io/badge/SQL%20Server-SSMS-red.svg)
![ETL](https://img.shields.io/badge/ETL-Pipeline-orange.svg)
![Status](https://img.shields.io/badge/Project-Learning%20Project-yellow.svg)

---

## 🚀 Overview

This project is a **simple ETL (Extract, Transform, Load) pipeline** built using Python.  
It demonstrates how raw data is processed, transformed, and loaded into a **SQL Server database**.

The goal is to simulate a real-world **Data Engineering workflow** using Python and SQL Server.

---

## 🏗️ Architecture

```plaintext
Raw Data (CSV)
      ↓
Extract (Pandas)
      ↓
Transform (Cleaning + Feature Engineering)
      ↓
Load (SQL Server via ODBC)
      ↓
Final Table (SSMS)