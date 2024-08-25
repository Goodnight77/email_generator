# CrewAI Email Generator

## Project Overview

This project provides a tool for generating personalized email templates for potential candidates during the hiring process. The tool can be used to send out interview invitations, confirmation emails, and other relevant communications.

## Features

- **Personalized Email Templates:** Generates emails tailored to each candidate's information.
- **Email Management:** Manages a directory of pre-written email templates.
- **Email Sending Functionality:** Facilitates the sending of generated emails to candidates.

## Installation

**Using Pip (Recommended)**

1. **Create a virtual environment:**
   ```bash
   python -m venv env
   source env/bin/activate 
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

**Manual Installation**

1. **Install Python:** Ensure you have Python installed on your system.
2. **Install Required Packages:** Install the following packages using pip:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Prepare Email Templates:**
   - Create your email templates in the `emails` directory.
   - Each template should be a separate text file with the candidate's name in the filename (e.g., `Amine Manai_interview_email.txt`).

2. **Run the Script:**
   - Open a terminal and navigate to the project directory.
   - Execute the `main.py` script:
      ```bash
      python main.py
      ```
   - The script will generate personalized emails based on the templates and send them to the respective candidates (if the `send_email.py` script is configured).

**Example:**

To send an interview invitation email to Amine Manai, you would create a template file named `Amine Manai_interview_email.txt` in the `emails` directory. The script would then use this template to generate a personalized email addressed to Amine Manai and send it to his email address.

## Contributing

Contributions are welcome! Please feel free to open issues or submit pull requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
