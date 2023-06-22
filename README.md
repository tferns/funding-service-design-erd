# funding-service-design-erd

## Setup

Install graphviz and add bin to path: https://graphviz.org/download/

```bash
python -m venv .venv
.venv/Scripts/python -m pip install -r requirements.txt
.venv/Scripts/python create_erd_images.py
```

## Diagrams

<!-- ERD Start -->

### Account_store:
![erds/account_store.png](erds/account_store.png)

### Fund_store:
![erds/fund_store.png](erds/fund_store.png)

### Assessment_store:
![erds/assessment_store.png](erds/assessment_store.png)

### Application_store:
![erds/application_store.png](erds/application_store.png)

<!-- ERD End -->
