# Notas de la Versión (Release Notes) - Pollería Don Fuego S.A.C.

**Curso:** Modelado y Desarrollo de Aplicaciones (CIIN1322P)  
**Estudiante:** Kenneth Zaidd Machacuay Maldonado  
**Organización:** Pollería Don Fuego S.A.C.  
**Versión:** `v1.0-iter1` / Entrega Final (Hito PR)  
**Fecha:** 2026-11-07  

---

## 1. Resumen de la Versión
Esta entrega consolida el expediente técnico, de modelado y documentación operativa bajo el marco metodológico RUP para el sistema de gestión de pedidos, cocina y facturación de la **Pollería Don Fuego S.A.C.** Se incluyen todos los artefactos correspondientes a las fases de Inicio, Elaboración, Construcción y Transición[cite: 2].

---

## 2. Nuevas Funcionalidades y Artefactos Incluidos

### Fase de Inicio (Iteración I1 - Hito LCO)
* **Documento de Visión (`vision.md`):** Definición del problema, objetivos de negocio (`OBJ-1` a `OBJ-3`), alcance incluido/excluido y criterios de éxito.
* **Glosario Único (`glosario.md`):** Estandarización de actores (unificando el rol de *Cajero*) y conceptos clave del dominio.
* **Matriz de Riesgos (`riesgos.md`):** Identificación y planes de mitigación temprana (`R1` a `R8`) a lo largo de las 14 semanas[cite: 2].
* **Roadmap (`roadmap.md`):** Planificación temporal de fases, iteraciones e hitos (`LCO`, `LCA`, `IOC`, `PR`)[cite: 2].

### Fase de Elaboración (Iteraciones E1 y E2 - Hito LCA)
* **SRS Breve (`srs-breve.md`):** Especificación de los 9 Requisitos Funcionales (`RF-01` a `RF-09`) vinculados a las Historias de Usuario (`HU-01` a `HU-14`).
* **Modelos de Casos de Uso (`casos-uso.md`):** Detalle de `CU-01` a `CU-09`[cite: 1].
* **Modelado Visual (`exportaciones/`):** Diagrama de actividad con carriles (*Cliente*, *Cajero / Sistema*, *Cocina y reparto*) y gestión explícita de flujos alternos y compensaciones (`E1`, `E2`, `E3`)[cite: 1].

### Fase de Construcción y Transición (Iteraciones C1, C2 y T1 - Hitos IOC y PR)
* **Trazabilidad Integral (`trazabilidad.md`):** Mapeo bidireccional completo entre objetivos, requisitos, casos de uso y diagramas.
* **Plan de Pruebas (`pruebas.md`):** Casos de prueba funcionales y de excepción (`CP-01` a `CP-06`).
* **Documentación de Despliegue (`manual.md`):** Guía operativa por rol para la puesta en marcha piloto.

---

## 3. Correcciones y Mejoras Aplicadas (Revisión de Calidad)
* **Unificación Nominal:** Eliminación de ambigüedades entre "Recepcionista" y "Cajero" en todos los diagramas y textos.
* **Control de Excepciones:** Incorporación de compensaciones formales para liberación de stock reservado tras fallos de pago (máx. 2 reintentos) y reembolsos parciales por faltantes en cocina[cite: 1].
* **Estructura de Repositorio:** Estandarización bajo convenciones de ramas (`main`), commits descriptivos y etiquetado (`v1.0-iter1`).

---

## 4. Limitaciones Conocidas (Fuera de Alcance v1.0)
* No incluye integración con pasarelas de delivery de terceros.
* Módulos de contabilidad general, planillas y gestión de proveedores externos quedan diferidos para futuras versiones.