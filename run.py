import threading
import time
import queue
from identity_module import IdentityModule
from output_module import OutputModule

def main():
    print("Starting Identity-Aware LLM Architecture...")

    # Shared memory (initially a list, could be more complex later)
    agent_memory = []

    # Communication queue for thoughts and internal model info
    thought_queue = queue.Queue()

    # Initialize and start modules as threads
    identity_module = IdentityModule(agent_memory)
    output_module = OutputModule(thought_queue)

    # **Important: Connect the queue to the IdentityModule**
    identity_module.set_output_queue(thought_queue)

    identity_module.start()
    output_module.start()

    print("Modules started in threads.")

    # In a real application, you might have a main loop here to control the system,
    # provide initial prompts, handle user input, etc.
    # For this example, let's just run for a while and then stop.
    time.sleep(30) # Run for 30 seconds

    print("Stopping modules...")
    identity_module.stop()
    output_module.stop()

    identity_module.join()
    output_module.join()

    print("Modules stopped and threads joined.")
    print("Final agent memory:", agent_memory)
    print("Identity-Aware LLM Architecture run finished.")

if __name__ == "__main__":
    main()