# ⚽ gameChat

**Red social móvil para hinchas de fútbol:** chats en vivo durante los partidos, minijuegos entre hinchas rivales y predicciones, todo con un personaje que te representa.

> 🎓 **Proyecto de estudio en desarrollo.** Lo construyo desde cero para reaprender frameworks y diseño de APIs, aprendiendo haciendo y documentando cada avance. El objetivo a largo plazo es que pueda convertirse en una aplicación funcional.

![Estado](https://img.shields.io/badge/estado-en%20desarrollo-yellow)
![Python](https://img.shields.io/badge/Python-FastAPI-009688)
![Flutter](https://img.shields.io/badge/Flutter-Dart-02569B)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-database-4169E1)
![Docker](https://img.shields.io/badge/Docker-compose-2496ED)

---

## 💡 La idea

gameChat busca que los hinchas vivan cada partido en comunidad:

- **Catarsis:** chat solo para los hinchas de tu equipo durante el partido.
- **Rivales:** chat compartido con la hinchada contraria, con traducción automática.
- **Minijuegos PvP y PvE:** penales, reacción rápida, "Quién domina más el balón" y más.
- **Pencas:** predicciones de resultados con moneda virtual (sin dinero real).
- **Personaje propio:** con los colores de tu club o tu selección.
- **Sin pay-to-win:** las monedas solo se ganan jugando.

El diseño completo del producto (historias de usuario, modelo de datos, arquitectura, monetización y riesgos) está en **[docs/arquitectura.md](docs/arquitectura.md)**.

---

## 🎯 ¿Por qué este proyecto?

Hice los fundamentos de programación en **Holberton School**. Ahora quiero recuperar y profundizar en frameworks y en la construcción de APIs propias, y la mejor forma que conozco es construir algo real.

Mis reglas para este proyecto:

1. **Aprender haciendo:** cada concepto se aprende al necesitarlo para construir una pieza real del proyecto.
2. **El código lo escribo yo.** Uso IA como profesor y revisor (me explica conceptos, me da pistas y revisa mi código), no como autor. Tengo que poder explicar y defender cada línea.
3. **Pasos pequeños y constantes:** 1 hora por día, todos los días.
4. **Compartir el proceso:** publico mis avances en LinkedIn al cerrar cada hito.

---

## 🗺️ Hoja de ruta

No voy a construir todo el producto de una vez. Primero construyo una **versión mínima de punta a punta**: elijo mi club, veo la cuenta regresiva de su próximo partido, entro al chat de mi hinchada y juego un minijuego. Cada etapa me enseña una tecnología nueva.

Los tiempos son estimados con 1 hora diaria (~7 horas por semana).

| Etapa | Qué construyo | Qué aprendo | Tiempo estimado | Estado |
|---|---|---|---|---|
| **0. Preparación** | Repositorio nuevo y ordenado, entorno de trabajo, licencia | Git y GitHub (ramas, commits, Pull Requests), entornos virtuales de Python, `.gitignore` y manejo de secretos | 1 semana | ✅ Completo |
| **1. Primera API** | API en FastAPI que consulta una API deportiva y devuelve el próximo partido de un club | HTTP y REST, FastAPI, modelos con Pydantic, consumir APIs externas, variables de entorno, tests con `pytest` | 3-4 semanas | 🟡 En curso |
| **2. Base de datos** | Clubes, partidos y usuarios guardados en PostgreSQL, con una tarea que sincroniza los partidos | SQL, Docker, PostgreSQL en Docker, SQLAlchemy, migraciones con Alembic, tareas programadas | 3-4 semanas | ⬜ Pendiente |
| **3. Autenticación** | Registro, login y perfil del usuario (elegir club y selección) | Hash de contraseñas, JWT (access y refresh tokens), rutas protegidas, seguridad básica de APIs | 2-3 semanas | ⬜ Pendiente |
| **4. App Flutter** | Onboarding, login, tema con los colores del club y Home con la cuenta regresiva del próximo partido, consumiendo **mi propia API** | Dart, widgets, navegación, manejo de estado con Riverpod, consumir una API desde el móvil | 4-6 semanas | ⬜ Pendiente |
| **5. Tiempo real** | Chat **Catarsis** durante el partido | WebSockets en FastAPI y en Flutter, salas, autorización por JWT | 3-4 semanas | ⬜ Pendiente |
| **6. Primer minijuego** | "Quién domina más el balón" contra la IA (3 niveles de dificultad) | Flame Engine, game loop, física simple, timers | 3-4 semanas | ⬜ Pendiente |
| **7. Energía** | Sistema de energía calculado y validado en el servidor | Lógica de negocio en el backend, transacciones en la base de datos | 1-2 semanas | ⬜ Pendiente |

**🏁 Hito 1 (versión mínima de punta a punta): ~5 a 7 meses.**

Después del Hito 1 vienen, en orden: el chat Rivales con traducción, el sistema de amigos, las pencas, más minijuegos, las peleas RPG y los rankings (ver [plan completo](docs/arquitectura.md#17-plan-de-implementación-mvp)).

---

## 🧱 Stack tecnológico

| Capa | Tecnología |
|---|---|
| App móvil (Android / iOS) | Flutter + Flame Engine |
| Estado de la app | Riverpod (patrón MVVM) |
| Backend (API propia) | Python + FastAPI (REST + WebSockets) |
| Base de datos | PostgreSQL + SQLAlchemy + Alembic |
| Autenticación | JWT + hash de contraseñas |
| Infraestructura | Docker + Docker Compose (Redis cuando haga falta escalar) |
| Datos deportivos | API pública de fútbol, consultada solo desde el backend |
| Testing | `pytest`, `flutter_test` |
| CI | GitHub Actions |

**¿Por qué un backend propio y no Firebase?** Firebase resuelve el backend por ti. Como mi objetivo es aprender a construir APIs, prefiero diseñar y entender cada pieza: la base de datos, el login, el tiempo real y la seguridad.

### Estructura prevista del repositorio

```text
gameChat/
├── backend/             # API en FastAPI (Etapas 1, 2, 3, 5 y 7)
├── app/                 # Aplicación Flutter (Etapa 4 en adelante)
├── docs/                # Documento de arquitectura y notas de aprendizaje
└── docker-compose.yml   # Levanta API + PostgreSQL con un solo comando
```

---

## 📓 Bitácora de avances

Registro semanal de lo que construí y aprendí. Cada hito tiene su publicación en LinkedIn.

| Semana | Fecha | Qué construí / aprendí | Publicación |
|---|---|---|---|
| 0 | Octubre 2026 | Documento de arquitectura del producto (backend propio) y plan de aprendizaje por etapas | https://lnkd.in/p/dn9KAWQa |
| 1 | 9-10 octubre 2026 | Inicio de la Etapa 1: API en FastAPI con las rutas `/` y `/salud` (health check) y documentación OpenAPI automática en `/docs`. Dependencias fijadas en `requirements.txt`. Primera integración con una API externa (football-data.org) usando `httpx`, con la API key en variables de entorno (`.env` excluido del repositorio y `.env.example` como referencia). Elección del proveedor de datos deportivos documentada en la arquitectura. | Pendiente |
| 2 | | | |

---

## 👤 Autor

**Emanuel Romero**: programador trainee, egresado de los fundamentos de programación de Holberton School.

- GitHub: [@padredemellis](https://github.com/padredemellis)
- LinkedIn: https://www.linkedin.com/in/luis-emanuel-romero-duarte/

---

> gameChat es un proyecto personal de estudio. No está afiliado a ningún club, liga ni federación de fútbol. La moneda virtual de la app no tiene valor real y no puede canjearse por dinero.
