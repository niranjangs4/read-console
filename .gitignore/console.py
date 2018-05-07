import io
import time
import subprocess
import sys,os


filename = 'test.log'
with io.open(filename, 'wb') as writer, io.open(filename, 'rb', 1) as reader:
    process = subprocess.Popen('"tool"', stdout=writer, shell = True)
    while process.poll() is None:
        sys.stdout.write(reader.read())
        time.sleep(0.5)
    # Read the remaining
    sys.stdout.write(reader.read())
