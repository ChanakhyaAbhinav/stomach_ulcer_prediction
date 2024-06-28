
FROM python:3.9-slim

# Set the working directsory in the container
WORKDIR /usr/src/app


COPY requirements.txt ./

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Make port 8501 available to the world outside this container (Streamlit's default port)
EXPOSE 8501

# Run the application
CMD ["streamlit", "run", "app.py"]
