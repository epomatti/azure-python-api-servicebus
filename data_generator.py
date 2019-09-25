from servicebus import enqueue
from storage import delete, upload

delete('file1.txt')
delete('file2.txt')
delete('file3.txt')

upload('./sample_file.txt', 'file1.txt')
upload('./sample_file.txt', 'file2.txt')
upload('./sample_file.txt', 'file3.txt')

data1 = '{"timestamp": "2019-09-25 00:00:00.000000", "filename": "file1.txt", "device_id": "device1"}'
data2 = '{"timestamp": "2019-09-25 00:00:00.000000", "filename": "file2.txt", "device_id": "device2"}'
data3 = '{"timestamp": "2019-09-25 00:00:00.000000", "filename": "file3.txt", "device_id": "device3"}'

enqueue(data1, 'SERVICE_BUS_INPUT_QUEUE')
enqueue(data2, 'SERVICE_BUS_INPUT_QUEUE')
enqueue(data3, 'SERVICE_BUS_INPUT_QUEUE')