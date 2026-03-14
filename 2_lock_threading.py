import multiprocessing
import threading
import time
import requests  # Assuming you have the requests library installed
 
def download_data(url):
  """Downloads data from a URL."""
  response = requests.get(url)
  return response.content
 
def process_data(data):
  """Performs some CPU-bound calculations on the downloaded data."""
  # Simulate some calculations by sleeping for a bit
  time.sleep(2)  # Adjust this based on your actual processing time
  return f"Processed data: {len(data)} bytes"
 
def handle_request(url):
  """Handles a user request by downloading data and processing it."""
  # Download data in a separate thread
  download_thread = threading.Thread(target=download_data, args=(url,))
  download_thread.start()
 
  # Optionally, perform some other tasks in the main thread while waiting for download
  # ...
 
  # Wait for the download to finish and retrieve the data
  data = download_thread.join(timeout=5)  # Set a timeout to avoid deadlocks
  if data is None:
      print(f"Download timed out for {url}")
      return
 
  # Process the downloaded data
  result = process_data(data)
  return result
 
if __name__ == "__main__":
  # Define URLs to process
  urls = ["https://450dsa.com/backtracking", "https://www.google.com/"]
 
  # Create a pool of worker processes
  pool = multiprocessing.Pool()
 
  # Use map_async to submit requests to the pool asynchronously
  results = pool.map_async(handle_request, urls)
 
  # Retrieve the results from the AsyncResult objects
  for result in results.get():
    print(result)
 
  # Close the pool to release resources
  pool.close()
  pool.join()
 
  print("All requests processed.")



# import multiprocessing
# import threading
# import requests  # Assuming you have the requests library installed
# import time
 
# # Sample data for 10 cells (replace with your actual data)
# data = [f"Cell {i+1} data" for i in range(10)]
 
 
# def process_data(cell_data):
#   """Processes data for a single cell (replace with your actual processing logic)."""
#   # Simulate some processing by sleeping for a bit
#   time.sleep(1)  # Adjust this based on your processing time
#   print("Processes Data")
#   return f"Processed: {cell_data}"
 
 
# def send_request_with_data(processed_data):
#   """Sends a request to a server with the processed data and retrieves the output."""
#   url = "https://450dsa.com/backtracking"  # Replace with your actual URL
#   response = requests.post(url, data={"data": processed_data})
#   return response.text
 
 
# def process_and_send_requests(processed_data):
#   """Sends a request with the provided processed data and retrieves the output."""
#   output = send_request_with_data(processed_data)
#   print(f"Output for {processed_data}: {output}")
 
 
# if __name__ == "__main__":
#   # Use multiprocessing to process data for each cell
#   pool = multiprocessing.Pool()
#   processed_data = pool.map(process_data, data)
#   pool.close()
#   pool.join()
#   print("All data processed.")
#   print(processed_data)
 
#   # Use threading to send requests concurrently for each processed data
#   threads = []
#   for item in processed_data:
#     thread = threading.Thread(target=process_and_send_requests, args=(item,))
#     threads.append(thread)
#     thread.start()
 
#   # Wait for all threads to finish
#   for thread in threads:
#     thread.join()
 
#   print("All requests sent and outputs printed.")