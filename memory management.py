import sys
from collections import deque

class MemoryBlock:
    def __init__(self, start_address, size):
        self.start_address = start_address  
        self.size = size  

    def __str__(self):
        return f"[Start: {self.start_address}, Size: {self.size}]"

class Process:
    def __init__(self, name, memory_size):
        self.name = name  
        self.memory_size = memory_size  
        self.pages = []  

class Memory:
    def __init__(self, total_memory):
        self.total_memory = total_memory  
        self.free_blocks = [MemoryBlock(0, total_memory)]  
        self.allocated_processes = {}  
        self.current_pages = []  

    def allocate_first_fit(self, process):
        for block in self.free_blocks:
            if block.size >= process.memory_size:
                self.free_blocks.remove(block)
                allocated_block = MemoryBlock(block.start_address, process.memory_size)
                self.free_blocks.append(MemoryBlock(block.start_address + process.memory_size, block.size - process.memory_size))
                self.allocated_processes[process.name] = allocated_block
                print(f"{process.name} allocated successfully")
                return True
        return False

    def show_memory_status(self):
        print(f"Current Memory Pages: {self.current_pages}")

class PageReplacementAlgorithm:
    def __init__(self):
        self.pages_in_memory = deque() 

    def access_page(self, page_request, memory):
        process, page_number = page_request

        if (process, page_number) not in memory.current_pages:
            memory.current_pages.append((process, page_number))
            print(f"- Page fault! Accessing {process}, Page {page_number}")

        memory_status = [f"{p[0]}{p[1]}" for p in memory.current_pages]
        return memory_status

def simulate_memory_management():
    memory = Memory(100)

    process_list = {
        "Process A": Process("Process A", 40),
        "Process B": Process("Process B", 30),
        "Process C": Process("Process C", 50),
    }

    total_page_faults = 0
    page_faults_by_process = {"A": 0, "B": 0, "C": 0}

    for proc in process_list.values():
        memory.allocate_first_fit(proc)

    page_access_sequence = [
        ["Process A", 1], ["Process B", 1], ["Process A", 2],
        ["Process C", 1], ["Process A", 3], ["Process C", 2],
        ["Process B", 2], ["Process C", 3], ["Process A", 4],
        ["Process C", 4], ["Process B", 3], ["Process C", 5]
    ]

    lru = PageReplacementAlgorithm()

    for idx, (process, page_number) in enumerate(page_access_sequence):
        print(f"{idx + 1}. Accessing {process}, Page {page_number}")

        memory_status = lru.access_page((process, page_number), memory)

        process_id = process.split()[-1]  
        page_faults_by_process[process_id] += 1

        print(f"Memory Status: {memory_status}")


    total_page_faults = sum(page_faults_by_process.values())


    print("\nFinal Statistics:")
    print(f"- Total Page Faults: {total_page_faults}")
    print(f"- Final Memory Status: {memory.current_pages}")
    print(f"- Page Faults by Process: A = {page_faults_by_process['A']}, B = {page_faults_by_process['B']}, C = {page_faults_by_process['C']}")

simulate_memory_management()
