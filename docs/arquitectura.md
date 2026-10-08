# Documento de Arquitectura de Software – gameChat

**Versión:** 1.2 (backend propio en lugar de Firebase)  
**Fecha:** 08/10/2026 (v1.0: 14/05/2026)  
**Autor:** Emanuel Romero  
**Cliente / Producto:** gameChat – Red social para hinchas  

---

## Tabla de Contenidos
1. [Visión General](#1-visión-general)
2. [Glosario de Términos](#2-glosario-de-términos)
3. [Historias de Usuario](#3-historias-de-usuario)
4. [Requisitos No Funcionales](#4-requisitos-no-funcionales)
5. [Stack Tecnológico](#5-stack-tecnológico)
6. [Arquitectura de Componentes](#6-arquitectura-de-componentes)
7. [Modelo de Datos Principal (PostgreSQL)](#7-modelo-de-datos-principal-postgresql)
8. [Sistema de Energía](#8-sistema-de-energía)
9. [Flujos de Usuario Principales](#9-flujos-de-usuario-principales)
10. [Catálogo de Minijuegos PvP (MVP)](#10-catálogo-de-minijuegos-pvp-mvp)
11. [Estrategia de Monetización (No Pay-to-Win)](#11-estrategia-de-monetización-no-pay-to-win)
12. [API de Datos Deportivos](#12-api-de-datos-deportivos)
13. [Seguridad y Moderación](#13-seguridad-y-moderación)
14. [Traducción Automática en Chat Rivales](#14-traducción-automática-en-chat-rivales)
15. [Escalabilidad y Rendimiento](#15-escalabilidad-y-rendimiento)
16. [Rankings](#16-rankings)
17. [Plan de Implementación (MVP)](#17-plan-de-implementación-mvp)
18. [Gestión de Riesgos](#18-gestión-de-riesgos)
19. [Arquitectura de Código (MVVM + Riverpod)](#19-arquitectura-de-código-mvvm--riverpod)
20. [Estrategia de Testing](#20-estrategia-de-testing)
21. [Plan de Rollout y Métricas de Éxito](#21-plan-de-rollout-y-métricas-de-éxito)
22. [Análisis de Viabilidad y Futuro del Sistema](#22-análisis-de-viabilidad-y-futuro-del-sistema)
23. [Herramientas de IA para Generación de Assets](#23-herramientas-de-ia-para-generación-de-assets)
24. [Inversión Estimada y Planificación Temporal](#24-inversión-estimada-y-planificación-temporal)

---

## 1. Visión General

### 1.1 Propósito del sistema
gameChat es una plataforma social móvil para hinchas de fútbol que permite vivir los partidos en comunidad mediante chats sincrónicos, un simulador visual del encuentro, peleas RPG por turnos entre hinchas rivales con apuestas, ademas de un ecosistema de minijuegos PvP y PvE y pencas (predicciones) que operan durante toda la semana. Todo esto dentro de una experiencia gamificada con moneda virtual, sistema de energía, tienda estética y una red de amigos persistente.

### 1.2 Propuesta de valor única
Ser la primera aplicación que une transmisión de eventos deportivos en vivo, interacción social segmentada por equipo, enfrentamientos lúdicos entre hinchas y minijuegos PvP y PvE, con un modelo de monetización ético y estético que refuerza la identidad del usuario a través de su personaje personalizado. Los usuarios podran:

- Ver los eventos mas importantes de los partidos de fútbol en vivo, como goles, tarjetas, penales, cambios, etc. Ademas podrán ver estadísticas del partido.
- Interactuar con otros hinchas en chats sincrónicos.
- Agregar amigos de cualquier equipo y chatear con ellos de forma privada toda la semana.
- Jugar minijuegos PvP y PvE, desafiando a desconocidos o a sus propios amigos.
- Apostar en pencas (predicciones).
- Personalizar su personaje.
- Comprar ítems en la tienda estética.
- Ganar monedas virtuales.
- Subir de nivel.
- Subir de rango.
- Subir de liga.
- Subir de copa.
- Subir de torneo.

### 1.3 Público objetivo
Aficionados al fútbol mayores de 16 años, usuarios de teléfonos móviles Android e iOS, con foco inicial en América y Europa.

### 1.4 Principios de diseño
- **Identidad ante todo:** El personaje del usuario aparece en peleas, minijuegos y simulador; es el eje visual de la experiencia.
- **No pay-to-win:** Las monedas no se compran con dinero real. Solo se obtienen jugando, acertando predicciones y viendo anuncios opcionales.
- **Efímero y seguro:** Los chats duran solo el partido. No se permite multimedia. Moderación por spam y reportes.
- **Energía como recurso estratégico:** Limita los minijuegos diarios y fomenta decisiones sobre qué jugar.
- **Sin barreras idiomáticas:** El chat rivales traduce automáticamente los mensajes para que los hinchas de distintos países interactúen sin fricción.

---

## 2. Glosario de Términos

| Término | Definición |
|--------|------------|
| **Catarsis** | Chat exclusivo para hinchas del mismo equipo durante un partido. |
| **Rivales** | Chat compartido entre hinchas de ambos equipos durante un partido. |
| **Chat de Amigos** | Chat privado persistente (1v1 o grupal) disponible en todo momento, independiente del equipo de los usuarios. |
| **Pelea RPG** | Combate 1v1 por turnos simultáneos donde los jugadores eligen zonas de ataque y defensa. |
| **Penca** | Predicción de resultados de partidos con apuesta de monedas virtuales. |
| **Energía** | Recurso limitante diario (máx. 200 puntos) que se consume al jugar minijuegos. Se recarga con el tiempo o viendo anuncios. |
| **Monedas** | Moneda virtual de la app. Se gana en peleas, pencas y minijuegos. Solo se gasta en la tienda estética. |
| **Premium** | Suscripción mensual que elimina todos los anuncios de la app. |
| **MVP** | Producto Mínimo Viable. Primera versión con las funcionalidades Core suficientes para validar la idea en el mercado. |
| **GEP** | Goles y Eventos Principales. Datos de un partido en vivo (gol, tarjeta, penal, cambios). |
| **Flame Engine** | Motor de juegos 2D para Flutter. Utilizado para peleas, simulador y minijuegos. |

---

## 3. Historias de Usuario

### Épica 1: Onboarding y Personalización

**HU-01: Selección de idioma**
> Como usuario nuevo, quiero elegir mi idioma al abrir la app para que toda la interfaz se muestre en mi lengua nativa.
- **Prioridad:** Must Have.

**HU-02: Registro e inicio de sesión**
> Como usuario, quiero registrarme con mi email o cuenta de Google/Apple para acceder a la aplicación de forma segura.
- **Prioridad:** Must Have.

**HU-03: Elegir club y selección**
> Como hincha, quiero seleccionar mi club y mi selección para que la app personalice mi experiencia.
- **Prioridad:** Must Have.

**HU-03.1: Tema de la app**
> Como usuario, quiero que luego de seleccionar mi club o seleccion la app se renderice en base a los colores de mi club o seleccion. De esta manera me siento identificado con la app.
- **Prioridad:** Must Have.

**HU-04: Personalizar personaje**
> Como usuario, quiero editar el aspecto de mi personaje (color de piel, peinado, vestimenta con colores de mi club o selección) para que me represente en la app.
- **Prioridad:** Must Have.

---

### Épica 2: Chat y Partido en Vivo

**HU-05: Ver cuenta regresiva en Home**
> Como hincha, quiero ver en la pantalla principal el próximo partido de mi club y seleccion con una cuenta regresiva para saber cuándo empieza.
- **Prioridad:** Must Have.

**HU-06: Ingresar al chat "Catarsis"**
> Como hincha, quiero entrar al chat de mi equipo durante el partido para desahogarme y comentar la jugada solo con hinchas de mi club.
- **Prioridad:** Must Have.

**HU-07: Ingresar al chat "Rivales"**
> Como hincha, quiero entrar al chat compartido con los hinchas del equipo rival para cargarlos y desafiarlos durante el partido.
- **Prioridad:** Must Have.

**HU-08: Ver simulador del partido**
> Como usuario, quiero ver una cancha con los jugadores y los eventos importantes del partido en tiempo real para seguir el encuentro visualmente.
- **Prioridad:** Should Have.

---

### Épica 3: Amigos y Chat Social (Retención Semanal)

**HU-09: Agregar amigos**
> Como usuario, quiero buscar y agregar a otros usuarios como amigos para mantener contacto con ellos fuera de los partidos, independientemente del equipo que sigan.
- **Criterios de aceptación:**
  - Búsqueda por nombre de usuario o código único.
  - Sistema de solicitud de amistad (enviar, aceptar, rechazar).
  - Lista de amigos visible en una sección dedicada.
- **Prioridad:** Must Have.

**HU-10: Chat privado con amigos**
> Como usuario, quiero tener un chat persistente con mis amigos en cualquier momento de la semana para hablar de fútbol y organizar partidas.
- **Criterios de aceptación:**
  - Chat 1v1 y posibilidad de crear grupos de amigos.
  - Los mensajes persisten en el tiempo (a diferencia de los chats de partido).
  - Historial de mensajes accesible en todo momento.
- **Prioridad:** Must Have.

**HU-11: Desafiar amigos a minijuegos**
> Como usuario, quiero poder enviar un desafío directo a un amigo desde nuestro chat para jugar un minijuego juntos.
- **Criterios de aceptación:**
  - Botón de "Desafiar" dentro del chat privado o perfil del amigo.
  - Selección rápida de minijuego.
  - El amigo recibe una notificación push y una tarjeta de invitación accionable en el chat.
- **Prioridad:** Must Have.

---

### Épica 4: Peleas RPG

**HU-12: Invitar a un hincha rival a pelear**
> Como hincha, quiero invitar a un hincha del equipo rival a una pelea RPG desde el chat rivales para demostrar quién manda.
- **Prioridad:** Must Have.

**HU-13: Participar en una pelea RPG**
> Como jugador retado, quiero pelear por turnos simultáneos eligiendo zonas de ataque y defensa para vencer a mi rival.
- **Prioridad:** Must Have.

**HU-14: Ver pelea como espectador**
> Como usuario en el chat rivales, quiero ver la pelea entre dos usuarios en tiempo real para entretenerme y apostar por un ganador.
- **Prioridad:** Should Have.

---

### Épica 5: Minijuegos PvP

**HU-15: Jugar un minijuego PvP**
> Como usuario, quiero jugar minijuegos contra otros hinchas durante la semana para divertirme y ganar monedas.
- **Prioridad:** Must Have.

**HU-16: Consultar y recargar energía**
> Como usuario, quiero ver cuánta energía me queda y recargarla viendo un anuncio para seguir jugando.
- **Prioridad:** Must Have.

---

### Épica 6: Pencas

**HU-17: Apostar en una penca**
> Como usuario, quiero predecir el resultado de un partido y arriesgar monedas para ganar más monedas si acierto.
- **Prioridad:** Must Have.

---

### Épica 7: Tienda y Premium

**HU-18: Comprar ítems estéticos**
> Como usuario, quiero comprar skins, stickers y temas con mis monedas ganadas para personalizar aún más mi experiencia.
- **Prioridad:** Could Have (Fase 5).

**HU-19: Adquirir Premium mensual**
> Como usuario, quiero pagar una suscripción mensual para eliminar todos los anuncios de la aplicación.
- **Prioridad:** Should Have (Fase 5).

---

### Épica 8: Rankings

**HU-20: Ver mi posición en los rankings**
> Como usuario competitivo, quiero ver en qué posición estoy en los diferentes rankings para motivarme a mejorar.
- **Prioridad:** Should Have.

---

### Épica 9: Experiencia Inmersiva (Audio y Sonido)

**HU-21: Efectos de sonido en interacciones**
> Como usuario, quiero escuchar efectos de sonido al interactuar con la interfaz (botones, ganar monedas, resultados de minijuegos) para tener una retroalimentación más clara y gratificante.
- **Prioridad:** Should Have.

**HU-22: Audio inmersivo en partidos y peleas**
> Como hincha, quiero escuchar sonido ambiente de estadio durante la simulación del partido y efectos de golpes en las peleas RPG y minijuegos para sentir más emoción.
- **Prioridad:** Could Have.

**HU-23: Control de volumen y silencio**
> Como usuario, quiero poder silenciar los efectos de sonido y la música de fondo desde las configuraciones para no molestar a otros cuando estoy en espacios públicos.
- **Prioridad:** Must Have.

---

## 4. Requisitos No Funcionales

| Categoría | Requisito |
|-----------|-----------|
| **Rendimiento** | Un mensaje de chat aparece en los demás clientes en menos de 1 s. Los minijuegos corren a 60 FPS en dispositivos de gama media. |
| **Disponibilidad** | El chat y el seguimiento del partido deben estar disponibles durante todo el partido (los picos de tráfico se dan en los clásicos). |
| **Usabilidad** | Desde el Home, el usuario entra al chat del partido en 2 toques o menos. Interfaz disponible en 5 idiomas. |
| **Seguridad** | Ninguna clave de API vive en el cliente móvil. Toda lógica que otorga monedas o energía se valida en el servidor. |
| **Mantenibilidad** | Código organizado por features, con tests en la capa de dominio y CI en cada Pull Request. |

---

## 5. Stack Tecnológico

> **Decisión (v1.2):** gameChat usa un **backend propio** en lugar de Firebase. El objetivo del proyecto es aprender a diseñar y construir APIs, así que cada pieza del servidor (datos, autenticación, tiempo real) se construye y se entiende desde cero.

| Capa | Tecnología | Justificación |
|------|------------|---------------|
| **Frontend** | Flutter 3.x + Flame Engine | Desarrollo unificado Android/iOS, motor 2D ligero para peleas, simulador táctico y minijuegos. |
| **Estado de la app** | Riverpod (MVVM) | Separación entre UI y lógica, fácil de testear. |
| **Backend (API propia)** | Python + FastAPI | API REST + WebSockets. Documentación automática (OpenAPI/Swagger), validación con Pydantic y soporte asíncrono. |
| **Base de datos** | PostgreSQL + SQLAlchemy + Alembic | Base relacional para usuarios, clubes, partidos, amistades, pencas, rankings y tienda. Alembic versiona los cambios del esquema (migraciones). |
| **Tiempo real** | WebSockets (FastAPI) | Chats de partido, chat privado, peleas y minijuegos PvP. En la primera versión las salas viven en memoria del servidor. |
| **Caché y mensajería** | Redis *(cuando haga falta escalar)* | Pub/Sub para repartir mensajes entre varias instancias del servidor, chats efímeros con expiración (TTL) y caché de datos deportivos. |
| **Autenticación** | JWT (access + refresh tokens) + hash de contraseñas (Argon2/bcrypt) | Login con email propio. Más adelante, inicio de sesión con Google y Apple (OAuth 2.0). |
| **Tareas programadas** | APScheduler dentro del backend | Consulta periódica de la API deportiva, cierre de pencas, limpieza de chats y reparto de premios. |
| **Notificaciones push** | Firebase Cloud Messaging (FCM) — *solo para push* | Es el canal estándar para notificaciones en Android (y puede enviar a iOS vía APNs). Se integra al final; no almacena datos de la app. |
| **API de Deportes** | MVP: API pública gratuita (por ej. OpenLigaDB). Producción: Sportmonks / API-Football (pago). | Solo el backend consulta la API externa; la app nunca ve las claves. |
| **Traducción** | Google Cloud Translation API (NMT) | Traducción de mensajes en chat rivales, solo a los idiomas presentes en la sala (ver costos en la sección 14.5). |
| **Infraestructura** | Docker + Docker Compose | Levantar API + PostgreSQL (+ Redis) en local con un solo comando, y desplegar igual en un hosting con soporte para contenedores. |
| **Monetización** | Google Play / App Store (suscripciones) + AdMob (anuncios) | Suscripción mensual para eliminar anuncios. Anuncios recompensados para recargar energía. |
| **Audio** | audioplayers / flame_audio | Efectos de sonido (SFX) para UI, música de fondo y ambiente de estadio. |

---

## 6. Arquitectura de Componentes

```text
┌──────────────────────────────────────────────┐
│ App Flutter (Android / iOS)                  │
│  Pantallas (UI) · Flame 2D · Riverpod        │
│  Servicios de dominio · Cliente HTTP + WS    │
└──────────────┬───────────────────┬───────────┘
               │ HTTPS (REST)      │ WebSocket (WSS)
               ▼                   ▼
┌──────────────────────────────────────────────┐
│ Backend gameChat (FastAPI)                   │
│                                              │
│  Routers REST            Gateway WebSocket   │
│  /auth  /usuarios        /ws/partidos/{id}   │
│  /clubes /partidos       /ws/chats/{id}      │
│  /amigos /pencas         /ws/salas/{id}      │
│  /minijuegos /rankings                       │
│  /tienda /config                             │
│                                              │
│  Servicios: Auth · Energía · Pencas · Chat   │
│  Peleas · Minijuegos · Rankings · Traducción │
│                                              │
│  Tareas programadas (APScheduler):           │
│  - Consultar API deportiva                   │
│  - Cerrar pencas y repartir premios          │
│  - Limpiar chats de partido                  │
└───────┬──────────────┬──────────────┬────────┘
        │              │              │
        ▼              ▼              ▼
┌──────────────┐ ┌────────────┐ ┌───────────────────┐
│ PostgreSQL   │ │ Redis      │ │ Servicios externos│
│ datos        │ │ (al escalar│ │ - API deportiva   │
│ persistentes │ │ pub/sub,   │ │ - Google Translate│
│              │ │ caché)     │ │ - FCM (push)      │
└──────────────┘ └────────────┘ └───────────────────┘
```

**Principio clave:** la app nunca habla directo con la base de datos ni con servicios externos. Todo pasa por la API, que valida permisos y reglas de negocio (monedas, energía, apuestas) en el servidor.

---

## 7. Modelo de Datos Principal (PostgreSQL)

### 7.1 Tablas

`PK` = clave primaria, `FK` = clave foránea.

**usuarios**
- `id` (PK, UUID)
- `email` (único), `password_hash`
- `nombre_usuario` (único), `codigo_amigo` (único)
- `idioma`: es | en | pt | fr | de
- `club_id` (FK → clubes), `seleccion_id` (FK → selecciones)
- `tema_actual`: club | seleccion
- `personaje`: JSONB (colorCuerpo, peinado, vestimenta)
- `monedas`: entero
- `energia`: entero (máx. 200), valor guardado en la última actualización
- `energia_actualizada_en`: timestamp (ver sección 8.1)
- `premium`: booleano
- `creado_en`: timestamp

**clubes**
- `id` (PK), `nombre`, `escudo_url`, `color_primario`, `color_secundario`, `liga_id` (FK → ligas), `id_externo` (id en la API deportiva)

**selecciones**
- `id` (PK), `nombre`, `bandera_url`, `color_primario`, `color_secundario`, `id_externo`

**partidos**
- `id` (PK), `id_externo`
- `equipo_local_id`, `equipo_visitante_id`, `tipo_equipo`: club | seleccion
- `fecha_hora`: timestamp
- `estado`: programado | en_juego | finalizado
- `goles_local`, `goles_visitante`

**eventos_partido**
- `id` (PK), `partido_id` (FK), `minuto`, `tipo`: gol | tarjeta | penal | cambio, `equipo_id`, `detalle`: JSONB

**amistades**
- `id` (PK), `solicitante_id` (FK → usuarios), `receptor_id` (FK → usuarios)
- `estado`: pendiente | aceptada | rechazada
- `creado_en`
- Restricción única sobre el par de usuarios.

**chats_privados** / **chat_participantes** / **mensajes_privados**
- `chats_privados`: `id`, `es_grupo`, `creado_en`
- `chat_participantes`: `chat_id`, `usuario_id` (PK compuesta)
- `mensajes_privados`: `id`, `chat_id`, `usuario_id`, `texto`, `creado_en` (índice por `chat_id, creado_en` para paginar el historial)

**pencas** / **apuestas_penca**
- `pencas`: `id`, `partido_id` (FK), `cierre_apuestas`, `estado`: abierta | cerrada | liquidada
- `apuestas_penca`: `id`, `penca_id`, `usuario_id`, `ganador`: local | empate | visitante, `goles_local`, `goles_visitante` (opcionales), `monto`, `premio`, `creado_en`. Restricción única: una apuesta por usuario y penca.

**batallas**
- `id` (PK), `retador_id`, `retado_id`, `partido_id` (opcional, solo peleas durante partidos)
- `tipo`: pelea_partido | penales | ppt | reaccion | obstaculos | tenis | domina_balon
- `estado`: esperando_aceptacion | en_curso | finalizada
- `ganador_id` (opcional), `empate`: booleano, `resumen`: JSONB (secuencia de acciones)
- `creado_en`, `finalizado_en`

**apuestas_espectadores**
- `id`, `batalla_id`, `usuario_id`, `apuesta_por_id`, `monto`

**puntajes_ranking**
- `tipo`: global_peleas | global_pencas | penales | ppt | reaccion | obstaculos | tenis | domina_balon
- `usuario_id`, `puntaje`, `periodo` (por ej. `2026-10` para el ranking mensual de pencas; `permanente` para el resto), `actualizado_en`
- PK compuesta (`tipo`, `periodo`, `usuario_id`) e índice sobre (`tipo`, `periodo`, `puntaje DESC`). La posición se calcula con una consulta ordenada.

**movimientos_monedas**
- `id`, `usuario_id`, `cantidad` (+/−), `motivo`: pelea | penca | minijuego | tienda | anuncio, `referencia_id`, `creado_en`
- Libro de movimientos: el saldo de `usuarios.monedas` se actualiza en la misma transacción. Permite auditar y detectar trampas.

**items_tienda** / **inventario_usuario**
- `items_tienda`: `id`, `tipo`: skin | peinado | sticker | tema | festejo, `nombre`, `precio_monedas`, `activo`
- `inventario_usuario`: `usuario_id`, `item_id`, `comprado_en`

**configuracion**
- `clave` (PK), `valor`: JSONB
- Valores ajustables sin publicar una nueva versión de la app (costos de energía, dificultad de la IA, etc.). La app los lee desde `GET /config`.

### 7.2 Tiempo real (WebSockets)

Los datos efímeros no se guardan en PostgreSQL. Viven en memoria del servidor (y en Redis cuando se escale a varias instancias).

| Canal | Quién puede entrar | Contenido |
|---|---|---|
| `/ws/partidos/{partidoId}/catarsis` | Solo hinchas del equipo (el servidor lo verifica con el JWT) | Mensajes `{usuarioId, texto, timestamp}` |
| `/ws/partidos/{partidoId}/rivales` | Usuarios autenticados | Mensajes `{usuarioId, texto, idioma, traducciones, timestamp}` y avisos de peleas |
| `/ws/partidos/{partidoId}/eventos` | Usuarios autenticados | Goles, tarjetas y cambios para el simulador |
| `/ws/chats/{chatId}` | Participantes del chat privado | Mensajes nuevos (además se guardan en `mensajes_privados`) |
| `/ws/salas/{salaId}` | Los dos jugadores (+ espectadores en peleas) | Acciones de la partida `{usuarioId, tipo, timestamp}` |

**Formato de los mensajes:** todos los mensajes por WebSocket son JSON con un campo `tipo` (por ej. `mensaje`, `traduccion`, `evento_partido`, `accion`, `resultado`) para que la app sepa cómo procesarlos.

**Ciclo de vida:** los chats de partido se eliminan 10 minutos después del final del partido (tarea programada). Las salas de minijuegos se cierran al terminar la partida y solo se guarda el resultado en `batallas`.

---

## 8. Sistema de Energía

### 8.1 Reglas de negocio
- **Máximo de energía:** 200 puntos por usuario.
- **Consumo por minijuego:** Variable según popularidad y tipo, ajustable desde la tabla `configuracion` (ver 7.1).
  - Ejemplo inicial:
    - Piedra/Papel/Tijera Futbolero: 10 pts.
    - Reacción Rápida: 15 pts.
    - Penales PvP: 20 pts.
    - Fútbol-Tenis: 20 pts.
    - Carrera de Obstáculos: 25 pts.
    - Quien domina mas el balon: 25 pts.
- **Recarga automática:** 1 punto cada 3 minutos (20 puntos/hora). Tiempo total de recarga completa: 10 horas.
- **Cálculo perezoso (sin procesos programados):** no se actualiza la energía de todos los usuarios cada 3 minutos. Se guardan `energia` y `energiaActualizadaEn`, y la energía actual se calcula al consultarla:
  `energiaActual = min(200, energia + floor(minutosTranscurridos / 3))`.
  Al consumir energía, el endpoint del backend recalcula el valor, descuenta el costo y guarda el nuevo par (valor, fecha) dentro de una transacción.
- **Recarga por anuncio:** Ver un anuncio recompensado (AdMob) otorga 50 puntos de energía. Límite de 3 anuncios/día para usuarios gratuitos; sin límite para premium.
- **Premium:** La suscripción mensual elimina anuncios pero NO otorga energía extra automática. Los usuarios premium pueden optar por ver anuncios recompensados voluntariamente si desean energía adicional (sin límite).
- **Exclusión:** Las peleas RPG durante partidos NO consumen energía.

### 8.2 Indicadores visuales
- Barra de energía en Home y pantalla de minijuegos(un balon que se va inflando y desinflando segun la energia que tenga el usuario).
- Opción "Recargar" visible al quedarse sin energía suficiente(aparece un boton de mas energia al lado de la barra de energia).

---

## 9. Flujos de Usuario Principales

### 9.1 Onboarding
1. Seleccionar idioma → guardar en almacenamiento local y luego en el perfil del usuario.
2. Registro e inicio de sesión (`POST /auth/registro`, `POST /auth/login` → JWT).
3. Elegir club y selección (búsqueda con `GET /clubes?buscar=`).
4. Elegir tema visual (colores club o selección).
5. Personalizar avatar (Vectores dinámicos con Flutter CustomPaint).
6. Home.

### 9.2 Chat durante partido
1. Usuario toca "Ingresar al partido" desde Home (visible solo 5 min antes).
2. Se carga simulador visual (stream desde API externa).
3. Debajo, dos pestañas: "Catarsis" y "Rivales".
4. En "Rivales", los mensajes se muestran traducidos al idioma del usuario.
5. Botón "Invitar a pelear" → notifica al rival.
6. Si el rival acepta, se genera alerta global en chat rivales.

### 9.3 Pelea RPG (Flame)
1. Ambos jugadores entran en pantalla de pelea (máx. 90 seg).
2. Fase simultánea:
   - Eligen ataque (cabeza/pecho/abdomen/piernas) y defensa (mismas zonas).
   - Se revelan elecciones tras 3 segundos máx.
   - Cálculo de daño por zona no defendida.
3. Tres rondas. Si hay empate, moneda virtual (random). Si persiste, gana mayor ranking global de peleas.
4. Los espectadores ven la pelea en tiempo real por WebSocket y pueden apostar con monedas.
5. El ganador recibe recompensa en monedas + sube en ranking global de peleas. El perdedor no pierde monedas.

### 9.4 Pencas (Predicciones)
1. Usuario ve partidos disponibles hasta 10 min antes del inicio.
2. Vota por ganador/empate/perdedor; opcional resultado exacto.
3. Se descuentan monedas (apuesta base).
4. Al finalizar el partido, una tarea programada del backend reparte los premios según los aciertos.
5. Ranking mensual de pencas con recompensa (monedas o ítems estéticos).

### 9.5 Minijuegos PvP (entre semana)
1. Usuario selecciona minijuego desde el lobby.
2. El sistema verifica energía suficiente (costo variable según juego).
3. Emparejamiento aleatorio o desafío a amigo/rival.
4. Al entrar, se descuenta la energía.
5. Se juega en tiempo real por WebSocket (sala de la partida) + renderizado del personaje en Flame. El servidor valida las acciones y decide el resultado.
6. El ganador recibe recompensa baja en monedas. El perdedor pierde la energía. En caso de desconexión, el usuario desconectado no pierde nada (ni energía ni monedas), pero el usuario que permaneció conectado gana la partida por defecto.
7. El resultado actualiza el ranking individual del minijuego.

### 9.6 Interacción con Amigos y Desafíos
1. Usuario busca a un amigo por su ID/Username y envía solicitud.
2. El receptor acepta la solicitud; se crea el vínculo en la colección `amistades`.
3. Ambos pueden acceder a un chat privado persistente en la sección "Social".
4. Desde el chat, uno de los usuarios toca "Desafiar", elige un minijuego y apuesta su energía.
5. Se envía una notificación push y una tarjeta interactiva en el chat.

---

## 10. Catálogo de Minijuegos PvP (MVP)

### 10.1 Piedra, Papel o Tijera Futbolero
- **Tipo:** PvP por turnos simultáneos (3 seg límite).
- **Mecánica:** "Ataque" vence a "Defensa", "Defensa" vence a "Contraataque", "Contraataque" vence a "Ataque".
- **Duración:** Mejor de 3 rondas (~30 seg total).
- **Personaje:** Aparece ejecutando animación de ataque/defensa/contraataque.
- **Costo energía:** 10 pts.
- **Dificultad técnica:** Muy baja.

### 10.2 Reacción Rápida
- **Tipo:** PvP tiempo real.
- **Mecánica:** Aparece un balón en pantalla en un punto aleatorio. Ambos jugadores tocan la pantalla. El más rápido gana la ronda. 3 rondas.
- **Personaje:** El personaje del ganador festeja; el perdedor se lamenta.
- **Costo energía:** 15 pts.
- **Dificultad técnica:** Muy baja.

### 10.3 Penales PvP
- **Tipo:** PvP por turnos simultáneos.
- **Mecánica:** Un jugador es pateador (elige dirección y potencia), el otro es arquero (elige zambullida). Se alternan roles. 3 penales cada uno.
- **Personaje:** El personaje personalizado de cada uno aparece en su rol (pateador con camiseta de su club; arquero con guantes).
- **Costo energía:** 20 pts.
- **Dificultad técnica:** Media (física simple de trayectoria en Flame).

### 10.4 Fútbol-Tenis (Toques)
- **Tipo:** PvP tiempo real.
- **Mecánica:** Una pelota rebota entre ambos lados. El jugador toca la pantalla en el momento justo para devolverla. Quien falla el timing pierde el punto.
- **Personaje:** Ejecuta animación de golpeo (cabeza, pie, rodilla) según la altura de la pelota.
- **Costo energía:** 20 pts.
- **Dificultad técnica:** Media-baja.

### 10.5 Carrera de Obstáculos
- **Tipo:** PvP tiempo real con puntuación.
- **Mecánica:** Ambos jugadores controlan a su personaje corriendo lateralmente por una cancha, esquivando defensores (obstáculos). Gana quien llega más lejos sin chocar.
- **Personaje:** Corre, salta, se desmarca con animaciones fluidas.
- **Costo energía:** 25 pts.
- **Dificultad técnica:** Media (scroll lateral + colisiones en Flame).

### 10.6 Quien domina mas el balon
- **Tipo:** PvP tiempo real / vs IA (modo entrenamiento).
- **Mecánica:** A pantalla dividida, cada jugador toca su mitad de la pantalla para mantener el balón en el aire (como un contador de keepie-uppies). **El ganador es quien acumule más toques durante 60 segundos**. Si el balón toca el suelo, **se resetea automáticamente** al punto de inicio (sin eliminar al jugador); se contabiliza como una caída (💧) visible en el marcador. La partida termina únicamente al agotarse el tiempo.
- **Flujo de una partida:**
  1. Ambos jugadores ven un overlay **3-2-1** antes de que arranque la física.
  2. Al llegar a 0, los balones aparecen quietos en la parte superior de cada panel.
  3. El jugador toca para dar el primer impulso y acumular toques durante 60 segundos.
  4. Al finalizar el tiempo, aparece el overlay de resultado comparando los toques de ambos jugadores.
- **Personaje:** Cada jugador controla su avatar de perfil. Al tocar la pantalla el personaje da una patadita para devolverla.
- **Costo energía:** 15 pts.
- **Dificultad técnica:** Muy baja.

#### Modo vs IA (entrenamiento / testing)
> Permite jugar sin necesidad de un rival real. Diseñado principalmente para testing durante el desarrollo, pero también disponible para usuarios que quieran practicar antes de jugar PvP.

El rival IA tiene **tres niveles de dificultad**, seleccionables desde el lobby antes de iniciar:

| Nivel | Intervalo entre toques | Descripción |
|-------|------------------------|-------------|
| 🟢 **Fácil** | 0.9 – 2.2 segundos | La IA comete errores frecuentes. Ideal para aprender. |
| 🟡 **Media** | 0.5 – 1.1 segundos | La IA es competitiva pero vencible. Desafío equilibrado. |
| 🔴 **Difícil** | 0.3 – 0.6 segundos | La IA casi nunca pierde. Solo para jugadores expertos. |

**Implementación técnica:**
- La IA corre su propia simulación de física local (gravedad, rebote, reset al caer) en paralelo al panel del jugador, a 60 FPS.
- Los toques se programan con `Timer` de duración aleatoria dentro del rango de la dificultad (`DificultadIA.minMs` – `DificultadIA.maxMs`).
- No usa WebSocket; es 100% local. El `salaId` se fija en `'ia_game'` como valor de prueba.
- Los intervalos pueden ajustarse desde `GET /config` sin publicar una nueva versión (`dificultad_ia.<nivel>.min_ms` / `max_ms`).


---

## 11. Estrategia de Monetización (No Pay-to-Win)

### 11.1 Plan mensual Premium
- **Pago mensual** (ej: USD 2.99 – 5.99).
- **Beneficio principal:** Elimina TODOS los anuncios (banners, intersticiales, y obligatoriedad de ver recompensados).
- **Beneficio secundario:** Puede ver anuncios recompensados voluntariamente sin límite diario para recargar energía. Usuarios gratuitos limitados a 3/día.
- **NO otorga:** monedas extra, items exclusivos funcionales, energía extra gratuita, ventaja en rankings.

### 11.2 Anuncios (AdMob)
- Usuarios gratuitos: banner persistente en personalizar avatar, configuraciones de la app y lobby de minijuegos y pencas Intersticial cada 3 cambios de pantalla.En home y chat no habra publicidad
- Anuncios recompensados: disponibles para recargar 50 pts de energía (máx 3/día gratis; ilimitado premium).

### 11.3 Tienda Estética
- Ítems: skins de personaje, peinados, colores, animaciones de festejo, stickers para chat, temas visuales.
- **Moneda exclusiva de juego:** Solo se obtiene participando (sin compra directa). Esto elimina el pay-to-win y preserva la integridad competitiva.

---

## 12. API de Datos Deportivos

- **MVP:** OpenLigaDB (gratuita, limitada a algunas ligas) o ESPN Core API. Proveerá fixture, resultado y eventos básicos.
- **Producción:** Migrar a Sportmonks o API-Football (latencia <2s para GEP).  
  El simulador visual usará solo eventos importantes: gol, tarjeta roja, penal, cambios; no requiere tracking posicional minuto a minuto en MVP.
- **Backend como único consumidor:** para evitar límites de peticiones (rate limits) y no exponer claves de API en la app, solo el backend consulta (o recibe webhooks de) la API deportiva. Normaliza los datos, los guarda en PostgreSQL (`partidos`, `eventos_partido`) y los emite por WebSocket a los usuarios conectados.
- **Capa de abstracción:** el backend define una interfaz `ProveedorDeportivo` con una implementación por API externa, para poder cambiar de proveedor sin tocar el resto del código.

---

## 13. Seguridad y Moderación

- **Chat:** Filtro de spam básico (límite 1 msg/segundo). Reporte de usuario con revisión reactiva.
- **Contenido:** Solo texto plano; no se permite subir imágenes, audio o video. Esto evita costos de almacenamiento y revisión de contenido multimedia.
- **Apuestas:** Moneda virtual cerrada, sin valor real ni retiro. Sin implicaciones legales de juego.
- **Autorización en la API:** cada endpoint y canal WebSocket verifica el JWT y los permisos (por ej., solo hinchas del equipo entran a Catarsis).
- **Lógica en el servidor:** energía, monedas, apuestas y resultados de partidas se calculan y validan en el backend, nunca en la app.
- **Contraseñas:** se guardan solo como hash (Argon2 o bcrypt).
- **Límite de peticiones:** rate limiting por usuario e IP en el login y en los chats.
- **Secretos:** las claves (API deportiva, traducción, firma de JWT) viven en variables de entorno, nunca en el repositorio.

---

## 14. Traducción Automática en Chat Rivales

### 14.1 Problema a resolver
En partidos entre selecciones o clubes de distintos países (ej. Uruguay vs Inglaterra), los hinchas hablan idiomas diferentes. Sin traducción, el chat rivales pierde su esencia. Se requiere un sistema que derribe la barrera del idioma sin fricción para el usuario.

### 14.2 Solución propuesta
Integración con **Google Cloud Translation API (NMT)** desde el **servicio de traducción del backend**, que procesa cada mensaje del chat Rivales después de publicarlo.

### 14.3 Flujo de funcionamiento
1. El usuario redacta un mensaje en su idioma nativo y lo envía al chat "Rivales".
2. La app envía el mensaje por WebSocket con el texto original y su idioma (campo `idioma`).
3. El backend reenvía de inmediato el mensaje original a todos los conectados y, en paralelo, lanza una tarea asíncrona de traducción.
4. La función invoca la API de traducción **solo para los idiomas de los usuarios presentes en la sala**, exceptuando el idioma original (en un Uruguay vs Inglaterra, normalmente solo español ↔ inglés). Los 5 idiomas soportados son inglés, español, portugués, francés y alemán.
5. Cuando llegan las traducciones, el backend emite un evento `traduccion` con el campo `traducciones` asociado al id del mensaje.
6. El cliente Flutter, al renderizar el chat, muestra **automáticamente el texto en el idioma seleccionado por el usuario** (obtenido de su perfil). Si existe traducción a ese idioma, la muestra; si no, muestra el texto original.
7. El usuario puede **tocar el mensaje** para revelar el texto original en una burbuja emergente, permitiendo ver la redacción exacta del rival.

### 14.4 Estructura del mensaje (evento WebSocket)
```json
"mensajes": {
  "msg_123": {
    "uid": "usuarioUruguay",
    "texto": "¡Vamos la celeste, hoy copamos!",
    "idioma": "es",
    "timestamp": 1715692800000,
    "traducciones": {
      "en": "Let's go sky blue, we're taking over today!",
      "pt": "Vamos Celeste, hoje dominamos!",
      "fr": "Allez les bleus ciel, on prend le contrôle aujourd'hui !",
      "de": "Auf geht's Himmelblau, heute übernehmen wir!"
    }
  }
}
```

### 14.5 Costos operativos

**Precio de referencia:** ~USD 20 por cada millón de caracteres traducidos.

| Escenario (por partido) | Cálculo | Costo |
|---|---|---|
| Traducir a 4 idiomas siempre (diseño original) | 10.000 mensajes × 50 caracteres × 4 idiomas = 2.000.000 caracteres | **USD 40** |
| Traducir solo a los idiomas presentes en la sala (ej. español ↔ inglés) | 10.000 × 50 × 1 = 500.000 caracteres | **USD 10** |

Con 100 partidos al mes, el diseño original costaría unos **USD 4.000/mes**, y el diseño por idiomas presentes, unos **USD 1.000/mes**. Para bajar aún más el costo se evaluarán dos medidas:

- **Traducción bajo demanda:** traducir solo cuando un usuario toca el mensaje.
- **Caché de frases frecuentes:** "¡Gooool!", "¡Vamos!", etc.

### 14.6 Privacidad y latencia

- La traducción corre en segundo plano en el backend. El mensaje original se muestra al instante en el idioma del emisor mientras la traducción se propaga (latencia < 1 s).
- No se almacenan datos sensibles: solo texto efímero que se elimina al cerrar el chat.

---

## 15. Escalabilidad y Rendimiento

- **PostgreSQL:** perfiles, amistades, pencas, rankings y tienda. Consultas paginadas e índices sobre las columnas más consultadas.
- **WebSockets:** mensajes efímeros y estados de peleas y minijuegos. En la primera versión, una sola instancia del backend guarda las salas en memoria.
- **Escalado horizontal:** cuando una instancia no alcance (por ej. en un clásico), se levantan varias instancias detrás de un balanceador y se usa **Redis Pub/Sub** para que un mensaje llegue a todos los usuarios de la sala, estén conectados a la instancia que estén.
- **Tareas programadas:** reparto de premios (pencas, peleas), limpieza de chats y consulta de la API deportiva. La energía **no** usa un proceso programado (ver sección 8.1).
- **Flame Engine:** las peleas y minijuegos se renderizan en la app; solo se transmiten acciones por WebSocket (bajo consumo de ancho de banda).

---

## 16. Rankings

Cada actividad tiene su propio ranking independiente, que se actualiza al finalizar cada partida o evento:

1. Ranking global de peleas (solo peleas RPG de partidos).
2. Ranking de pencas (mensual, se resetea).
3. Ranking de Penales PvP.
4. Ranking de Piedra, Papel o Tijera.
5. Ranking de Reacción Rápida.
6. Ranking de Fútbol-Tenis.
7. Ranking de Carrera de Obstáculos.
8. Ranking de Quién domina más el balón.

Los rankings 3 a 8 son permanentes (no se resetean) y se almacenan en `rankings/{tipo}/entradas/{uid}`.

---

## 17. Plan de Implementación (MVP)

> El orden de aprendizaje y construcción real del proyecto de estudio está en el [README](../README.md). Las fases de abajo describen el producto completo.

**Fase 1: Núcleo social y partidos**
- Onboarding, selección de club/selección, personalización de personaje.
- Integración con la API deportiva (fixture y resultados) a través del backend.
- Chat Catarsis y Rivales con ciclo de vida automático y traducción en Rivales.
- Simulador básico (eventos importantes).
- Sistema de energía (visualización y recarga calculada).

**Fase 2: Peleas y sistema social**
- Sistema de amigos y chat privado persistente.
- Desafíos directos desde el chat de amigos.
- Sistema de peleas RPG en Flame (turnos simultáneos).
- Espectadores y apuestas en tiempo real.
- Ranking global de peleas.

**Fase 3: Pencas**
- Predicciones de partidos con monedas.
- Ranking mensual de pencas.
- Tarea programada de reparto de premios.

**Fase 4: Minijuegos y energía completa**
- Piedra, Papel o Tijera, Domina el balón y Reacción Rápida (dificultad muy baja).
- Penales PvP y Fútbol-Tenis (dificultad media).
- Carrera de Obstáculos.
- Integración con el sistema de energía y la recarga por anuncios.
- Rankings independientes.

**Fase 5: Tienda y monetización**
- Tienda estética completa (skins, stickers, temas).
- Integración con AdMob (banners, intersticiales, recompensados).
- Suscripción Premium mensual.
- Configuración dinámica de costos de energía (`GET /config`).
- Notificaciones push con FCM.

---

## 18. Gestión de Riesgos

| Riesgo | Impacto | Mitigación |
|---|---|---|
| La API deportiva gratuita cierra o limita el acceso | Alto | Interfaz `ProveedorDeportivo` en el backend; tener Sportmonks como alternativa. |
| Los picos de tráfico en clásicos saturan el backend | Medio | Pruebas de carga antes de cada fase; varias instancias + Redis Pub/Sub; escrituras en lote; monitoreo. |
| Pay-to-win encubierto si se venden monedas | Alto (reputacional) | No implementar jamás la compra de monedas. Solo se obtienen jugando. |
| Abuso de energía con multicuentas | Medio | Verificación de email al registrarse; detección de patrones anómalos con el libro `movimientos_monedas`. |
| Moderación insuficiente en los chats | Medio | Filtro de spam automático, reportes de usuarios y, a futuro, Perspective API. |
| Seguridad de un backend propio (login, datos de usuarios) | Alto | Librerías probadas para hash y JWT, validación con Pydantic, rate limiting, dependencias actualizadas y revisión de seguridad antes de publicar. |
| Costos de traducción elevados | Medio | Traducir solo a los idiomas presentes o bajo demanda; caché de frases comunes; monitoreo de cuotas (ver 14.5). |

---

## 19. Arquitectura de Código (MVVM + Riverpod)

### 19.1 Decisión arquitectónica
No se recomienda Clean Architecture pura en la app. La app consume una sola API propia (repositorio remoto), y Flame Engine requiere acoplamiento entre el renderizado y la UI. Clean Architecture generaría sobrediseño y haría más lenta la iteración del MVP.

**Patrón elegido:** MVVM con Riverpod (`Notifier` / `AsyncNotifier` + providers), en una estructura modular por features.

### 19.2 Ventajas
- Separación clara entre la lógica de negocio (domain/services) y la presentación (widgets + providers).
- Riverpod es un paquete muy adoptado en la comunidad Flutter, no depende del `BuildContext` y facilita el testing.
- Testeable por capas sin multiplicar archivos innecesarios.
- Fácil incorporación de nuevos desarrolladores.

### 19.3 Estructura de carpetas

```text
lib/
├── app.dart
├── main.dart
├── core/
│   ├── theme/
│   ├── router/
│   ├── energy/              # Lógica de energía (transversal)
│   ├── network/             # Cliente HTTP (dio) y WebSocket, manejo del JWT
│   └── config/              # Configuración leída de GET /config
├── features/
│   ├── auth/
│   │   ├── data/            # Repositorio: /auth (login, registro, refresh)
│   │   ├── domain/          # AuthService
│   │   └── presentation/    # Pantallas y providers
│   ├── chat/
│   │   ├── data/            # Repositorio: WebSocket de chats
│   │   ├── domain/          # ChatService
│   │   └── presentation/
│   ├── match_simulator/
│   │   ├── data/            # Repositorio: /partidos + WebSocket de eventos
│   │   ├── domain/          # MatchService
│   │   └── presentation/    # Widget de Flame
│   ├── fights/
│   │   ├── data/
│   │   ├── domain/
│   │   └── presentation/    # Widget de Flame
│   ├── minigames/
│   │   ├── domina_balon/
│   │   ├── penales/
│   │   │   ├── domain/      # PenalGameService
│   │   │   └── presentation/
│   │   ├── ppt/
│   │   ├── reaccion/
│   │   ├── obstaculos/
│   │   └── tenis/
│   ├── pencas/
│   ├── store/
│   └── rankings/
└── shared/
    ├── models/
    ├── widgets/
    └── utils/
```

---

## 20. Estrategia de Testing

### 20.1 Pirámide de testing
Dado el stack Flutter + Flame + FastAPI + PostgreSQL, la estrategia de testing tiene 5 niveles.

| Nivel | Qué se testea | Herramientas | Objetivo |
|---|---|---|---|
| **Backend** | Servicios, endpoints REST y WebSockets | `pytest`, `TestClient` de FastAPI, PostgreSQL de prueba en Docker | Cada endpoint con casos felices y de error; 90% de cobertura en los servicios. |
| **Unitarios (app)** | Servicios de dominio en Dart (AuthService, PeleaService, EnergiaService, PencaService) | `flutter_test`, `mocktail` | 90% de cobertura en la capa domain, testeando contra interfaces abstractas. |
| **Widget tests** | Widgets de UI aislados, con providers simulados | `flutter_test` + `ProviderScope` con overrides | Estados de carga, error y datos en Onboarding, Home y Lobby de minijuegos. |
| **Integración** | Flujos completos app + backend levantado con Docker Compose | `integration_test` | Registro, login, personalización del personaje y envío/lectura de un mensaje con traducción. |
| **Manual / gameplay** | Sincronización de peleas, renderizado y minijuegos | TestFlight (iOS) / Internal Testing (Android) | Experiencia de juego y latencia en redes reales (WiFi/4G/5G). |

### 20.2 Reglas de calidad
- Ningún Pull Request se mergea si no pasan los tests unitarios y de widget.
- Los tests del backend y de integración corren en CI (GitHub Actions), con PostgreSQL levantado como servicio.
- Los tests manuales de gameplay se hacen antes de cada Release Candidate.

---

## 21. Plan de Rollout y Métricas de Éxito

### 21.1 Fases de rollout

| Fase | Usuarios | Canal | Objetivo |
|---|---|---|---|
| **Alpha cerrada** (Fases 1-2) | 50-100 hinchas de un club local | Invitación directa, grupos de WhatsApp | Validar onboarding, chat y cuenta regresiva. Detectar bugs críticos de UX. |
| **Beta abierta regional** (Fase 3) | 500-2.000 hinchas de 2-3 clubes grandes de un país | Redes sociales, campañas en Instagram/TikTok | Medir retención, uso de energía, primeras peleas y pencas, calidad de la traducción. |
| **Lanzamiento global** (MVP completo) | Apertura total en Play Store y App Store | ASO, contenido generado por usuarios | Escalar a 10k+ usuarios activos y validar la monetización. |

### 21.2 Métricas de éxito clave
- **North Star Metric:** usuarios activos en día de partido (DAU Matchday).
- **Retención:** Día 7 > 40% y Día 30 > 20%.
- **Engagement:** promedio de 5 mensajes enviados por usuario en el chat del partido.
- **Traducción:** > 90% de los mensajes en Rivales se muestran traducidos correctamente.
- **Energía:** > 30% de los usuarios gratuitos ven al menos 1 anuncio de recarga por semana.
- **Conversión a Premium:** 2-5% de los usuarios activos se suscriben en los primeros 3 meses.
- **Costo de adquisición (CAC):** < USD 1 por usuario en canales orgánicos.

---

## 22. Análisis de Viabilidad y Futuro del Sistema

### 22.1 Fortalezas
- **Momento de mercado:** no hay una app conocida que una comunidad, partido en vivo y minijuegos PvP en una sola experiencia.
- **Personaje como identidad:** la personalización genera apego emocional y retención.
- **Modelo de energía:** limita la saturación y crea hábito de retorno (mecánica usada en juegos como Clash Royale y apps como Duolingo).
- **No pay-to-win:** genera confianza y una comunidad leal; sacrifica ingresos inmediatos pero construye valor a largo plazo.
- **Traducción automática:** conecta hinchas de cualquier país sin fricción.

### 22.2 Riesgos a gestionar
- **Dependencia de una API gratuita:** mitigado con la capa de abstracción del backend y una alternativa paga.
- **Masa crítica:** una app social vacía muere. Estrategia: lanzar con foco en un único club o liga y hacer una campaña muy dirigida.
- **Flame Engine para minijuegos:** requiere experiencia en desarrollo de juegos. Mitigado empezando por los más simples.

### 22.3 Veredicto
Si el MVP se ejecuta bien, con foco en una comunidad concreta y un chat fluido durante el partido, gameChat tiene potencial para ser la app que los hinchas abran antes, durante y después de cada partido.

---

## 23. Herramientas de IA para Generación de Assets

### 23.1 Personajes base y personalización
Como el avatar usará `CustomPaint`, las herramientas de IA (Midjourney, DALL-E) servirán para generar conceptos visuales que luego se vectorizan y se dividen en capas programables en Flutter. No se usarán sprites estáticos para los elementos dinámicos (piel, ropa, pelo).

### 23.2 Animaciones
Se usarán animaciones vectoriales o transformaciones de canvas interpoladas en Flutter. Para animaciones complejas se evaluará Rive u otra herramienta que exporte animaciones vectoriales controlables.

### 23.3 Íconos, escudos y UI
- **Midjourney:** fondos de estadio, iconografía, texturas de cancha.
- **Recraft.ai o IconifyAI:** sets de íconos consistentes.
- **Photopea:** edición final y recorte (gratuito, web).

### 23.4 Flujo de trabajo recomendado
1. Diseñar 3-4 personajes base con un ilustrador humano (o comprar assets con licencia comercial).
2. Usar Scenario.gg para generar las variaciones (clubes, selecciones, peinados).
3. Hacer a mano en Aseprite las animaciones críticas (patear, festejar, pelear) para garantizar la calidad.
4. Generar con IA los assets secundarios (canchas, pelotas, fondos).

---

## 24. Inversión Estimada y Planificación Temporal

> Esta sección estima lo que costaría construir el producto completo de forma profesional. El proyecto de estudio se desarrolla de forma individual y no tiene estos costos.

### 24.1 Escenarios de inversión para el MVP
Todas las cifras están en dólares estadounidenses y excluyen marketing y costos operativos posteriores al lanzamiento.

**Escenario A: Freelancers (Latinoamérica / Europa del Este)**

| Concepto | Costo estimado | Tiempo |
|---|---|---|
| Desarrollador Flutter + Flame (full-time) | USD 15.000 – 24.000 | 6 meses |
| Diseñador UX/UI (pantallas, flujos) | USD 3.000 – 5.000 | 2 meses, parcial |
| Ilustrador 2D (personajes base, sprites) | USD 2.000 – 4.000 | 2 meses, parcial |
| Hosting del backend + PostgreSQL (en desarrollo) | USD 0 – 50/mes | — |
| API deportiva | USD 0 (OpenLigaDB en MVP) → USD 99/mes (Sportmonks en producción) | — |
| Cuentas de desarrollador | Google Play: USD 25 (pago único) · Apple: USD 99/año | — |
| **Total** | **USD 20.000 – 33.000** | **6 meses** |

**Escenario B: Agencia pequeña (México, Colombia, España)**

| Concepto | Costo estimado | Tiempo |
|---|---|---|
| Equipo dedicado (3 personas: PM, desarrollador, diseñador/QA) | USD 30.000 – 50.000 | 4 meses |
| Assets visuales profesionales | USD 5.000 – 8.000 | Incluido |
| **Total** | **USD 35.000 – 58.000** | **4-5 meses** |

**Escenario C: Cofundador técnico (equity + salario bajo)**

| Concepto | Costo estimado | Tiempo |
|---|---|---|
| Salario mínimo + equity (30-40%) | USD 12.000 – 18.000 | 8-10 meses (part-time) |
| Diseñador freelance | USD 3.000 – 5.000 | — |
| **Total** | **USD 15.000 – 23.000** | **8-10 meses** |

### 24.2 Costos operativos posteriores al lanzamiento (mensuales)

| Servicio | Costo estimado |
|---|---|
| Hosting del backend + PostgreSQL + Redis (con usuarios) | USD 100 – 500/mes (estimado, según tráfico y proveedor) |
| API Sportmonks | USD 99 – 299/mes |
| Google Cloud Translation | Variable según volumen (ver sección 14.5) |
| Servidor WebSocket (si se escala a lucha 2D en tiempo real) | USD 50 – 200/mes |

### 24.3 Estimación de tiempos (desarrollador Flutter senior full-time)

| Fase | Con IA como copiloto | Sin IA |
|---|---|---|
| Onboarding + Auth + selección de club | 2 semanas | 4 semanas |
| Personalización de personaje | 3 semanas | 6 semanas |
| Chat efímero + simulador + traducción | 5 semanas | 10 semanas |
| Sistema RPG por turnos | 3 semanas | 6 semanas |
| Sistema de energía + recarga | 1 semana | 2 semanas |
| Backend propio (auth, base de datos, WebSockets) | 4 semanas | 8 semanas |
| Pencas + tareas programadas | 2 semanas | 4 semanas |
| Minijuegos (6) | 6 semanas | 12 semanas |
| Tienda + AdMob + suscripción | 2 semanas | 4 semanas |
| Rankings | 1 semana | 2 semanas |
| Testing, bugs y ajustes | 4 semanas | 8 semanas |
| Publicación | 1 semana | 2 semanas |
| **Total** | **~9 meses** | **~18 meses** |

> **Nota importante:** sin experiencia previa en Flutter, estos tiempos se multiplican por 3 o 4. La IA es un copiloto, no un piloto automático: no puede conectar todas las piezas, manejar estados globales complejos ni garantizar un producto sin errores en producción.

### 24.4 Recomendación de inversión
Para un MVP funcional con estas características, la opción óptima es un equipo reducido (1-2 desarrolladores + diseñador) con un presupuesto de **USD 25.000 – 40.000** y 6-8 meses de desarrollo. La IA puede reducir ese tiempo en un 40-50% si el equipo tiene experiencia previa.
