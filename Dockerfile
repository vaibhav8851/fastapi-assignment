# # Dockerfile

# # Use the official Python image
# FROM python:3.10-slim

# # Set the working directory
# WORKDIR /app

# # Copy the requirements.txt file into the container
# COPY requirements.txt .

# # Install the required packages
# RUN pip install --no-cache-dir -r requirements.txt

# # Copy the rest of the application code
# COPY . .

# # Expose the application port
# EXPOSE 8000

# # Command to run the application
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
