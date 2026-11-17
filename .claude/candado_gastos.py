#!/usr/bin/env python3
"""Candado de gastos (pedido del dueño): antes de cualquier orden que pueda generar algo de pago en Higgsfield,
se detiene y le pregunta al dueño en la aplicación. La consulta de precios (/estimate/) no cobra y pasa sin preguntar.
Lo llama el sistema antes de cada orden de la terminal (ver .claude/settings.json)."""
import json, re, sys

try:
    datos = json.load(sys.stdin)
except Exception:
    sys.exit(0)
orden = (datos.get("tool_input") or {}).get("command", "") or ""

# Lo que puede costar plata: llamadas a Higgsfield que no sean la consulta de precio,
# y los programas del proyecto que piden clips o imágenes.
de_pago = [
    r"api\.higgsfield\.ai(?!/estimate/)",
    r"generar\.py\s+enviar",
    r"portada_hf\.py\s+(borrar|animar)",
]
if any(re.search(p, orden) for p in de_pago):
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": "ask",
        "permissionDecisionReason": "CANDADO DE GASTOS: esta orden puede generar algo de pago en Higgsfield. "
            "Apruébela solo si ya le dijeron el costo en dólares y usted dijo que sí.",
    }}, ensure_ascii=False))
sys.exit(0)
