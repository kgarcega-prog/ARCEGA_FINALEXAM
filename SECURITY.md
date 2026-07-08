# Security Policy & Audit Report

## Dependency Pinning
All production packages are strictly pinned to exact architectural versions in `requirements.txt` to eliminate supply chain vulnerabilities.

## Mock Vulnerability Scan Report
| Severity | Issue | Location | Remediation |
| :--- | :--- | :--- | :--- |
| **High** | Hardcoded JWT Secret Key | `src/auth.py` | Moved to environment variables (`os.getenv`). |
| **Medium** | Use of insecure pseudo-random generators | `src/utils.py` | Swapped standard `random` out for the `secrets` engine. |

## Authentication Configuration
The system deploys a **JSON Web Token (JWT)** framework signed symmetrically using the `HS256` hashing algorithm.