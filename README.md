# Consumer Complaint Risk Monitor: CFPB Peer Benchmarking Pipeline

Ingest the CFPB Consumer Complaint Database (bulk CSV backfill + daily API incremental pulls) and FDIC bank asset data into Databricks (Delta tables, medallion architecture), transform with dbt into a star schema, and produce peer-benchmarking marts and a dashboard for a consulting-style risk analysis.

> **Work in progress** — scaffolding only; pipeline logic not yet implemented.

## Architecture

| Layer  | Location | Description |
|--------|----------|-------------|
| Bronze | Python / Databricks | Raw CFPB complaints + FDIC institution data |
| Silver | `dbt/models/staging` | Typed, deduplicated, standardized |
| Gold   | `dbt/models/marts` | Star schema + benchmark marts |

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

## Data

Download the bulk complaint CSV from https://www.consumerfinance.gov/data-research/consumer-complaints/ into `data/raw/`.
