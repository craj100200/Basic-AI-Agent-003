FROM python:3.12-slim

# Install ffmpeg (required by MoviePy)
RUN apt-get update && apt-get install -y ffmpeg && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the test script
COPY test_moviepy.py .

# Run the test script
CMD ["python", "test_moviepy.py"]
