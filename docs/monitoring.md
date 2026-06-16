# Monitoring & Observability

The platform includes production monitoring using Prometheus and Grafana.

---

## Prometheus Metrics

### Total Predictions

```text
email_predictions_total
```

### Spam Predictions

```text
spam_predictions_total
```

### Prediction Errors

```text
prediction_errors_total
```

### CPU Usage

```text
process_cpu_seconds_total
```

### Memory Usage

```text
process_resident_memory_bytes
```

### Prediction Latency

```text
prediction_latency_ms
```

---

## Grafana Dashboard

Public Dashboard:

https://prasannavaddeman.grafana.net/public-dashboards/f619b25a945540b2905c7afce72c9bf5

---

## Dashboard Panels

- Total Emails Processed
- Spam Predictions
- Prediction Errors
- Backend Status
- CPU Usage
- Memory Usage
- Prediction Latency

---

## Logging

Application logging captures:

- Prediction Requests
- Inference Events
- Database Operations
- Monitoring Events
- Exceptions

Log Location:

```text
logs/app.log
```

---

## Testing

Run:

```bash
pytest -v
```

Current Status:

```text
5 Passed
```