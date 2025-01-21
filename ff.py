import pyautogui
import time
import pygame


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
            print("bnwi and next clicked")

            # Wait for "noslot.png" to appear after clicking on "next"
            start_time = time.time()
            while not is_image_on_screen('C:\\Users\\zhang\\OneDrive\\Desktop\\autoclick\\noslot.png'):
                elapsed_time = time.time() - start_time
                if elapsed_time >= 30:
                    # Play a sound after 30 seconds
                    play_sound()
                    break

            # If "noslot.png" is detected, break out of the inner loop and repeat the process
            if is_image_on_screen('C:\\Users\\zhang\\OneDrive\\Desktop\\autoclick\\noslot.png'):
                break

except KeyboardInterrupt:
    print('\n')
