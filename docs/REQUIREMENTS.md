# REQUIREMENTS.md

## Project Overview
**Project Name:** saas‑sentinel  
**Product Type:** AI‑powered user context & insights platform for SaaS applications  
**Goal:** Deliver actionable engagement & churn‑reduction insights to SaaS product teams through real‑time user context analysis, predictive modeling, and automated recommendation workflows.

---

## 1. Functional Requirements

| ID | Description | Priority | Acceptance Criteria |
|----|-------------|----------|---------------------|
| **FR‑1** | **User Data Ingestion** | P1 | • Accept event streams (webhooks, SDK logs, API calls) from supported SaaS platforms (e.g., Salesforce, HubSpot, Intercom). <br>• Store raw events in a time‑series database with minimal latency (< 200 ms). |
| **FR‑2** | **Contextual Enrichment** | P1 | • Enrich raw events with user profile data (demographics, subscription tier, usage history). <br>• Resolve user identifiers across multiple data sources. |
| **FR‑3** | **Feature Engine** | P1 | • Compute real‑time features (e.g., session length, feature adoption score, churn probability). <br>• Update features within 5 s of event ingestion. |
| **FR‑4** | **Predictive Models** | P1 | • Deploy pre‑trained churn & engagement models (scikit‑learn, XGBoost). <br>• Return probability scores with confidence intervals. |
| **FR‑5** | **Insight Generation** | P1 | • Generate actionable insights (e.g., “User X is at 70% churn risk; recommend onboarding email”). <br>• Deliver insights via REST API and web dashboard. |
| **FR‑6** | **Recommendation Engine** | P2 | • Suggest personalized actions (emails, in‑app messages, feature tours). <br>• Allow A/B testing of recommendation variants. |
| **FR‑7** | **Alerting & Notification** | P1 | • Trigger alerts (Slack, email, webhook) when churn risk > 80% or engagement drops > 30%. |
| **FR‑8** | **Dashboard UI** | P2 | • Visualize user segments, churn heatmaps, feature adoption trends. <br>• Provide drill‑down to individual user context. |
| **FR‑9** | **API Gateway** | P1 | • Expose secure endpoints for data ingestion, feature lookup, and insight retrieval. |
| **FR‑10** | **Data Retention & Export** | P2 | • Allow customers to export raw and enriched data (CSV, JSON) and to set retention policies (30‑365 days). |
| **FR‑11** | **User Management** | P2 | • Support multi‑tenant SaaS with role‑based access control (Admin, Analyst, Viewer). |
| **FR‑12** | **Audit & Logging** | P1 | • Log all API calls, model inferences, and user actions with timestamps for compliance. |
| **FR‑13** | **Model Retraining Pipeline** | P2 | • Automate periodic retraining (weekly) using new labeled data; deploy updated models with zero downtime. |
| **FR‑14** | **SDK Integration** | P2 | • Provide JavaScript & Python SDKs for easy event tracking in client applications. |
| **FR‑15** | **Compliance & Privacy** | P1 | • Ensure GDPR, CCPA, and other privacy regulations are met (data minimization, user opt‑out). |

---

## 2. Non‑Functional Requirements

| Category | Requirement | Metric |
|----------|-------------|--------|
| **Performance** | Real‑time ingestion latency | < 200 ms per event |
| | Feature computation latency | < 5 s per user |
| | API response time | < 150 ms (95th percentile) |
| **Scalability** | Handle 10 k events/s per tenant | Horizontal scaling via Kubernetes |
| | Support up to 1 M concurrent users | Auto‑scaling compute |
| **Reliability** | 99.9% uptime SLA | 99.9% MTBF |
| | Data durability | 3‑replica storage, geo‑redundant backups |
| **Security** | Authentication | OAuth 2.0 / JWT |
| | Encryption | TLS 1.3 for transport; AES‑256 at rest |
| | Access control | RBAC, audit logs |
| **Maintainability** | Code coverage | ≥ 90% unit tests |
| | Documentation | Auto‑generated API docs (OpenAPI) |
| | CI/CD | Automated tests, linting, and blue‑green deployments |
| **Compliance** | Data residency | Option to host in EU/US regions |
| | Privacy | Opt‑in/opt‑out flows, data deletion on request |
| **Usability** | Dashboard UI | Responsive, accessible (WCAG 2.1 AA) |
| | SDKs | Clear examples, versioning |

---

## 3. Constraints

1. **Existing Portfolio** – Must not duplicate functionality of Lemmy:programming’s iceoryx2 or any other Axentx product.  
2. **Technology Stack** – Must use the current Axentx tech stack: Python 3.11, FastAPI, PostgreSQL, Redis, Kafka, and Docker/Kubernetes.  
3. **Data Sources** – Only ingest data from SaaS platforms that provide official SDKs or webhooks; no scraping.  
4. **Modeling** – Models must be explainable (SHAP or LIME) to satisfy compliance.  
5. **Deployment** – Must run on the existing Axentx cloud infrastructure (AWS EKS) with no additional vendor lock‑in.

---

## 4. Assumptions

- SaaS customers will provide API keys and necessary permissions for event ingestion.  
- Event payloads conform to a standard JSON schema defined in the SDK.  
- Customers will manage their own user identifiers; the platform will only map identifiers internally.  
- The AI models will be trained on anonymized, aggregated data to preserve privacy.  
- The platform will be offered as a SaaS subscription with tiered pricing based on event volume and feature set.

---

## 5. Deliverables

1. **API Specification** – OpenAPI 3.0 document.  
2. **Data Model** – ER diagram for PostgreSQL.  
3. **Deployment Scripts** – Helm charts for EKS.  
4. **SDKs** – JavaScript and Python packages with documentation.  
5. **Dashboard** – React‑based UI with component library.  
6. **Testing Suite** – Unit, integration, and performance tests.  
7. **Compliance Report** – GDPR/CCPA audit checklist.  

---

## 6. Acceptance Criteria Summary

- All functional requirements are implemented and pass unit tests.  
- System meets performance, scalability, and reliability metrics under load testing.  
- Security and compliance checks pass internal audit.  
- Documentation is complete and publicly accessible.  
- Product demo shows real‑time insights and recommendation workflow.

---

*Prepared by: Senior Product/Engineering Lead – Axentx*
