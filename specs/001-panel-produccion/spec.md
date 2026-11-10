# Especificación: Panel de producción de Archivos Inexplicables

**Rama**: `claude/funny-keller-tkdr3z`
**Creada**: 2026-11-10
**Estado**: Implementada (fase 1)
**Pedido original**: «A partir de esos agentes, un sistema que pueda subir a GitHub y anclar a Vercel y
Supabase, donde pueda primero crear el guion y refinarlo, después usar cada uno de los agentes con un
panel interactivo, con la estética del canal Archivos Inexplicables, y que me dé el guion para ponerlo
en un creador de videos automáticos con IA.»

## Decisiones tomadas con el dueño del canal (2026-11-10)

| Pregunta | Respuesta |
| --- | --- |
| Estética | Misterio cinematográfico |
| Motor de IA | Sin IA por ahora; dejar el espacio listo |
| Recorrido | Paso a paso, una línea de producción por video |
| Entrega al creador de videos | Esperar su repositorio; por ahora copiar el guion |
| Quién entra | Solo el dueño |
| Refinar el guion | Por bloques |
| Shorts | Sacados del video largo |
| Automatización futura | El dueño aprueba cada paso |

## Historias de usuario

### Historia 1 · Crear y refinar el guion (Prioridad: P1)

Como dueño del canal, abro un expediente para un caso, escribo la idea, pruebo varios ganchos viendo su
puntaje, escribo el guion por bloques y lo reviso antes de aprobarlo.

**Por qué es la primera**: sin guion no hay video; es lo que pidió hacer «primero».

**Prueba independiente**: crear un expediente, aprobar Idea, Guion y Refinar, y ver el guion completo con
su duración.

**Escenarios de aceptación**:

1. **Dado** un expediente nuevo, **cuando** no he escrito el caso ni la promesa, **entonces** no puedo
   aprobar la etapa Idea y la etapa Guion aparece bloqueada.
2. **Dado** que escribo dos ganchos, **cuando** uno es un saludo vago y el otro tiene fecha y cifra,
   **entonces** el concreto recibe más puntaje y queda marcado como el de mayor puntaje.
3. **Dado** un guion con un bloque sin indicación de imagen, **cuando** entro a Refinar, **entonces** el
   panel nombra ese bloque, y al completarlo el aviso desaparece.
4. **Dado** el guion revisado, **cuando** no he marcado las tres confirmaciones manuales, **entonces** no
   puedo aprobar Refinar.

### Historia 2 · Empaquetar el video (Prioridad: P2)

Con el guion aprobado, preparo título, miniatura, descripción y capítulos, cada uno con su revisión.

**Prueba independiente**: con un guion aprobado, completar las etapas 4 a 6 y copiar la descripción con
capítulos.

**Escenarios de aceptación**:

1. **Dado** un título que repite una palabra de la miniatura, **entonces** el panel lo señala.
2. **Dado** un primer bloque de menos de 10 segundos, **entonces** los capítulos se marcan como no válidos
   y se indica unir el bloque siguiente; al unirlo pasan a válidos y empiezan en 00:00.
3. **Dada** una búsqueda cuyas palabras no están en el título ni en las primeras líneas, **entonces** el
   panel lista las que faltan.

### Historia 3 · Shorts y exportación (Prioridad: P3)

Elijo los momentos del guion que sirven como Shorts y exporto todo para el creador de videos.

**Escenarios de aceptación**:

1. **Dado** un guion escrito, **entonces** el panel ordena los bloques por lo bien que se sostienen solos
   y marca los tres primeros como propuestas.
2. **Dado** el video aprobado, **cuando** abro Exportar, **entonces** puedo copiar o descargar el guion por
   escenas, solo narración o en JSON, y el JSON incluye escenas, capítulos y Shorts.

### Historia 4 · Usar los demás agentes (Prioridad: P4)

Desde la página Canal escribo el perfil de voz y uso los agentes de plan, tendencias, auditoría,
comentarios, retención y edición copiando sus instrucciones.

### Casos límite

- Reabrir una etapa aprobada bloquea las siguientes hasta volver a aprobarla.
- Recargar la página o cerrar el navegador no pierde cambios (guardado automático; aviso si falla).
- Sin Supabase configurado, el panel avisa que está en modo demostración.
- Un gancho vacío no muestra puntaje; un guion vacío no exporta nada.

## Requisitos

### Funcionales

- **RF-001**: El sistema DEBE pedir correo y contraseña cuando Supabase está configurado, y no ofrecer registro.
- **RF-002**: El sistema DEBE guardar cada video y el perfil del canal por usuario, con seguridad por fila.
- **RF-003**: El usuario DEBE poder crear, abrir, renombrar y eliminar expedientes.
- **RF-004**: Cada expediente DEBE recorrer ocho etapas en orden; una etapa solo se abre al aprobar la anterior.
- **RF-005**: El usuario DEBE poder reabrir cualquier etapa aprobada.
- **RF-006**: El sistema DEBE puntuar ganchos (cinco propiedades, veredicto, fórmula, arreglo) mientras se escribe.
- **RF-007**: El guion DEBE editarse por bloques, cada uno con narración e indicación de pantalla, reordenables.
- **RF-008**: El sistema DEBE calcular duración por bloque y total según palabras por minuto configurables.
- **RF-009**: El sistema DEBE revisar título y miniatura como pareja.
- **RF-010**: El sistema DEBE generar capítulos desde los bloques y validarlos con las reglas de YouTube.
- **RF-011**: El sistema DEBE proponer candidatos a Short desde los bloques del guion.
- **RF-012**: El sistema DEBE exportar el guion en tres formatos y permitir copiar y descargar.
- **RF-013**: Cada etapa DEBE ofrecer las instrucciones completas de su agente para copiar, incluyendo la voz
  del canal y los datos del video.
- **RF-014**: Las instrucciones de todo agente DEBEN prohibir inventar datos.
- **RF-015**: El sistema DEBE generar texto con IA dentro del panel. [PENDIENTE: el dueño eligió no conectar IA por ahora]
- **RF-016**: El sistema DEBE enviar el guion al creador de videos. [NECESITA ACLARACIÓN: formato exacto; depende del
  repositorio del creador de videos, aún no entregado]

### Entidades

- **Video (expediente)**: nombre, idea, ganchos, bloques, revisión, títulos, miniatura, descripción,
  capítulos, Shorts, etapas aprobadas.
- **Bloque**: tipo (gancho, giro, desarrollo, revelación, cierre), título, narración, en pantalla.
- **Short**: bloque de origen, primera línea nueva, texto, texto en pantalla, punto de bucle.
- **Perfil del canal**: audiencia, cómo habla, palabras que no usa, palabras que usa, lo que no afirma, formato.

## Criterios de éxito

- **CE-001**: Una persona que no programa puede poner el panel en internet siguiendo solo el README.
- **CE-002**: Un video recorre las ocho etapas de principio a fin sin errores en la consola del navegador.
- **CE-003**: Tras recargar la página, todo lo escrito sigue ahí.
- **CE-004**: El panel no tiene desplazamiento horizontal en un celular de 390 px de ancho.
- **CE-005**: Toda regla de `lib/` tiene al menos una prueba, y todas pasan.

## Supuestos

- El canal es de misterios y casos sin resolver, narrado en español, con video generado por IA.
- La estética exacta del canal (logo, colores) no fue entregada; se usó la dirección elegida por el dueño.
- La voz del creador de videos habla a unas 150 palabras por minuto; es ajustable por video.
