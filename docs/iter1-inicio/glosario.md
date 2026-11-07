# Glosario Único de Términos - Pollería Don Fuego S.A.C.

**Curso:** Modelado y Desarrollo de Aplicaciones (CIIN1322P)  
**Estudiante:** Kenneth Zaidd Machacuay Maldonado  
**Propósito:** Unificar el vocabulario del dominio para asegurar la consistencia nominal entre el Documento de Visión, el SRS breve, las Historias de Usuario y los modelos UML.

---

## 1. Actores del Sistema y del Negocio
* **Cliente:** Persona natural o jurídica que solicita un pedido de pollos a la brasa o platos complementarios mediante atención presencial en salón, vía telefónica o servicio de delivery.
* **Cajero:** Usuario operativo encargado de recibir la solicitud del cliente, verificar la disponibilidad en carta/stock, registrar el pedido en el sistema, procesar el cobro y emitir el comprobante de pago *(Nota: Unificado bajo este término en reemplazo de "Recepcionista" tras hallazgo H1)*.
* **Cocinero:** Personal de planta responsable de recibir la comanda digital, preparar los alimentos solicitados, verificar la existencia de insumos durante la cocción y actualizar el estado del pedido a listo para despacho.
* **Repartidor:** Personal encargado de trasladar y entregar el pedido preparado al cliente en el punto de atención o domicilio correspondiente, confirmando la entrega final.
* **Administrador:** Usuario con privilegios de supervisión encargado de gestionar la carta vigente, controlar los parámetros del sistema y auditar el flujo general de ventas y anulaciones.

---

## 2. Conceptos Clave del Dominio
* **Pedido:** Solicitud formal realizada por un Cliente que contiene uno o más ítems de la carta vigente, modalidad de atención (salón, teléfono, delivery), estado actual y monto total a cobrar.
* **Comanda:** Orden de preparación interna enviada automáticamente hacia el área de cocina una vez que el pago del pedido ha sido validado con éxito.
* **Carta Vigente:** Catálogo activo de platos, combos y bebidas disponibles para la venta en la pollería durante el turno operativo.
* **Stock Reservado:** Cantidad de porciones o productos descontados temporalmente del inventario disponible mientras el cliente completa el proceso de pago (se libera automáticamente si el pago es rechazado tras agotar reintentos).
* **Comprobante de Pago:** Documento tributario o interno (boleta/factura) emitido obligatoriamente en el 100% de los pedidos cuyo cobro haya sido validado.

---

## 3. Términos de Gestión de Excepciones (RUP / UML)
* **Excepción E1 (Sin stock / Fuera de carta):** Evento alterno que ocurre durante la validación previa al cobro cuando un producto solicitado no cuenta con disponibilidad; requiere ofrecer una alternativa al cliente o cancelar el pedido sin generar cobro.
* **Excepción E2 (Pago rechazado):** Falla en la validación del medio de pago; permite hasta un máximo de 2 reintentos antes de anular definitivamente el pedido y liberar el stock reservado.
* **Excepción E3 (Faltante de insumos en cocina):** Incidencia detectada durante la preparación que impide completar un ítem ya cobrado; obliga a notificar al Cajero, anular el ítem afectado y procesar un reembolso parcial antes de cerrar el comprobante.
* **Compensación:** Acción correctiva definida explícitamente en el flujo del sistema para revertir estados parciales (como liberar stock o reembolsar dinero) ante la ocurrencia de una excepción, evitando transacciones inconclusas.