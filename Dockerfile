# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Python code to the working directory
COPY . .

# Install the required dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
        libxcb-xinerama0 \
        && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir pyqt5

# Run the Python script
CMD [ "python", "notepad.py" ]
