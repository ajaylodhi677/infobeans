from pynput import keyboard, mouse

# ---------- KEYBOARD ----------
def on_key_press(key):
    print("Key pressed:", key)

    # Stop when ESC is pressed
    if key == keyboard.Key.esc:
        print("Keyboard listener stopped")
        return False


# ---------- MOUSE ----------
def on_click(x, y, button, pressed):
    if pressed:
        print(f"Mouse clicked at ({x}, {y}) with {button}")


print("Pynput demo started!")
print("Press ESC to stop the keyboard listener.")
print("Click the mouse to see its position.")

keyboard_listener = keyboard.Listener(on_press=on_key_press)
mouse_listener = mouse.Listener(on_click=on_click)

keyboard_listener.start()
mouse_listener.start()

keyboard_listener.join()
mouse_listener.stop()

mouse_listener.join()

print("Program finished.")