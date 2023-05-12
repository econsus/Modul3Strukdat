from Queue import Queue

queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.print_queue()


while not queue.is_empty():
    queue_member = queue.dequeue()
    print(queue_member)

queue.enqueue_string("Ini")
queue.print_queue()
