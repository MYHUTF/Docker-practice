# Use an official Python 3.12 slim image as the base image
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the game script into the container
COPY tic_tac_toe.py .

# Define the command to run the game
CMD ["python", "tic_tac_toe.py"]

