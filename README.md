# 🧠 Customer Support AI Agent

## 📘 Overview

**Customer Support AI Agent** is a Python-based intelligent system that monitors product prices on e-commerce platforms and predicts future price trends using an **ARIMA time series model**.

When a price drop is forecasted within the next 10 days, the system automatically notifies users via email — helping customers make data-driven purchasing decisions and improving the overall shopping experience.

![Workflow Diagram](https://github.com/BigData5911/customer-support-ai-agent/blob/main/customer-ai-agent-workflow.png)

---

## 🚀 Key Features

* **Automated Product Monitoring:** Continuously fetches product data from supported e-commerce sites.
* **Predictive Price Analytics:** Utilizes ARIMA forecasting to estimate short-term price fluctuations.
* **Smart Notifications:** Sends email alerts when a product’s price is expected to decrease.
* **Easy Configuration:** Simple setup for custom thresholds, data sources, and email settings.

---

## ⚙️ Requirements

* **Python:** 3.6 or higher
* **Dependencies:**
  Install required libraries using:

  ```bash
  pip install -r requirements.txt
  ```

  Required packages include:

  * `pandas`
  * `numpy`
  * `statsmodels`
  * `requests`
  * `smtplib`
  * `email`

---

## 🧩 Installation & Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/bigdata5911/customer-support-ai-agent.git
   cd customer-support-ai-agent
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure email settings:**
   Update your credentials in `config.py`:

   ```python
   EMAIL_ADDRESS = 'your_email@example.com'
   EMAIL_PASSWORD = 'your_password'
   ```

---