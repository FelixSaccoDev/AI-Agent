# Customer Support AI Agent  

## Overview  

The **Customer Support AI Agent** is a Python-based solution designed to monitor product prices on an e-commerce site. By utilizing an ARIMA model, it predicts future prices and sends notifications to customers when the price of a product is expected to drop in the next 10 days. This proactive approach helps customers make informed purchasing decisions and enhances their shopping experience.  

![Workflow Diagram](https://github.com/BigData5911/customer-support-ai-agent/blob/main/customer-ai-agent-workflow.png)  

## Features  

- Fetches a list of products from an e-commerce site  
- Implements ARIMA model for price prediction  
- Sends email notifications to users when product prices are predicted to be lower  
- User-friendly setup and configuration  

## Requirements  

- Python 3.6 or higher  
- Required libraries (install using `pip install -r requirements.txt`):  
  - pandas  
  - numpy  
  - statsmodels  
  - requests  
  - smtplib  
  - email  

## Installation  

1. Clone the repository:  

   ```bash  
   git clone https://github.com/bigdata5911/customer-support-ai-agent.git  
   cd customer-support-ai-agent
2. Install the required libraries:
   ```bash
   pip install -r requirements.txt  
   ```
3. Set up your email configuration in config.py:
    ```python
    EMAIL_ADDRESS = 'your_email@example.com'
    ```

## Contributing
Contributions are welcome! If you have suggestions for improvements or encounter issues, please create an issue or submit a pull request.

## Contact
For questions or feedback, please reach out via GitHub issues or email at worker.opentext@gmail.com.


### Customization Tips  
- Make sure to replace `yourusername`, `your_email@example.com`, and actual script names with your specific information.  
- Adjust the sections based on the actual structure and features of your project.   
- You might want to include screenshots or examples of how the system works for better clarity.
