import socket
import tkinter as tk
from tkinter import scrolledtext

class SimpleClient:
    def __init__(self):
        self.host = 'localhost'
        self.port = 12345
        self.client_socket = None
        self.connected = False
        
        self.root = tk.Tk()
        self.root.title("Simple Chat Client")
        self.root.geometry("500x400")
        
        self.status_label = tk.Label(self.root, text="Status: Disconnected", fg="red")
        self.status_label.pack(pady=5)
        
        self.message_area = scrolledtext.ScrolledText(self.root, state=tk.DISABLED, height=15)
        self.message_area.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)
        
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=5)
        
        self.receive_button = tk.Button(button_frame, text="Receive Message", command=self.receive_message)
        self.receive_button.pack(side=tk.LEFT, padx=5)
        
        message_frame = tk.Frame(self.root)
        message_frame.pack(pady=5, fill=tk.X, padx=10)
        
        tk.Label(message_frame, text="Message:").pack(anchor=tk.W)
        
        input_frame = tk.Frame(message_frame)
        input_frame.pack(fill=tk.X, pady=2)
        
        self.message_entry = tk.Entry(input_frame)
        self.message_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
        self.message_entry.bind('<Return>', self.send_message)
        
        self.send_button = tk.Button(input_frame, text="Send", command=self.send_message)
        self.send_button.pack(side=tk.RIGHT)
        
        self.root.after(1000, self.connect_to_server)
        
    def log_message(self, message):
        """Add message to the display area"""
        self.message_area.config(state=tk.NORMAL)
        self.message_area.insert(tk.END, message + "\n")
        self.message_area.config(state=tk.DISABLED)
        self.message_area.see(tk.END)
        
    def connect_to_server(self):
        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client_socket.connect((self.host, self.port))
            
            self.connected = True
            self.status_label.config(text="Status: Connected", fg="green")
            
        except Exception as e:
            self.log_message(f"Failed to connect to server: {str(e)}")
            self.log_message("Make sure the server is running first!")
            
    def receive_message(self):
        """Receive a message from the server"""
        if not self.connected:
            self.log_message("Not connected to server!")
            return
            
        try:
            message = self.client_socket.recv(1024).decode('utf-8')
            if message:
                self.log_message(f"Server: {message}")
            else:
                self.log_message("Server disconnected")
                self.connected = False
                self.status_label.config(text="Status: Disconnected", fg="red")
        except Exception as e:
            self.log_message(f"Error receiving message: {str(e)}")
            self.connected = False
            self.status_label.config(text="Status: Disconnected", fg="red")
            
    def send_message(self, event=None):
        """Send a message to the server"""
        if not self.connected:
            self.log_message("Not connected to server!")
            return
            
        message = self.message_entry.get()
        if message.strip():
            try:
                self.client_socket.send(message.encode('utf-8'))
                self.log_message(f"Client: {message}")
                self.message_entry.delete(0, tk.END)
            except Exception as e:
                self.log_message(f"Error sending message: {str(e)}")
                self.connected = False
                self.status_label.config(text="Status: Disconnected", fg="red")
                
    def run(self):
        """Start the GUI"""
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()
        
    def on_closing(self):
        """Handle window closing"""
        if self.connected and self.client_socket:
            self.client_socket.close()
        self.root.destroy()

if __name__ == "__main__":
    client = SimpleClient()
    client.run()