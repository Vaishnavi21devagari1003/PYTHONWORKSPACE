import threading
import time

def cook_pasta():
    print("Starting to boil water...")
    time.sleep(3) # Simulating a task taking time
    print("Pasta is ready!")

cook_pasta();
