FROM python:3 AS build

# Copy your utility scripts or modules into the utils directory
COPY . .

RUN pip install -r requirements.txt

# Set the PYTHONPATH environment variable to include the utils directory
ENV PYTHONPATH="${PYTHONPATH}:/src/utils"

# Your application's entrypoint or command
CMD ["python", "src/main.py"]