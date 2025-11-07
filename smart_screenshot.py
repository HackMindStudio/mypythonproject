import os
import datetime
import webbrowser
import pyautogui

# If moving mouse to top-left stops the script, disable the failsafe:
pyautogui.FAILSAFE = False

OUTPUT_DIR = "Captured_Screenshots"

def ensure_output_dir():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

def unique_filename(prefix="screenshot", ext="png"):
    ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{prefix}_{ts}.{ext}"

def take_screenshot():
    ensure_output_dir()
    filename = unique_filename()
    save_path = os.path.join(OUTPUT_DIR, filename)

    try:
        img = pyautogui.screenshot()
        img.save(save_path)
        print(f"Screenshot saved: {save_path}")
        # Auto-open the saved file (Windows default viewer)
        try:
            webbrowser.open(save_path)
        except Exception:
            pass
    except Exception as e:
        print(f"Error taking screenshot: {e}")

def main():
    print("Smart Screenshot Capture Tool")
    print("Press Enter to take a screenshot, or type 'exit' to quit.\n")

    while True:
        user_input = input("Press Enter to capture (or type 'exit'): ").strip().lower()
        if user_input == "exit":
            print("Exiting Screenshot App...")
            break
        take_screenshot()

if __name__ == "__main__":
    main()
