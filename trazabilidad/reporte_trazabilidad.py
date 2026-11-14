"""Reporte semiautomatizado de cobertura. Uso: python reporte_trazabilidad.py matriz.csv
CSV con columnas: req,cu,clase,prueba (valores multiples separados por ';')"""
import csv, sys
with open(sys.argv[1], newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))
n = len(rows)
for col in ("cu", "clase", "prueba"):
    ok = sum(1 for r in rows if r[col].strip())
    print(f"Cobertura {col}: {ok}/{n} = {ok/n:.0%}")
for r in rows:
    faltan = [c for c in ("cu", "clase", "prueba") if not r[c].strip()]
    if faltan:
        print(f"BRECHA {r['req']}: sin {', '.join(faltan)}")
