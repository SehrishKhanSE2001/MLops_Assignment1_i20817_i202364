# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /MLops_Assignment1_i20817_i202364

# Copy the current directory contents into the container at /MLops_Assignment1_i20817_i202364
COPY . /MLops_Assignment1_i20817_i202364

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Expose the port the app runs on
EXPOSE 8080

# Run script.py when the container launches
CMD ["python", "script.py"]
