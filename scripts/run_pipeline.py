"""
Mutual Fund Analytics Capstone Project

Master ETL Pipeline Runner

This script executes the complete data pipeline:
1. Data Ingestion
2. Data Cleaning
3. Load to SQLite Database
"""

import subprocess
import sys


def run_script(script_path):
    """Run a Python script and stop pipeline if it fails."""

    print(f"\n{'='*60}")
    print(f"Running: {script_path}")
    print(f"{'='*60}")

    result = subprocess.run(
        [sys.executable, script_path]
    )

    if result.returncode != 0:
        print(f"\nERROR: {script_path} failed.")
        sys.exit(1)

    print(f"\nSUCCESS: {script_path} completed.")


if __name__ == "__main__":

    print("\nStarting Mutual Fund ETL Pipeline...")

    run_script("scripts/data_ingestion.py")
    run_script("scripts/data_cleaning.py")
    run_script("scripts/load_to_sqlite.py")

    print("\n" + "="*60)
    print("ETL PIPELINE COMPLETED SUCCESSFULLY")
    print("="*60)