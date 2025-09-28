# Inbound Carrier Sales API

API service for Acme Logistics’ inbound carrier sales automation proof of concept.
Built with **FastAPI**, containerized with **Docker**, and deployed on **Railway**.

This API powers the HappyRobot agent by verifying carriers and serving load data for automated carrier calls.

## 🚀 Features

* **Carrier Verification**
  Validate MC numbers against the FMCSA API.

* **Load Search**
  Find available loads by equipment type, with optional filters for origin, destination, and dates.

* **Load Details**
  Retrieve full information about a specific load by ID.

All endpoints are secured with an API key (`X-API-Key` header).


## 📦 Endpoints

### 1. Verify Carrier

```
GET /verify_carrier
```

**Description:** Verify a carrier’s MC number via the FMCSA API.

**Path Parameters:**

* `mc_number` (string, required) – Carrier’s MC number.

**Headers:**

* `X-API-Key: your_api_key`

**Response (200):**

```json
{
  "content": {
    "is_eligible": True,
    "mc_number": "123456",
    "carrier_name": "Rapid Trans Inc.",
    "datail": "Mock verification successful: Carrier is eligible."
  }
}
```

---

### 2. Search Loads

```
GET /search_loads
```

**Description:** Search for available loads by equipment type, with optional filters.

**Query Parameters:**

* `equipment_type` (string, required) – e.g. `"Reefer"`, `"Dry Van"`.
* `origin` (string, optional) – Pickup city/state.
* `destination` (string, optional) – Delivery city/state.
* `pickup_date` (string, optional, YYYY-MM-DD) – Pickup date.
* `delivery_date` (string, optional, YYYY-MM-DD) – Delivery date.

**Headers:**

* `X-API-Key: your_api_key`

**Response (200):**

```json
[
  {
    "load_id": "582103",
    "origin": "Madrid",
    "destination": "Barcelona",
    "equipment_type": "Reefer",
    "loadboard_rate": 950.00,
    "weight": 19000,
    "miles": 628,
    "pickup_datetime": "2025-09-28T08:00:00",
    "delivery_datetime": "2025-09-28T18:00:00",
    "notes": "Fruta refrigerada. Mantener a 2°C.",
    "commodity_type": "Cítricos",
    "num_of_pieces": 20,
    "dimensions": "120x80x160"
  }
]
```

**Response (404):**

```json
{"detail": "No loads found matching criteria"}
```

---

### 3. Get Load Details

```
GET /get_load_details
```

**Description:** Retrieve detailed information for a specific load.

**Query Parameters:**

* `load_id` (string, required) – Unique identifier for the load.

**Headers:**

* `X-API-Key: your_api_key`

**Response (200):**

```json
{
  "load_id": "582103",
  "origin": "Madrid",
  "destination": "Barcelona",
  "equipment_type": "Reefer",
  "loadboard_rate": 950.00,
  "weight": 19000,
  "miles": 628,
  "pickup_datetime": "2025-09-28T08:00:00",
  "delivery_datetime": "2025-09-28T18:00:00",
  "notes": "Fruta refrigerada. Mantener a 2°C.",
  "commodity_type": "Cítricos",
  "num_of_pieces": 20,
  "dimensions": "120x80x160"
}
```

**Response (404):**

```json
{"detail": "Load with ID '582103' not found."}
```

## 🛡️ Security

All endpoints require an API key provided via the `X-API-Key` header.

Example:

```bash
curl -H "X-API-Key: your_api_key" \
"https://your-deployment.up.railway.app/search_loads?equipment_type=Reefer"
```


## 🐳 Deployment

### Local (with venv)

```bash
pip install -r requirements.txt
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Docker

```bash
docker build -t carrier-api .
docker run -p 8000:8000 --env-file .env carrier-api
```

### Cloud (Railway)

```bash
railway up
```

## 📂 Project Structure

```
.
├── main.py                # FastAPI app entrypoint
├── api/
│   ├── routes/
│   │   ├── carriers.py    # /verify_carrier
│   │   └── loads.py       # /search_loads, /get_load_details
│   ├── data.py            # Loads mock DB
│   ├── models.py          # Pydantic models
│   └── security.py        # API key auth
├── loads_DB.json          # Load database
├── requirements.txt
├── Dockerfile
└── README.md
```

## 📖 License

MIT License – for challenge/demo purposes only.
