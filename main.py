import copy


def heapify(max_heap, current_node_index):
    # Find the index of the left and right children nodes
    left_child_index = 2 * current_node_index
    right_child_index = (2 * current_node_index) + 1

    # If the left child is larger than the current node
    if (
        left_child_index <= (len(max_heap) - 1)
        and max_heap[left_child_index] > max_heap[current_node_index]
    ):
        largest_node_index = left_child_index
    else:
        largest_node_index = current_node_index

    # If the right child is the largest node
    if (
        right_child_index <= (len(max_heap) - 1)
        and max_heap[right_child_index] > max_heap[largest_node_index]
    ):
        largest_node_index = right_child_index

    # If one of the children has a larger value, swap places with the current node
    if largest_node_index != current_node_index:
        swap_value = max_heap[current_node_index]
        max_heap[current_node_index] = max_heap[largest_node_index]
        max_heap[largest_node_index] = swap_value

        # Recursively heapify
        heapify(max_heap, largest_node_index)

    return max_heap


def build_max_heap(max_heap):
    heap_size = len(max_heap)

    for i in range((heap_size // 2), -1, -1):
        max_heap = heapify(max_heap, i)

    return max_heap


def heapsort(hlist):
    # Check for special cases
    if hlist is None:
        return None
    elif hlist == []:
        return []

    # Build the inital max heap
    max_heap = copy.deepcopy(hlist)
    build_max_heap(max_heap)

    sorted_heap = []
    for i in range(len(max_heap), 0, -1):
        # Add largest value in maxHeap to the sorted heap
        sorted_heap.insert(0, max_heap[0])
        # Move the last value in maxHeap to the front
        max_heap[0] = max_heap[len(max_heap) - 1]
        max_heap.pop(len(max_heap) - 1)

        # Restore maxHeap property
        heapify(max_heap, 0)

    return sorted_heap
