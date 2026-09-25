# Sklep – Aplikacja Webowa Flask

Aplikacja napisana w mikro-frameworku Flask realizująca podstawowe funkcjonalności tras dynamicznych, obsługę błędów HTTP oraz operacje na danych zgodnie ze standardami PEP 8, dokumentacją docstring/type hints oraz konwencją Conventional Commits.

## Struktura projektu

```text
.
├── app.py                  # Główny plik aplikacji (notatki z lekcji)
├── kopia_z_zadaniami.py    # Wersja rozszerzona z dodatkowymi trasami i zadaniami
├── requirements.txt        # Zależności projektu
└── README.md               # Dokumentacja projektu
```

## Instrukcja uruchomienia

1. **Stwórz i aktywuj środowisko wirtualne:**
   ```bash
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   # Linux/macOS:
   source venv/bin/activate
   ```

2. **Zainstaluj zależności:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Uruchom aplikację:**
   ```bash
   python app.py
   # lub wersję z zadaniami:
   python kopia_z_zadaniami.py
   ```

---

## Tabela tras (Endpoints)

| Metoda | Adres | Opis | Przykładowe kody HTTP |
| :--- | :--- | :--- | :--- |
| **GET** | `/` | Strona główna | 200 OK |
| **GET** | `/about` | Informacje o nas | 200 OK |
| **GET** | `/contact` | Dane kontaktowe | 200 OK |
| **GET** | `/secret` | Trasa chroniona | 403 Forbidden |
| **GET** | `/api/status` | Status aplikacji w formacie JSON | 200 OK |
| **GET** | `/greet/<name>` | Powitanie po imieniu | 200 OK |
| **GET** | `/greet/<name>/<int:age>`* | Powitanie z podaniem wieku | 200 OK |
| **GET** | `/user/<first_name>/<last_name>` | Dane użytkownika | 200 OK |
| **GET** | `/add/<int:a>/<int:b>` | Dodawanie dwóch liczb | 200 OK |
| **GET** | `/subtract/<int:a>/<int:b>`* | Odejmowanie dwóch liczb | 200 OK |
| **GET** | `/multiply/<int:a>/<int:b>`* | Mnożenie dwóch liczb | 200 OK |
| **GET** | `/divide/<int:a>/<int:b>` | Dzielenie (z obsługą b=0) | 200 OK, 400 Bad Request |
| **GET** | `/power/<int:a>/<int:b>`* | Potęgowanie | 200 OK |
| **GET** | `/times-table/<int:n>`* | Tabliczka mnożenia (n: 1–20) | 200 OK, 400 Bad Request |
| **GET** | `/welcome` | Powitanie z Query String (`name`, `hour`) | 200 OK |
| **GET** | `/links` | Generowanie URL do szczegółów | 200 OK |
| **GET** | `/old-address` | Przekierowanie na `/` | 302 Found |
| **GET** | `/start`* | Przekierowanie na `/` | 302 Found |
| **GET** | `/products`* | Lista wszystkich produktów | 200 OK |
| **GET** | `/products/<int:product_id>` | Szczegóły produktu | 200 OK, 404 Not Found |

*\* Trasy obecne dodatkowo w pliku `kopia_z_zadaniami.py`.*

---

## Wyniki lintera (Ruff)

- **Liczba znalezionych problemów:** 12 (nieużywane importy, polskie nazwy identyfikatorów, formatowanie wcięć i spacji).
- **Rozwiązanie:** Błędy zostały naprawione przy użyciu komend `ruff check --fix` oraz sformatowane przez `ruff format .`.

---

## Bezpieczny GET

Metody GET w naszej aplikacji służą wyłącznie do odczytu i pobierania danych. Zgodnie ze specyfikacją HTTP i zasadami REST, żaden punkt końcowy typu GET nie modyfikuje, nie tworzy ani nie usuwa zasobów w bazie.

---

## Definition of Done (Lista kontrolna)

- [x] Aplikacja uruchamia się z czystego klonu (`pip install -r requirements.txt`, `python app.py`).
- [x] Nazwy zmiennych, funkcji, klas i tras są po angielsku, zgodnie z PEP 8.
- [x] `ruff check` nie zgłasza błędów, `ruff format` nie wprowadza dalszych zmian.
- [x] Każda funkcja widoku posiada docstring oraz type hints.
- [x] Żaden `GET` nie modyfikuje danych.
- [x] Nieistniejący zasób zwraca kod `404`, a nieprawidłowe dane `400` (brak `500`).
- [x] Plik `.gitignore` wyklucza `venv/`, `instance/`, `*.db`, `__pycache__/`, `.env`.
- [x] README zawiera opis, instrukcję uruchomienia, strukturę i tabelę tras.
- [x] Commity są małe, po angielsku i zgodne z Conventional Commits.