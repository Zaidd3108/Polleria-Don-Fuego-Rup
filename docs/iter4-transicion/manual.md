# Manual de Usuario y Guía de Despliegue - Pollería Don Fuego S.A.C.

**Curso:** Modelado y Desarrollo de Aplicaciones (CIIN1322P)  
**Estudiante:** Kenneth Zaidd Machacuay Maldonado  
**Organización:** Pollería Don Fuego S.A.C.  
**Propósito:** Proveer la guía de operación del sistema, instrucciones de despliegue piloto y procedimientos para el usuario final durante la fase de Transición (T1)[cite: 1, 4].

---

## 1. Introducción
El presente manual describe el funcionamiento operativo del sistema de gestión para la *Pollería Don Fuego S.A.C.*, orientado a centralizar el registro de pedidos, agilizar la preparación en cocina, controlar el despacho y asegurar la emisión correcta de comprobantes de pago bajo el marco de la metodología RUP[cite: 1].

---

## 2. Requisitos del Entorno y Despliegue
* **Plataforma:** Compatible con entornos web y de escritorio basados en navegadores modernos (Google Chrome, Microsoft Edge, Firefox).
* **Herramientas de Soporte:** Git/GitHub para control de versiones, Visual Studio Code para mantenimiento de código fuente y simuladores de pasarelas de pago[cite: 1].
* **Instalación:** Despliegue inicial validado mediante pruebas de aceptación y piloto acompañado para mitigar la resistencia al cambio del personal operativo[cite: 1].

---

## 3. Guía de Operación por Rol

### 3.1. Rol: Cajero
* **Registro de Pedidos (CU-01):** Permite capturar los datos del cliente, los platos seleccionados de la carta vigente y la modalidad de atención (salón, teléfono o delivery)[cite: 3].
* **Validación de Disponibilidad (CU-02):** El sistema verifica automáticamente el stock y la vigencia del producto[cite: 3].
* **Registro de Cobro (CU-07):** Procesa el pago seleccionado por el cliente, permitiendo hasta 2 reintentos en caso de rechazo (Excepción E2)[cite: 3].
* **Emisión de Comprobante (CU-08):** Genera la boleta o factura electrónica obligatoria tras un cobro exitoso[cite: 3].

### 3.2. Rol: Cocinero
* **Preparación de Pedidos (CU-04):** Recibe la comanda digital de forma automática en cocina una vez validado el pago[cite: 3].
* **Gestión de Faltantes (CU-05):** Permite reportar la insuficiencia de insumos durante la cocción (Excepción E3) para notificar a caja de forma inmediata[cite: 3].

### 3.3. Rol: Repartidor
* **Despacho y Entrega (CU-06):** Gestiona la salida de los pedidos preparados y confirma la entrega final al cliente en el punto de destino[cite: 3].

---

## 4. Gestión de Excepciones y Contingencias Operativas
* **Excepción E1 (Sin stock / Fuera de carta):** El sistema ofrece una alternativa del menú; si el cliente la rechaza, el pedido se cancela sin generar ningún cobro[cite: 3].
* **Excepción E2 (Pago rechazado):** El sistema permite un máximo de 2 reintentos con otro medio de pago. Al agotarse, el pedido se anula de forma automática y se libera el stock reservado[cite: 3].
* **Excepción E3 (Faltante de insumos):** Notifica al cajero, anula el ítem afectado y procesa un reembolso parcial al cliente antes de emitir el comprobante final[cite: 3].