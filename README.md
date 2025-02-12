![IQ24](/assets/images/tux.png)

# **IQ24.ai**

**AI Agents Revolutionizing Prospecting & Outreach, 24/7.**

![GitHub License](https://img.shields.io/badge/license-MIT-blue.svg) ![GitHub Issues](https://img.shields.io/github/issues/dabistech/IQ24.ai) ![GitHub Stars](https://img.shields.io/github/stars/dabistech/IQ24.ai)

---

## **Overview**

IQ24.ai is an AI-powered B2B prospecting and outreach platform that automates lead generation, validation, personalization, and campaign execution. Built on a modular multi-agent architecture, it leverages advanced AI models like DeepSeek R1 to deliver hyper-personalized outreach at scale.

This project is a proof of concept designed for businesses looking to streamline their sales workflows and improve conversion rates. It integrates seamlessly with external APIs (e.g., LinkedIn, Hunter.io, Twilio) and CRMs (e.g., HubSpot, Salesforce).

<Image src="/assets/dashboard-screenshot.png" alt="IQ24.ai Dashboard" width={800} height={400} />

---

## **Key Features**

- **Autonomous Lead Discovery**: Extracts qualified leads from platforms like LinkedIn Sales Navigator.
- **Validation & Enrichment**: Validates emails, phone numbers, and enriches lead data with metadata.
- **Hyper-Personalization**: Generates tailored outreach messages using advanced NLP models.
- **Multi-Channel Campaigns**: Executes campaigns via email, SMS, WhatsApp, and LinkedIn InMail.
- **Analytics & Feedback Loops**: Tracks engagement metrics and refines workflows based on performance.
- **Compliance Guardian**: Ensures all communications comply with GDPR, CAN-SPAM, and platform-specific guidelines.

---

## **Table of Contents**

1. [Setup](#setup)
2. [Usage](#usage)
3. [Running IQ24.ai](#running-iq24ai)
4. [Project Structure](#project-structure)
5. [Contributing](#contributing)
6. [Feature Requests](#feature-requests)
7. [License](#license)

---

## **Setup**

### **Prerequisites**
- Python 3.9+
- Poetry (dependency manager)
- API keys for external services (LinkedIn, Hunter.io, Twilio, SendGrid, etc.)

### **Clone the Repository**
```bash
git clone https://github.com/dabistech/IQ24.ai.git
cd IQ24.ai
```

### **Install Dependencies**
```sh
curl -sSL https://install.python-poetry.org | python3 -
poetry install
```

### **Set Up Environment Variables**
Create a ``.env`` file from the example:
```bash
cp .env.example .env
```
Set your API keys in the ``.env`` file:
```bash
OPENAI_API_KEY=your-openai-api-key
GROQ_API_KEY=your-groq-api-key
LINKEDIN_API_KEY=your-linkedin-api-key
HUNTER_IO_API_KEY=your-hunter-io-api-key
TWILIO_ACCOUNT_SID=your-twilio-account-sid
TWILIO_AUTH_TOKEN=your-twilio-auth-token
SENDGRID_API_KEY=your-sendgrid-api-key
```

---
# Usage
## **Running IQ24.ai**
Execute the full workflow with the following command:

```bash
poetry run python src/main.py --query "CTOs in Berlin SaaS startups"
```
##### Example Output :

```bash
🔍 Prospect Discovery Agent: Found 50 leads.
✅ Validation & Enrichment Agent: Validated 45 emails and enriched with metadata.
📝 Outreach Personalization Agent: Generated personalized messages for 45 leads.
📧 Campaign Execution Agent: Sent 45 emails via SendGrid.
📊 Analytics & Feedback Loop Agent: Tracked open rate = 35%, reply rate = 10%.
🔒 Compliance Guardian Network: All messages comply with GDPR.
```
##### Optional Flags
``--show-reasoning:`` Print the reasoning of each agent to the console.
``--start-date and --end-date:`` Run campaigns for a specific time period
##### Example :
```bash
poetry run python src/main.py --query "CTOs in Berlin SaaS startups" --show-reasoning --start-date 2024-01-01 --end-date 2024-03-01
```
#### Running the Backtester
Simulate campaign performance over historical data:
```bash
poetry run python src/backtester.py --query "CTOs in Berlin SaaS startups" --start-date 2024-01-01 --end-date 2024-03-01
```
##### Example Output :
```bash
📊 Backtester Results:
- Total Leads: 50
- Emails Sent: 45
- Open Rate: 35%
- Reply Rate: 10%
- Conversion Rate: 5%
```
---

## Project Structure
```bash
IQ24.ai/
├── src/                          # Core source code
│   ├── agents/                   # AI agent modules
│   │   ├── prospect_discovery.py # Prospect Discovery Agent (PDA)
│   │   ├── validation_agent.py   # Validation & Enrichment Agent (VEA)
│   │   ├── outreach_agent.py     # Outreach Personalization Agent (OPA)
│   │   ├── campaign_executor.py  # Campaign Execution Agent (CEA)
│   │   ├── analytics_agent.py    # Analytics & Feedback Loop Agent (AFLA)
│   │   ├── compliance_agent.py   # Compliance Guardian Network (CGN)
│   │   └── lead_scoring.py       # Lead scoring and prioritization logic
│   ├── data/                     # Data storage and processing
│   │   ├── raw/                  # Raw data from APIs (e.g., LinkedIn, Hunter.io)
│   │   ├── processed/            # Processed and cleaned data
│   │   ├── embeddings/           # Precomputed embeddings for leads
│   │   └── datasets/             # Custom datasets for training models
│   ├── graph/                    # Graph-based reasoning and relationship mapping
│   │   ├── network_analysis.py   # Analyze interconnected professional networks
│   │   ├── relationship_mapper.py# Map relationships between leads and companies
│   │   └── graph_utils.py        # Utility functions for graph operations
│   ├── llm/                      # Large Language Model integrations
│   │   ├── deepseek_r1.py        # DeepSeek R1 integration for personalization
│   │   ├── gpt_integration.py    # GPT integration for fallback or testing
│   │   └── fine_tuning.py        # Fine-tuning scripts for custom datasets
│   ├── tools/                    # External API wrappers and utilities
│   │   ├── api_wrapper.py        # Wrappers for LinkedIn, Hunter.io, Twilio, etc.
│   │   ├── crm_wrapper.py        # CRM integrations (HubSpot, Salesforce)
│   │   └── email_tools.py        # Email/SMS sending utilities
│   ├── utils/                    # General-purpose utility functions
│   │   ├── encryption.py         # AES-256 encryption for sensitive data
│   │   ├── logging.py            # Centralized logging system
│   │   ├── config_loader.py      # Load configuration files (YAML, JSON)
│   │   └── data_processor.py     # Data cleaning and preprocessing utilities
│   ├── main.py                   # Main entry point for the application
│   └── backtester.py             # Backtesting tools for campaign simulation
├── notebooks/                    # Jupyter notebooks for experimentation
│   ├── nlp_experiments.ipynb     # NLP model experiments (DeepSeek R1, GPT)
│   ├── data_analysis.ipynb       # Data exploration and visualization
│   └── fine_tuning.ipynb         # Fine-tuning workflows for LLMs
├── tests/                        # Testing suite
│   ├── unit_tests/               # Unit tests for individual modules
│   │   ├── test_prospect_discovery.py
│   │   ├── test_validation_agent.py
│   │   └── test_outreach_agent.py
│   ├── integration_tests/        # Integration tests for workflows
│   │   └── test_workflow.py
│   └── test_runner.py            # Script to run all tests
├── data/                         # Persistent data storage
│   ├── logs/                     # Application logs
│   ├── backups/                  # Database backups
│   └── exports/                  # Exported reports (CSV, JSON)
├── docs/                         # Documentation
│   ├── architecture.md           # System architecture details
│   ├── api_usage_guide.md        # API usage guides
│   ├── contributing.md           # Contribution guidelines
│   └── testing_guide.md          # Testing framework documentation
├── .github/                      # GitHub Actions workflows
│   └── workflows/
│       ├── ci.yml                # Continuous Integration pipeline
│       └── deploy.yml            # Deployment pipeline
├── .env                          # Environment variables (API keys, secrets)
├── requirements.txt              # Python dependencies
├── pyproject.toml                # Poetry configuration
├── README.md                     # Project overview and setup instructions
└── LICENSE                       # License file
```
---


## Contributing
We welcome contributions! To contribute:

1. Fork the repository.
2. Create a feature branch:
```bash
git checkout -b feature/your-feature-name
```
3. Commit your changes:
```bash
git commit -m "Add your feature description"
```
4. Push to the branch:
```bash
git push origin feature/your-feature-name
```
5. Create a Pull Request.
**Important** : Keep pull requests small and focused for easier review.

---
## Feature Requests
If you have a feature request, please open an issue and tag it with ``enhancement``.

---

## License
This project is licensed under the MIT License - see the **[LICENSE](#)** file for details.

---
## Contact
For questions or feedback, feel free to reach out:

Email : info@ai42.ai
GitHub Issues :  **[Open an Issue](https://github.com/dabistech/IQ24.ai/issues?spm=5aebb161.18f1a4c6.0.0.73b22e8c1uV0Pd)**

![Tux, the Linux mascot](/assets/images/tux.png)


