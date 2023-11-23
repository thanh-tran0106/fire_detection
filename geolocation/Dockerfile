FROM python:3.9-slim

# Set the working directory
WORKDIR /usr/src/app

# Copy the requirements file into the container
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application into the container
COPY local_authority.py .

# Expose the Flask port
EXPOSE 5000

# Run the application
CMD ["python", "local_authority.py"]

