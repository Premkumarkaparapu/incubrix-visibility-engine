#!/usr/bin/env python3
"""
IncuBrix AEO, SEO & GEO Visibility Engine
Single-Command Launcher
"""

import sys
import os
import uvicorn

# Ensure the project directory is in sys.path
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
if PROJECT_DIR not in sys.path:
    sys.path.insert(0, PROJECT_DIR)

from backend.database import init_db
from backend.main import seed_if_needed

def main():
    print("=" * 70)
    print("  INCUBRIX AEO, SEO & GEO VISIBILITY INTELLIGENCE ENGINE")
    print("  Growth Engineer Assessment | Option 3")
    print("=" * 70)
    
    print("\n[1/3] Initializing SQLite database and verifying seeds...")
    init_db()
    seed_if_needed()
    print("      ✓ Database ready at backend/incubrix_visibility.db")
    
    print("\n[2/3] Starting FastAPI Engine & React Dashboard...")
    print("      ✓ Dashboard URL : http://localhost:8000")
    print("      ✓ API Swagger   : http://localhost:8000/docs")
    print("      ✓ Raw CSV Data  : http://localhost:8000/api/export/csv")
    print("\n[3/3] Server listening on http://127.0.0.1:8000 (Press Ctrl+C to stop)\n")
    
    port = int(os.environ.get("PORT", 8000))
    host = "0.0.0.0" if os.environ.get("PORT") else "127.0.0.1"
    uvicorn.run("backend.main:app", host=host, port=port, log_level="info")

if __name__ == "__main__":
    main()
