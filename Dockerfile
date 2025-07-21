FROM python:3.12-alpine
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 5050

# Run the app when the container launches
# CMD ["python", "app.py"]
# Using Gunicorn for production-ready serving (more robust than Flask's dev server)
# First, add gunicorn to requirements.txt and install it:
# requirements.txt -> gunicorn==21.2.0
CMD ["gunicorn", "--bind", "0.0.0.0:5050", "main:app"]