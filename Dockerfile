# Use an official Python 3.12 slim image as the base image
FROM python:3.12-slim

# Install any OS-level dependencies if needed (e.g., build tools, fonts, etc.)
# In many cases, dash apps work out-of-the-box with the slim image.
# Uncomment and modify the following line if you need extra packages:
# RUN apt-get update && apt-get install -y <package-name> && rm -rf /var/lib/apt/lists/*

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose the port that the Dash app will run on (default is 8050)
EXPOSE 8050

# Define the command to run your Dash app
CMD ["python", "app_final.py"]
