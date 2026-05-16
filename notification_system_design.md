# Notification System Design

## Functional Requirements

- Email notifications
- SMS notifications
- In-app notifications

## Non Functional Requirements

- Scalability
- Reliability
- High availability

## Architecture

Client -> API -> Queue -> Worker -> Notification Provider

## Retry Mechanism

Failed notifications retry 3 times.

## Security

- JWT Authentication
- HTTPS
- Rate limiting