# PadelBook

**A booking API for a padel club, where two players can never book the same court at the same time.**

Built for the *Unified Process & Agile approaches* course at INSAT, following the Unified Process (inception, then elaboration iterations), with tagged milestones (`v0.0-inception`, `v0.1-elaboration`).

## The problem

Players book courts by phone, which leads to double bookings and lost time slots. PadelBook lets players check availability, book and pay online, and lets the club manager manage courts and slots.

## What is implemented

The elaboration iteration focuses on the riskiest use case first: **UC3 — Book a slot**.

- `POST /reservations` books a slot for a player:
  - **201** — slot booked (status `EN_ATTENTE_PAIEMENT`, waiting for payment);
  - **409** — the slot was already taken;
  - **404** — the slot does not exist.
- **No double booking, even under concurrency.** The slot is claimed with a single atomic SQL statement inside a transaction:

  ```sql
  UPDATE creneaux SET statut = 'RESERVE' WHERE id = ? AND statut = 'LIBRE'
  ```

  One modified row means the slot was free; zero means someone else was faster.
- **Proven by a test:** 10 players book the same slot simultaneously → exactly **1 success and 9 conflicts**.

## Architecture

Layered, each layer only talks to the one below:

```
HTTP request → Controller → Service → Repository → SQLite
```

| Layer | Role |
|---|---|
| Controller | receives the request, calls the service, returns 201 / 404 / 409 |
| Service | business rules and transaction |
| Repository | SQL reads and writes |

Design documents (in French) are in [`docs/`](docs/): vision and use-case prioritization, use-case diagram (PlantUML), base architecture.

## Stack

Python 3.12 · FastAPI · SQLite · pytest · GitHub Actions (tests on every push)

## Run it

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload   # API on http://localhost:8000 (docs at /docs)
pytest -v                       # tests, including the concurrency test
```

## Roadmap

Next iterations: online payment (UC4), availability (UC2), cancellation (UC5), authentication (UC1) and court management (UC6).
