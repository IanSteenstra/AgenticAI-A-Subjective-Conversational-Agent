import threading
import time

# Placeholder for LLM interaction - you'll replace this with Gemini API calls later
def call_llm_output(internal_info):
    """
    Placeholder for an LLM call to format or generate output text.
    Replace with actual Gemini API call if needed.
    """
    print(f"Output Module (Output LLM): Processing internal info: '{internal_info}'")
    time.sleep(0.5) # Simulate LLM processing time
    # *** Here you might call the Gemini API for output formatting ***
    # For now, just return a formatted output
    output_text = f"Listener, the agent is thinking about the internal info: '{internal_info}'" # Modified output text
    return output_text

class OutputModule(threading.Thread):
    def __init__(self, input_queue): # Expects an input queue to receive thoughts and internal model
        threading.Thread.__init__(self)
        self.input_queue = input_queue # Queue to receive data from identity module
        self.running = True

    def run(self):
        print("Output Module started.")
        while self.running:
            if not self.input_queue.empty():
                output_data = self.input_queue.get() # Get the dictionary from the queue
                thought = output_data.get("thought") # Extract thought
                internal_model = output_data.get("internal_model") # Extract internal model
                output_text = self.output_process(thought, internal_model) # Pass both to output_process
                self.deliver_output(output_text)
            time.sleep(0.1) # Check queue periodically

    def stop(self):
        self.running = False
        print("Output Module stopped.")

    def output_process(self, thought, internal_model):
        """
        Processes internal information (thought and internal model) to generate output text.
        """
        # For now, just format directly and print internal model info.
        # You could use call_llm_output here later and feed it both thought and internal_model
        # output_text = call_llm_output({"thought": thought, "internal_model": internal_model}) # Example if using LLM
        output_text = f"Agent's Thought: {thought}\nAgent's Current Internal Model (Memory):\n{internal_model}" # More informative output
        return output_text

    def deliver_output(self, output_text):
        """
        Delivers the output text to the "listener" (e.g., prints to console, sends to a UI, etc.).
        """
        print(f"Output Module Output:\n{output_text}\n---")

# Example usage (for testing within this file - remove in final run.py integration)
if __name__ == "__main__":
    import queue
    thought_queue = queue.Queue() # Create a queue for thoughts
    output_mod = OutputModule(thought_queue)
    output_mod.start()

    # Simulate putting data (thought and internal model) into the queue from another module
    output_data1 = {"thought": "Initial thought for testing.", "internal_model": ["Memory item 1", "Memory item 2"]}
    thought_queue.put(output_data1)
    time.sleep(5)
    output_data2 = {"thought": "Another thought after some processing.", "internal_model": ["Memory item 1", "Memory item 2", "New memory item"]}
    thought_queue.put(output_data2)
    time.sleep(5)

    output_mod.stop()
    output_mod.join()
    print("Output Module test finished.")