# syntax=docker/dockerfile:1.2
FROM python:3 AS builder


# Set the working directory in the container
WORKDIR /app

# Copy only the requirements file 
COPY requirements.txt .

# Install dependencies in a virtual environment to avoid polluting global space [4]
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Install only production dependencies [4]
RUN pip install --upgrade pip  && pip install -r requirements.txt

# Second stage for running the app
FROM python:3.10.12-slim-buster AS runner

# Copy the virtual environment from the builder stage [4]
COPY --from=builder /opt/venv /opt/venv

# Make sure we use the virtualenv
ENV PATH="/opt/venv/bin:$PATH"

# Set the working directory
WORKDIR /app

# Copy the application code 

COPY . .

# Run the application 
CMD ["python3", "src/main.py"]
