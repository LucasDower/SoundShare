import re

BUFFER_SIZE = 1024
CHUNK_SIZE = 200
SAMPLE_RATE = 44100

IP_REGEX = re.compile(r'\b(?:(?:2(?:[0-4][0-9]|5[0-5])|[0-1]?[0-9]?[0-9])\.){3}(?:(?:2([0-4][0-9]|5[0-5])|[0-1]?[0-9]?[0-9]))\b')