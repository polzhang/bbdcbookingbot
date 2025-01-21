import pyautogui
import time
import pygame

# Function to perform mouse click at a specified position
def click_at_position(x, y):
    pyautogui.click(x, y)

# Function to check if a certain image is present on the screen
def is_image_on_screen(image_path):
    return pyautogui.locateOnScreen(image_path, grayscale=False, confidence=0.8) is not None

# Function to play a sound
def play_sound():
    pygame.mixer.init()
    pygame.mixer.music.load('C:\\Users\\zhang\\OneDrive\\Desktop\\autoclick\\notif.mp3')  # Replace with your actual sound file path
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

time.sleep(2)

# Sign in
click_at_position(1490, 150)  # Click on booking website bookmark
while not is_image_on_screen('C:\\Users\\zhang\\OneDrive\\Desktop\\autoclick\\access.png'):  # Wait for website to load
    time.sleep(0.1)
    print("WAITING")
click_at_position(750, 600)  # Click on username field
pyautogui.write("159B09122002", interval=0.01)  # Type username
click_at_position(743, 772)  # Click on password field
pyautogui.write("991465", interval=0.01)  # Type password
click_at_position(1020, 964)  # Click on login
while not is_image_on_screen('C:\\Users\\zhang\\OneDrive\\Desktop\\autoclick\\verify.png'):  # Wait for captcha verify
    time.sleep(0.1)
# When verify button/captcha appears:
click_at_position(730, 800)  # Click on captcha field
# Have to manually type captcha and click on verify
while not is_image_on_screen('C:\\Users\\zhang\\OneDrive\\Desktop\\autoclick\\booking.png'):  # Wait for website to load
    time.sleep(0.1)
click_at_position(150, 580)
while not is_image_on_screen('C:\\Users\\zhang\\OneDrive\\Desktop\\autoclick\\marker.png'):
    time.sleep(0.5)
click_at_position(864, 488)  # Click on practical tab
print("clicked on practical")
time.sleep(1)
while not is_image_on_screen('C:\\Users\\zhang\\OneDrive\\Desktop\\autoclick\\book.png'):
    time.sleep(0.5)

# Initial delay before the first iteration (in seconds)
initial_delay = 2
is_first_iteration = True

# Start the loop
try:
    while True:
        if is_first_iteration:
            time.sleep(initial_delay)  # Initial delay only for the first iteration
            is_first_iteration = False

        while True:
            # Click on "book slot"
            click_at_position(750, 870)
            print("book slot clicked")

            # Wait for "bwfi" to appear on screen
            while not is_image_on_screen('C:\\Users\\zhang\\OneDrive\\Desktop\\autoclick\\bwfi.png'):
                time.sleep(0.05)
                print("no bwfi yet")

            # Click on "bwfi" after it appears
            click_at_position(960, 600)

            # Click on "next" immediately after clicking on "bwfi"
            click_at_position(1200, 835)
            print("bwfi and next clicked")

            # Wait for "noslot.png" to appear after clicking on "next"
            start_time = time.time()
            while not is_image_on_screen('C:\\Users\\zhang\\OneDrive\\Desktop\\autoclick\\noslot.png'):
                elapsed_time = time.time() - start_time
                if elapsed_time >= 15:
                    # Play a sound after 15 seconds
                    play_sound()
                    break

            # If "noslot.png" is detected, break out of the inner loop and repeat the process
            if is_image_on_screen('C:\\Users\\zhang\\OneDrive\\Desktop\\autoclick\\noslot.png'):
                break

except KeyboardInterrupt:
    print('\nStopped by user')
