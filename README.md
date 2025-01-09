# Project Overview

This project is a Python-based application that manages GitHub interactions, handles a database, and serves a web interface.

## Setup

1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Set up the environment variables by copying `.env.template` to `.env` and filling in the necessary values.

3. Initialize the database:
   ```bash
   sqlite3 database/database.db < database/schema.sql
   ```

4. Run the web server:
   ```bash
   python src/server.py
   ```

## Project Structure

- `database/`: Contains database-related files.
- `src/`: Contains the main source code.
- `templates/`: HTML templates for the web interface.

## Requirements

- Python 3.x
- Flask
- Requests
- SQLAlchemy

## License

This project is licensed under the MIT License.
