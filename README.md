
# Flask API Project

This project is a basic Flask API that integrates with external APIs and MongoDB, providing JWT authentication, and includes a cache system to optimize API calls. The project also includes testing with Pytest.

## How to Run the API

### 1. Clone the Repository

First, clone the repository to your machine:

```bash
git clone https://github.com/0zymandi45/crypto-api.git
cd crypt-api
```

### 2. Create and Activate a Virtual Environment (Optional but Recommended)

Create a virtual environment to isolate the project dependencies:

- **Windows**:
  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```

- **macOS/Linux**:
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### 3. Install Dependencies

Install the project dependencies using `pip`:

```bash
pip install -r requirements.txt
```

### 4. Configure MongoDB

Ensure you have a MongoDB instance running (locally or via [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)) and update the `config.py` or `.env` file with your MongoDB connection URL.

### 5. Run the API

You can use the **Makefile** to run the API or run it directly using Flask.

#### Using Makefile:

```bash
make run
```

#### Without Makefile (direct Flask command):

```bash
flask run
```

This will start the Flask server, and the API will be available at `http://127.0.0.1:5000`.

### 6. Test the API

If your project has tests, you can run them using **Pytest**:

```bash
pytest
```

### 7. Access Swagger Documentation (If Configured)

If Swagger is configured, access the API documentation at `http://127.0.0.1:5000/swagger` or `http://127.0.0.1:5000/docs`.

## Project Structure

- `app/`
  - `__init__.py`: Initializes the Flask app.
  - `routes.py`: Defines the API routes.
  - `auth.py`: Manages JWT authentication.
  - `config.py`: Contains app configuration and constants.
  - `cache.py`: Implements the cache system.
  - `models.py`: Defines MongoDB models.
  
- `tests/`
  - Contains tests for routes and authentication.

- `requirements.txt`: Project dependencies.
- `README.md`: Documentation for the project.

## License

This project is licensed under the MIT License.
