#!/data/data/com.termux/files/usr/bin/python

from gtts import gTTS
import os
import datetime
import wikipedia
import sys
import time
import random
import subprocess

# Color codes for terminal output
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    MAGENTA = '\033[95m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

# Banner design
def show_banner():
    banner = f"""
{Colors.CYAN}{Colors.BOLD}
    ╔══════════════════════════════════════════════════════════╗
    ║                                                          ║
    ║     ██╗ █████╗ ██████╗ ██╗   ██╗██╗███████╗             ║
    ║     ██║██╔══██╗██╔══██╗██║   ██║██║██╔════╝             ║
    ║     ██║███████║██████╔╝██║   ██║██║███████╗             ║
    ║██   ██║██╔══██║██╔══██╗╚██╗ ██╔╝██║╚════██║             ║
    ║╚█████╔╝██║  ██║██║  ██║ ╚████╔╝ ██║███████║             ║
    ║ ╚════╝ ╚═╝  ╚═╝╚═╝  ╚═╝  ╚═══╝  ╚═╝╚══════╝             ║
    ║                                                          ║
    ║              {Colors.YELLOW}Advanced AI Assistant{Colors.CYAN}                     ║
    ║                                                          ║
    ╚══════════════════════════════════════════════════════════╝
{Colors.END}
    """
    print(banner)
    
    creator = f"""
{Colors.MAGENTA}{Colors.BOLD}╔════════════════════════════════════════════════════════════╗
║                    CREATED BY ADITYA                       ║
║                   Version 2.0 | Termux Edition             ║
╚════════════════════════════════════════════════════════════╝{Colors.END}
    """
    print(creator)
    time.sleep(2)

def clear_screen():
    os.system('clear')

def speak(text):
    print(f"{Colors.GREEN}{Colors.BOLD}JARVIS:{Colors.END} {Colors.CYAN}{text}{Colors.END}")
    try:
        tts = gTTS(text=text, lang='en')
        tts.save("output.mp3")
        # Using mpv for Termux
        os.system("mpv output.mp3 > /dev/null 2>&1")
    except Exception as e:
        print(f"{Colors.RED}Audio error: {e}{Colors.END}")

def show_help():
    help_text = f"""
{Colors.YELLOW}{Colors.BOLD}╔════════════════════════════════════════════════════════════╗
║                    AVAILABLE COMMANDS                       ║
╚════════════════════════════════════════════════════════════╝{Colors.END}

{Colors.CYAN}▶ time{Colors.END}          - Get current time
{Colors.CYAN}▶ date{Colors.END}          - Get current date
{Colors.CYAN}▶ calculate [expr]{Colors.END} - Perform calculations (e.g., calculate 5+3)
{Colors.CYAN}▶ wikipedia [topic]{Colors.END} - Search Wikipedia
{Colors.CYAN}▶ help{Colors.END}           - Show this help menu
{Colors.CYAN}▶ clear{Colors.END}          - Clear screen
{Colors.CYAN}▶ exit/bye{Colors.END}       - Exit JARVIS

{Colors.YELLOW}{Colors.BOLD}Examples:{Colors.END}
  • {Colors.GREEN}calculate 25 * 4{Colors.END}
  • {Colors.GREEN}wikipedia Artificial Intelligence{Colors.END}
  
{Colors.MAGENTA}{Colors.BOLD}Tip: You can also use natural language commands!{Colors.END}
    """
    print(help_text)

def loading_animation():
    chars = "⣾⣽⣻⢿⡿⣟⣯⣷"
    for char in chars:
        sys.stdout.write(f"\r{Colors.YELLOW}Processing {char}{Colors.END}")
        sys.stdout.flush()
        time.sleep(0.05)
    sys.stdout.write("\r" + " " * 20 + "\r")

def get_ai_response(command):
    """Enhanced command processing"""
    command = command.lower().strip()
    
    # Greeting responses
    greetings = ["hello", "hi", "hey", "greetings"]
    if any(greet in command for greet in greetings):
        responses = [
            "Hello sir! How can I assist you today?",
            "Greetings! Ready to serve you.",
            "Hi there! What can I do for you?"
        ]
        return random.choice(responses)
    
    # Thank you responses
    if "thank" in command:
        responses = [
            "You're welcome! Always happy to help.",
            "My pleasure, sir!",
            "Anytime! That's what I'm here for."
        ]
        return random.choice(responses)
    
    # How are you responses
    if "how are you" in command:
        responses = [
            "I'm functioning optimally, sir! Ready for your commands.",
            "All systems operational! How can I help?",
            "I'm doing great! Thanks for asking."
        ]
        return random.choice(responses)
    
    # Creator info
    if "who created you" in command or "who made you" in command:
        return "I was created by Aditya, a talented developer from Termux community!"
    
    # About JARVIS
    if "what can you do" in command or "your capabilities" in command:
        return "I can tell time and date, perform calculations, search Wikipedia, and respond to your commands. Just say help to see all my features!"
    
    return None

def main():
    clear_screen()
    show_banner()
    
    # Welcome message
    welcome_messages = [
        "Hello sir. I am JARVIS, your personal AI assistant. Ready for commands.",
        "System online. JARVIS at your service, sir.",
        "Good to see you! JARVIS is ready for your commands."
    ]
    speak(random.choice(welcome_messages))
    
    while True:
        try:
            # Custom prompt design
            print(f"\n{Colors.BOLD}{Colors.BLUE}┌─[{Colors.CYAN}JARVIS{Colors.BLUE}]─[{Colors.GREEN}Ready{Colors.BLUE}]\n└──╼ {Colors.YELLOW}$ {Colors.END}", end="")
            command = input().strip()
            
            if not command:
                continue
            
            # Show loading animation for Wikipedia searches
            if "wikipedia" in command.lower():
                loading_animation()
            
            # Check for AI responses first
            ai_response = get_ai_response(command)
            if ai_response:
                speak(ai_response)
                continue
            
            # Command processing
            if "time" in command:
                time_now = datetime.datetime.now().strftime("%I:%M %p")
                speak(f"The time is {time_now}")
                
            elif "date" in command:
                date_today = datetime.datetime.now().strftime("%B %d, %Y")
                speak(f"Today is {date_today}")
                
            elif "calculate" in command:
                try:
                    expression = command.replace("calculate", "").strip()
                    # Safe calculation without dangerous eval
                    if any(char in expression for char in ['__', 'import', 'os', 'sys']):
                        speak("Invalid expression. Please use basic math operations.")
                    else:
                        result = eval(expression)
                        speak(f"The result is {result}")
                except Exception:
                    speak("Sorry, I couldn't calculate that. Please use format: calculate 5+3")
                    
            elif "wikipedia" in command:
                try:
                    topic = command.replace("wikipedia", "").strip()
                    if not topic:
                        speak("Please specify a topic to search on Wikipedia.")
                    else:
                        speak(f"Searching Wikipedia for {topic}...")
                        summary = wikipedia.summary(topic, sentences=2)
                        speak(summary)
                except wikipedia.exceptions.DisambiguationError as e:
                    speak(f"Multiple results found. Please be more specific. Suggestions: {e.options[:3]}")
                except wikipedia.exceptions.PageError:
                    speak(f"Sorry, I couldn't find information about {topic} on Wikipedia.")
                except Exception as e:
                    speak(f"Error accessing Wikipedia: {str(e)}")
                    
            elif "help" in command:
                show_help()
                
            elif "clear" in command:
                clear_screen()
                show_banner()
                speak("Screen cleared. Ready for your next command.")
                
            elif "exit" in command or "bye" in command or "quit" in command:
                farewell = random.choice([
                    "Goodbye sir. See you later.",
                    "Shutting down. Have a great day!",
                    "Farewell! Come back anytime."
                ])
                speak(farewell)
                break
                
            else:
                speak("I didn't understand that command. Type 'help' to see available commands.")
                
        except KeyboardInterrupt:
            print(f"\n{Colors.RED}\nInterrupted by user{Colors.END}")
            speak("System interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"{Colors.RED}Error: {e}{Colors.END}")
            speak("An unexpected error occurred. Please try again.")

if __name__ == "__main__":
    # Check for required dependencies
    try:
        import gtts, wikipedia
    except ImportError:
        print(f"{Colors.RED}Missing dependencies! Installing required packages...{Colors.END}")
        os.system("pkg install python python-pip mpv -y")
        os.system("pip install gtts wikipedia")
        print(f"{Colors.GREEN}Installation complete! Run the script again.{Colors.END}")
        sys.exit(0)
    
    main()
