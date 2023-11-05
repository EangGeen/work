## Python压力测试：



###### 原理：使用多进程、多线程的方式对URL进行访问，以达到压测的目的，可用于接口测试。

###### 1.多线程代码：

```python
import logging
import threading
import multiprocessing

# 配置日志
logging.basicConfig(filename="e:\\log\\custom_logging.log", level=logging.INFO, format="%(asctime)s - %(message)s")

def thread_task(process_id, thread_id):
    log_message = f"Process-{process_id}, Thread-{thread_id}"
    logging.info(log_message)

def process_task(process_id, num_threads):
    for thread_id in range(1, num_threads + 1):
        thread = threading.Thread(target=thread_task, args=(process_id, thread_id))
        thread.start()
        thread.join()

if __name__ == "__main__":
    num_processes = 3
    num_threads = 4

    processes = []
    for process_id in range(1, num_processes + 1):
        process = multiprocessing.Process(target=process_task, args=(process_id, num_threads))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()


```

1.1 out:

```
2023-11-05 18:43:48,199 - Process-1, Thread-1
2023-11-05 18:43:48,199 - Process-1, Thread-2
2023-11-05 18:43:48,200 - Process-1, Thread-3
2023-11-05 18:43:48,200 - Process-1, Thread-4
2023-11-05 18:43:48,214 - Process-2, Thread-1
2023-11-05 18:43:48,215 - Process-2, Thread-2
2023-11-05 18:43:48,215 - Process-2, Thread-3
2023-11-05 18:43:48,216 - Process-2, Thread-4
2023-11-05 18:43:48,237 - Process-3, Thread-1
2023-11-05 18:43:48,237 - Process-3, Thread-2
2023-11-05 18:43:48,237 - Process-3, Thread-3
2023-11-05 18:43:48,238 - Process-3, Thread-4
```



###### 2.多线程压测：

```python
import logging
import threading
import multiprocessing
import requests

# 自定义接口地址
url = "https://*****api"

# 配置日志
logging.basicConfig(filename="e:\\log\\custom_logging.log", level=logging.INFO, format="%(asctime)s - %(message)s")

def thread_task(process_id, thread_id):
    try:
        response = requests.get(url)
        log_message = f"Process-{process_id}, Thread-{thread_id}, URL: {url}, Response Code: {response.status_code}"
        logging.info(log_message)
    except Exception as e:
        error_message = f"Process-{process_id}, Thread-{thread_id}, URL: {url}, Error: {str(e)}"
        logging.error(error_message)

def process_task(process_id, num_threads):
    for thread_id in range(1, num_threads + 1):
        thread = threading.Thread(target=thread_task, args=(process_id, thread_id))
        thread.start()
        thread.join()

if __name__ == "__main__":
    num_processes = 3
    num_threads = 4

    processes = []
    for process_id in range(1, num_processes + 1):
        process = multiprocessing.Process(target=process_task, args=(process_id, num_threads))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

```

