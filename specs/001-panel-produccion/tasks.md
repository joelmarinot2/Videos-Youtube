# Tareas: Panel de producción

**Entrada**: [spec.md](spec.md), [plan.md](plan.md)
Formato: `[ID] [Historia] Descripción`. `[x]` hecho y comprobado · `[ ]` pendiente.

## Fase 1 · Preparación

- [x] T001 Proyecto Next.js + TypeScript en la raíz del repositorio
- [x] T002 Estilo «misterio cinematográfico» en `app/globals.css`
- [x] T003 Esquema de Supabase con seguridad por fila en `supabase/schema.sql`

## Fase 2 · Base (bloquea todo lo demás)

- [x] T004 Tipos y orden de etapas en `lib/tipos.ts`
- [x] T005 Texto en español con tildes en `lib/texto.ts`
- [x] T006 Guardado en Supabase o en el navegador en `lib/almacen.ts`
- [x] T007 Entrada con correo y contraseña en `components/Sesion.tsx`
- [x] T008 Guardado automático en `lib/useVideo.ts`

## Fase 3 · Historia 1: crear y refinar el guion (P1)

- [x] T009 [H1] Pruebas del puntaje de ganchos y de las 21 fórmulas
- [x] T010 [H1] 21 fórmulas en español en `lib/formulas.ts`
- [x] T011 [H1] Puntaje de ganchos en `lib/gancho.ts`
- [x] T012 [H1] Lista de expedientes en `app/page.tsx`
- [x] T013 [H1] Etapa Idea
- [x] T014 [H1] Etapa Guion: ganchos con puntaje y editor por bloques
- [x] T015 [H1] Etapa Refinar: revisión automática y confirmaciones manuales

## Fase 4 · Historia 2: empaquetar (P2)

- [x] T016 [H2] Pruebas de título, capítulos y búsquedas
- [x] T017 [H2] Revisión de título y miniatura en `lib/titulo.ts`
- [x] T018 [H2] Etapa Título y miniatura, con vista previa
- [x] T019 [H2] Etapa Descripción, con la prueba de las tres búsquedas
- [x] T020 [H2] Etapa Capítulos, con las reglas de YouTube

## Fase 5 · Historia 3: Shorts y exportación (P3)

- [x] T021 [H3] Pruebas de candidatos a Short y de exportación
- [x] T022 [H3] Etapa Shorts
- [x] T023 [H3] Etapa Exportar: por escenas, solo narración y JSON

## Fase 6 · Historia 4: los demás agentes (P4)

- [x] T024 [H4] Instrucciones de los 12 agentes en `lib/agentes.ts`
- [x] T025 [H4] Página Canal: perfil de voz y agentes del canal

## Fase 7 · Verificación

- [x] T026 11 pruebas automáticas de `lib/` pasan
- [x] T027 Recorrido completo en navegador real: 8 etapas, recarga, reabrir, canal, celular; sin errores
- [x] T028 README con los pasos de Supabase y Vercel

## Pendiente (necesita al dueño del canal)

- [ ] T029 Crear el proyecto de Supabase, ejecutar `schema.sql` y crear el usuario
- [ ] T030 Importar el repositorio en Vercel con las dos variables de entorno
- [ ] T031 Probar la entrada con contraseña contra el Supabase real (no se pudo probar sin el proyecto)
- [ ] T032 Llenar el perfil de voz del canal

## Pendiente (fases siguientes)

- [ ] T033 Conectar el motor de IA y activar «Generar aquí con IA»
- [ ] T034 Recibir el repositorio del creador de videos y ajustar el formato de exportación
- [ ] T035 Botón «Enviar al creador de videos» en la etapa Exportar
- [ ] T036 Lectura de retención y de transcripciones dentro del panel
