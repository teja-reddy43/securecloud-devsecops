\# SecureCloud — DevSecOps \& GitOps Platform



SecureCloud is a cloud-native DevSecOps project designed to demonstrate infrastructure as code, containerization, Kubernetes security, automated testing, and CI security scanning.



The project is being developed incrementally, starting with a working application and secure CI pipeline before expanding into GitOps deployment and observability.



\## Project Goals



\- Provision cloud infrastructure using Terraform.

\- Package an API application using Docker.

\- Deploy and secure workloads on Kubernetes.

\- Automate testing and security checks with GitHub Actions.

\- Introduce GitOps deployment using Argo CD.

\- Add monitoring, dashboards, and operational testing.



\## Architecture



```text

Developer

&#x20;  |

&#x20;  v

GitHub Repository

&#x20;  |

&#x20;  v

GitHub Actions CI

&#x20;  |

&#x20;  +--> Python API Tests

&#x20;  +--> Gitleaks Secret Scanning

&#x20;  +--> Semgrep Static Analysis

&#x20;  +--> Trivy Container Vulnerability Scan

&#x20;  |

&#x20;  v

Docker Image

&#x20;  |

&#x20;  v

Planned: Container Registry

&#x20;  |

&#x20;  v

Planned: Argo CD GitOps

&#x20;  |

&#x20;  v

Kubernetes Application

&#x20;  |

&#x20;  v

Planned: Prometheus / Grafana / Logging

```



\## Technology Stack



\- \*\*Application:\*\* Python, FastAPI, pytest

\- \*\*Containers:\*\* Docker

\- \*\*Infrastructure as Code:\*\* Terraform, AWS VPC

\- \*\*Orchestration:\*\* Kubernetes

\- \*\*CI/CD:\*\* GitHub Actions

\- \*\*Security:\*\* Gitleaks, Semgrep, Trivy

\- \*\*Planned:\*\* GitHub Container Registry, Argo CD, Prometheus, Grafana, Loki/OpenTelemetry



\## Current Implementation Status



\### Completed



\- FastAPI application and API tests.

\- Dockerfile and local image build.

\- Terraform-based AWS VPC foundation in `us-east-1`.

\- Kubernetes deployment and security manifests for local Kubernetes.

\- GitHub Actions workflow with four passing jobs:

&#x20; - Python Tests

&#x20; - Secret Scanning (Gitleaks)

&#x20; - Static Application Security Testing (Semgrep)

&#x20; - Container Vulnerability Scan (Trivy)



\### In Progress



\- Verification of Kubernetes NetworkPolicy enforcement.

\- Publishing versioned container images.

\- GitOps deployment with Argo CD.

\- Monitoring, logging, and reliability tests.



\## CI Security Pipeline



On pushes and pull requests targeting `main`, GitHub Actions runs the configured test and security jobs.



| Check | Purpose |

|---|---|

| Python Tests | Run automated API tests |

| Gitleaks | Detect potential secrets in repository history and content |

| Semgrep | Run static application security rules |

| Trivy | Scan the container image for operating-system and library vulnerabilities |



The Trivy job enforces failure for detected HIGH and CRITICAL findings under its configured policy. The workflow excludes pip's embedded SBOM file from scanning to avoid stale package metadata being treated as installed dependencies; the actual image and installed package versions should still be validated during security reviews.



\## Local Development



\### Prerequisites



\- Python 3.13

\- Docker Desktop

\- Git



\### Run the tests



```bash

python -m pip install -r app/requirements.txt

python -m pytest -v

```



\### Build the Docker image



```bash

docker build -t securecloud-api:local .

```



\### Run the container



```bash

docker run --rm -p 8000:8000 securecloud-api:local

```



The API should be available at `http://localhost:8000`. FastAPI's interactive documentation is typically available at `http://localhost:8000/docs`.



\## Security and Operational Notes



\- Dependency constraints were added after Trivy identified vulnerable Python package versions.

\- Container package versions were verified inside the built image.

\- The CI pipeline was rerun after the dependency changes and workflow cleanup.

\- Kubernetes NetworkPolicy enforcement must be validated against the local cluster's networking implementation before claiming isolation is effective.

\- Terraform state and secrets must not be committed to the repository.



\## Roadmap



1\. Publish versioned Docker images to GitHub Container Registry.

2\. Deploy through Argo CD using GitOps.

3\. Add Prometheus metrics and Grafana dashboards.

4\. Add logging and reliability/failure tests.

5\. Complete architecture documentation and operational evidence.



\## Repository



\[SecureCloud on GitHub](https://github.com/teja-reddy43/securecloud-devsecops)



\---



\*\*Project status:\*\* Active development. The CI security pipeline is operational; GitOps deployment and observability are planned next.

