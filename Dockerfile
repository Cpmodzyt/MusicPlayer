# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app/MusicPlayer

# Copy the current directory contents into the container at /app/MusicPlayer
COPY ./MusicPlayer /app/MusicPlayer

# Install any necessary dependencies
# Add a requirements.txt file to the MusicPlayer directory for this step
RUN pip install --no-cache-dir -r requirements.txt

# Set the command to execute the script
CMD ["python", "main.py"]
