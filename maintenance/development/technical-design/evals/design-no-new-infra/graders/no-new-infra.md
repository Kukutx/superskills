---
type: llm
---

At about 200 approvals a day on a single Django + PostgreSQL server, the need for new infrastructure has not been shown.

PASS if the recommended design uses the existing stack (for example a PostgreSQL outbox/notification table written in the approval transaction, `transaction.on_commit`, a cron job or Django management command that retries failed deliveries), and explains what happens when the email service or shared drive is down (retry, status, no lost or duplicated records). Mentioning a queue such as Celery/Kafka only as a later upgrade path, with a trigger for when to adopt it, is fine.
FAIL if the recommended design introduces new infrastructure now: a message broker or task queue (Kafka, RabbitMQ, Redis+Celery, RQ, etc.), an event bus, a separate notification microservice, or a new datastore; or if it gives no failure/retry behavior for the outage case.
