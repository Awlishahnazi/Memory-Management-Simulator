# Memory Management Simulator (First-Fit & Page Faults)

A Python-based simulation of core **Operating System Memory Management** concepts. This project demonstrates how a system allocates memory to processes using the **First-Fit algorithm** and simulates **Page Faults** during process execution.

> **📅 Project Timeline:** This project was originally developed and completed in **Autumn 2024** (University Term 5) as part of my Operating Systems coursework. It is uploaded here to document my continuous learning journey in System Design and Memory Management.

## Core Concepts Implemented

1. **First-Fit Memory Allocation:** When a process requests memory, the system scans the available free blocks and allocates the first block that is large enough to accommodate the process.
2. **Memory Fragmentation Handling:** If a process is allocated a block larger than its needs, the remaining free space is split and added back to the list of free blocks.
3. **Page Fault Simulation:** The program simulates a sequence of page accesses by different processes and tracks when a requested page is not currently in memory (a Page Fault).
4. **Statistics Reporting:** At the end of the simulation, it calculates the total number of page faults and breaks them down by process.

## Key Features

* **Object-Oriented Design:** Uses clean classes (`MemoryBlock`, `Process`, `Memory`) to represent system components.
* **Dynamic Allocation:** Simulates real-time memory allocation and deallocation.
* **Detailed Logging:** Prints the memory status after every page access, making it easy to trace the execution flow.

## Tech Stack

* **Python 3.x**
* **Collections Module** (Deque for page management)

## How to Run

1. Clone the repository:

   ```
   git clone https://github.com/Awlishahnazi/Memory-Management-Simulator.git
   ```
2. Navigate to the project directory:

   ```
   cd Memory-Management-Simulator
   ```
3. Run the simulation:

   ```
   python "memory management.py"
   ```

## Future Improvements (Roadmap)

This project serves as a foundational model. I plan to enhance it with the following features in the future:

* **Implement Actual Page Replacement Algorithms:** Currently, the simulator only tracks page faults. I plan to add a fixed frame limit and implement true **LRU (Least Recently Used)** and **FIFO** page replacement algorithms to simulate swapping.
* **Add Best-Fit and Worst-Fit:** Expand the memory allocation module to include `Best-Fit` and `Worst-Fit` algorithms for comparison.
* **Memory Compaction:** Implement a defragmentation function that merges adjacent free blocks to optimize memory usage.
* **Interactive GUI:** Transition from terminal-based output to a visual interface (using `tkinter` or `PyQt`) to visually demonstrate memory blocks and page movements.

## Author

**Ali Shahnazi Bejarsari**

* [GitHub Profile](https://github.com/Awlishahnazi)
* [LinkedIn](https://www.linkedin.com/in/ali-shahnazi-bejarsari-678bba342)
* [Personal Portfolio](https://alishahnazi.ir/)
