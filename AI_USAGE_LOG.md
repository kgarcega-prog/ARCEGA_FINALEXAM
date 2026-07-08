# AI Usage Log

## Interaction 1: Microservice Architectural Structure
* **Prompt:** "Design an enterprise Python Strategy Pattern setup to manipulate arrays dynamically."
* **AI Output:** Supplied structural blueprints.
* **Manual Verification:** Adjusted class names and injected explicit typing parameter rules (`List[int]`) to maintain standard compliance.

## Interaction 2: JWT Security Strategy
* **Prompt:** "Write a Python helper using PyJWT to sign payloads safely with HS256."
* **AI Output:** Provided standard token generation snippets.
* **Manual Verification:** Replaced `datetime.datetime.utcnow()` (deprecated) with timezone-aware `datetime.datetime.now(datetime.timezone.utc)` signatures.