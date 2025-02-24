# Use an official Python 3.12 runtime as a parent image
FROM python:3.12-slim

# Install Tk (required for tkinter)
RUN apt-get update && apt-get install -y python3-tk && rm -rf /var/lib/apt/lists/*

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install any dependencies (if any)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Define the command to run your script
CMD ["python", "script.py"]

