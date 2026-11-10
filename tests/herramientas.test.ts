import test from "node:test";
import assert from "node:assert/strict";
import { puntuar, clasificar } from "../lib/gancho.ts";
import { FORMULAS } from "../lib/formulas.ts";
import { revisarTitulo } from "../lib/titulo.ts";
import { contarPalabras, marca, rx } from "../lib/texto.ts";

test("los limites de palabra respetan las tildes", () => {
  assert.ok(rx("«qué»").test("no sabemos qué pasó"));
  assert.ok(!rx("«qué»").test("porque quéso"));
  assert.ok(!rx("«te»").test("este monte"));
  assert.equal(contarPalabras("¿Qué pasó en 1959? Nadie lo sabe."), 7);
  assert.equal(marca(75), "1:15");
  assert.equal(marca(3725), "1:02:05");
});

test("cada formula clasifica su propio ejemplo", () => {
  for (const f of FORMULAS) {
    const propias = f.patrones.filter((p) => rx(p).test(f.ejemplo)).length;
    assert.ok(propias > 0, `${f.nombre}: ningún patrón reconoce su ejemplo`);
  }
  assert.equal(FORMULAS.length, 21);
});

test("un gancho concreto le gana a un saludo vago", () => {
  const bueno = puntuar("El 8 de marzo de 2014 un avión con 239 personas desapareció de los radares. ¿Por qué nadie te contó esto?");
  const malo = puntuar("Hola amigos, bienvenidos al canal, hoy un video muy increíble");
  assert.ok(bueno.veredicto > malo.veredicto + 20, `${bueno.veredicto} vs ${malo.veredicto}`);
  assert.equal(malo.banda, "DÉBIL");
  assert.equal(clasificar("Hola amigos").nombre, "Sin clasificar");
});

test("la brevedad premia de 9 a 24 palabras", () => {
  assert.equal(puntuar("uno dos tres cuatro cinco seis siete ocho nueve").propiedades.brevedad, 100);
  assert.equal(puntuar("uno dos tres").propiedades.brevedad, 34);
  assert.equal(puntuar("").veredicto, 9); // igual que hookscore.py: el panel no se muestra para un gancho vacio
});

test("el titulo y la miniatura se revisan como pareja", () => {
  const r = revisarTitulo("El avión que desapareció con 239 personas", "239 DESAPARECIDOS HOY MISMO");
  const claves = r.problemas.map((p) => p.clave);
  assert.ok(claves.includes("repetido"));
  assert.ok(claves.includes("miniatura-larga"));
  assert.ok(claves.includes("celular"));
  const limpio = revisarTitulo("Vuelo MH370: 239 personas, 0 rastros", "SIGUE PERDIDO");
  assert.deepEqual(limpio.problemas, []);
  assert.equal(limpio.puntaje, 100);
  assert.ok(revisarTitulo("El caso MÁS IMPACTANTE DEL MUNDO ENTERO").problemas.some((p) => p.clave === "gritos"));
});

import { videoNuevo, desbloqueada, etapaActual } from "../lib/tipos.ts";
import { capitulosDe, candidatosShort, revisionAutomatica, exportarJSON, revisarConsulta, tiempos } from "../lib/guion.ts";

const frase = (n: number) => Array.from({ length: n }, (_, i) => `palabra${i}`).join(" ") + ".";

test("los capitulos siguen las reglas de YouTube", () => {
  const v = videoNuevo("Prueba");
  v.bloques.forEach((b) => (b.narracion = frase(50))); // 20 s por bloque a 150 ppm
  let c = capitulosDe(v);
  assert.equal(c.valido, true);
  assert.equal(c.lista[0].etiqueta, "0:00");
  assert.equal(c.lista[1].etiqueta, "0:20");
  v.bloques[1].narracion = frase(10); // 4 s: demasiado corto
  c = capitulosDe(v);
  assert.equal(c.valido, false);
  v.capitulos[v.bloques[1].id] = { titulo: "", incluir: false }; // se une al anterior
  c = capitulosDe(v);
  assert.equal(c.valido, true);
  assert.equal(c.lista.length, 6);
  assert.equal(Math.round(c.lista[0].segundos), 24);
  for (const b of v.bloques.slice(2, 6)) v.capitulos[b.id] = { titulo: "", incluir: false };
  assert.equal(capitulosDe(v).valido, false); // quedan menos de 3
});

test("los candidatos a Short se ordenan por lo que sobrevive solo", () => {
  const v = videoNuevo("Prueba");
  v.bloques[2].narracion = "El barco apareció intacto " + frase(60) + " Pero nadie estaba a bordo.";
  v.bloques[3].narracion = "Y entonces " + frase(8);
  const c = candidatosShort(v);
  assert.equal(c.length, 2);
  assert.equal(c[0].bloque.id, v.bloques[2].id);
  assert.ok(c[0].puntaje > c[1].puntaje);
});

test("las etapas se desbloquean solo al aprobar la anterior", () => {
  const v = videoNuevo("Prueba");
  assert.equal(etapaActual(v), "idea");
  assert.equal(desbloqueada(v, "guion"), false);
  v.aprobadas.idea = true;
  assert.equal(desbloqueada(v, "guion"), true);
  assert.equal(desbloqueada(v, "refinar"), false);
});

test("la revision automatica detecta saludo y falta de imagen", () => {
  const v = videoNuevo("Prueba");
  v.bloques[0].narracion = "Hola amigos, bienvenidos al canal.";
  const r = Object.fromEntries(revisionAutomatica(v).map((c) => [c.id, c.bien]));
  assert.equal(r.saludo, false);
  assert.equal(r.pantalla, false);
  assert.equal(r.gancho, false);
});

test("la exportacion arma las escenas y la consulta marca lo que falta", () => {
  const v = videoNuevo("Prueba");
  v.bloques[0].narracion = frase(25);
  v.bloques[0].enPantalla = "Mapa antiguo";
  const j = exportarJSON(v);
  assert.equal(j.escenas.length, 1);
  assert.equal(j.escenas[0].duracionSegundos, 10);
  assert.equal(tiempos(v)[1].inicio, 10);
  assert.deepEqual(revisarConsulta("qué pasó con el vuelo MH370", "El vuelo que nadie encontró", ""), ["pasó", "mh370"]);
});

test("hablarle al espectador sin pronombre tambien cuenta", () => {
  const sin = puntuar("Diez personas abandonaron en 1872 un barco que no se estaba hundiendo.");
  const con = puntuar("¿Sabías que diez personas abandonaron en 1872 un barco que no se estaba hundiendo?");
  assert.ok(con.propiedades.apelacion > sin.propiedades.apelacion);
  assert.ok(sin.propiedades.riesgo >= 70, `riesgo ${sin.propiedades.riesgo}`);
  assert.equal(con.banda, "ACEPTABLE");
  assert.equal(sin.banda, "DÉBIL");
});
