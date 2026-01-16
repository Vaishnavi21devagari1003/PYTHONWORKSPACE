#Create the thread
import threading
import time

def cook_pasta():
    print("Starting to boil water...")
    time.sleep(3) # Simulating a task taking time
    print("Pasta is ready!")
thread1 = threading.Thread(target=cook_pasta)
thread2 = threading.Thread(target=cook_pasta)
thread3 = threading.Thread(target=cook_pasta)

# Start the thread
thread1.start() ## cook_pasta runs in the background
thread2.start()
thread3.start()
# Wait for it to finish before moving on
thread1.join() 
thread2.join()
thread3.join() 

print("Dinner is served!")
