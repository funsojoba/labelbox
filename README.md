# Labelbox Project

## Project Description
This project is designed to integrate with Labelbox, a platform for managing and labeling data for machine learning. The goal is to streamline the process of data annotation and improve the efficiency of training machine learning models.


## Getting Started

### Prerequisites
- Python 3.7 or higher
- Labelbox account and API key

### Installation
1. Clone the repository:
    ```
    git clone https://github.com/funsojoba/labelbox.git
    cd labelbox-project
    ```

2. Create a virtual environment and activate it:
    ```
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required dependencies:
    ```
    pip install -r requirements.txt
    ```

### Configuration
1. Create a `.env` file in the root directory and add your Labelbox API key:
    ```env
    LABELBOX_API_KEY=your_api_key_here
    ```

### Usage
1. Run the main script to start the project:
    ```bash
    python manage.py runserver
    ```


