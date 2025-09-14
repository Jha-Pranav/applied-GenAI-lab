# Memory Integration Example for Buddy Chat Client

class ChatClientWithMemory:
    """Example integration of token management with chat client"""
    
    def __init__(self, model="gpt-4", max_tokens=128000):
        from .tools import ToolManager
        self.tool_manager = ToolManager(model, max_tokens)
        self.conversation_history = []
        self.model = model
        
    def add_message(self, role: str, content: str):
        """Add message and check for compression"""
        # Add new message
        self.conversation_history.append({"role": role, "content": content})
        
        # Check if compression is needed
        compressed_history, was_compressed = self.tool_manager.check_and_compress_history(
            self.conversation_history
        )
        
        if was_compressed:
            self.conversation_history = compressed_history
            print("🧠 Memory compressed to stay within token budget")
            
        return was_compressed
    
    def get_memory_status(self):
        """Get current memory status"""
        return self.tool_manager.get_token_info(self.conversation_history)
    
    def force_compression(self):
        """Manually trigger compression"""
        result = self.tool_manager._memory_manager("compress", messages=self.conversation_history)
        if result.get("success") and result.get("compressed"):
            self.conversation_history = result["compressed_history"]
            return result
        return {"compressed": False}

# Usage example:
"""
client = ChatClientWithMemory()

# Add messages normally
client.add_message("user", "Hello, can you help me with my project?")
client.add_message("assistant", "Sure! I'd be happy to help...")

# Check memory status
status = client.get_memory_status()
print(f"Token usage: {status['usage_percent']}%")

# Automatic compression happens when reaching 80% capacity
"""
