# Registro de Revisión por Pares y Control de Calidad - Pollería Don Fuego S.A.C.

**Curso:** Modelado y Desarrollo de Aplicaciones (CIIN1322P)  
**Estudiante:** Kenneth Zaidd Machacuay Maldonado  
**Organización:** Pollería Don Fuego S.A.C.  
**Propósito:** Documentar la verificación de coherencia entre los artefactos de Inicio y Elaboración (Documento de Visión, Glosario, SRS Breve y Diagrama de Actividad), registrando los hallazgos detectados y las acciones correctivas aplicadas antes de emitir la etiqueta `v1.0-iter1`.

---

## 1. Lista de Verificación de Calidad (Checklist)

| Criterio de Revisión | Artefactos Verificados | Estado | Observaciones |
| :--- | :--- | :--- | :--- |
| **Consistencia Nominal** | Visión, Glosario, SRS Breve, Diagramas | Aprobado (Corregido) | Se unificó el término de actor operativo a **Cajero** en todos los documentos. |
| **Claridad de Alcance** | Documento de Visión (`vision.md`) | Aprobado | Inclusiones (E1-E3) y exclusiones explícitas claramente delimitadas. |
| **Cobertura de Requisitos** | SRS Breve (`srs-breve.md`) y Casos de Uso | Aprobado | El 100% de los RF (`RF-01` a `RF-09`) tienen HU y CU asignados. |
| **Control de Excepciones** | Diagrama de Actividad (`actividad.png`) | Aprobado (Corregido) | Excepciones E1, E2 y E3 modeladas con sus respectivas compensaciones y nodos de fin. |
| **Trazabilidad Cruzada** | Matriz de Trazabilidad (`trazabilidad.md`) | Aprobado | Correspondencia bidireccional verificada entre objetivos, RF, HU, CU y evidencias gráficas. |
| **Estándares del Repositorio** | Estructura de carpetas, commits y tags | Aprobado | Nomenclatura de archivos y etiqueta `v1.0-iter1` listas para entrega. |

---

## 2. Registro de Hallazgos y Acciones Correctivas

| ID | Artefacto Afectado | Hallazgo Detectado | Acción Correctiva Aplicada | Estado |
| :--- | :--- | :--- | :--- | :--- |
| **H1** | Documento de Visión, Glosario y Diagramas | Inconsistencia terminológica: se utilizaba "Recepcionista" en algunos textos y "Cajero" en los carriles del diagrama de actividad. | Se estandarizó el rol bajo el término único **Cajero** en el Glosario (`glosario.md`), Documento de Visión y modelos UML. | Resuelto |
| **H2** | Diagrama de Actividad (`actividad.png`) | En la Excepción E2 (Pago rechazado), faltaba especificar la acción de compensación sobre el inventario reservado tras agotar reintentos. | Se incorporó explícitamente la liberación del stock reservado al anular el pedido tras alcanzar el límite de 2 reintentos. | Resuelto |
| **H3** | Diagrama de Actividad y SRS Breve | En la Excepción E3 (Faltante de insumos en cocina), el flujo no indicaba el ajuste financiero previo a la emisión del comprobante. | Se vinculó la notificación de faltante (`CU-05`) con el reembolso parcial (`CU-09`) antes de ejecutar la emisión del comprobante (`CU-08`). | Resuelto |
| **H4** | Matriz de Trazabilidad (`trazabilidad.md`) | Algunos requisitos carecían de referencia explícita hacia la evidencia visual en el diagrama de actividad. | Se añadió la columna de evidencia gráfica mapeando cada `RF` y `CU` con su nodo o decisión exacta en la Figura 2. | Resuelto |