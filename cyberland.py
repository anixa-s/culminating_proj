import pygame
import sys
from pygame.locals import *
import textwrap


# Initiating Pygame

pygame.init()

FPS = 80
SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 790
 
# Setting the background and screen

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Cyberland!")
clock = pygame.time.Clock()
start_ticks = pygame.time.get_ticks()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


# Fonts
font = pygame.font.Font(None, 36)

# Load assets

bg = pygame.image.load('Cyberworld_01.jpg')
bg = pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
endworld = pygame.image.load('Endworld.jpg')
object_1 = pygame.image.load("mushroom.png")
object_1 = pygame.transform.scale(object_1, (75, 100))
character_left = pygame.image.load("character_left.png")
character_left = pygame.transform.scale(character_left, (300, 350))
character_right = pygame.image.load("character_right.png")
character_right = pygame.transform.scale(character_right, (300, 350))

# Define the mushroom rectangle
ufo_x, ufo_y = 910, 310
ufo_width, ufo_height = object_1.get_width(), object_1.get_height()
ufo_rect = pygame.Rect(ufo_x, ufo_y, ufo_width, ufo_height)


# Preparing blurbs, questions, and answers

information  = [
"Cybersecurity is the practice of protecting systems, networks, and programs from digital attacks. These cyberattacks are usually aimed at assessing, changing, or destroying sensitive information; extorting money from users through ransomware; or interrupting normal business processes.",
"Phishing is the practice of sending fraudulent emails that resemble emails from reputable sources. The aim is to steal sensitive data, such as credit card numbers and login information, and is the most common type of cyberattack. ",
"Ransomware is a type of malicious software that is designed to extort money by blocking access to files or the computer system until the ransom is paid. Paying the ransom does not guarantee that the files will be recovered or the system restored.",
"Social engineering is a psychological tactic that adversaries use to trick you into revealing sensitive information. Attackers gain the trust of targets, so they lower their guard, and then encourage them into taking unsafe actions such as divulging personal information or clicking on web links or opening attachments that may be malicious.",
"You can protect yourself from cyber attacks by: "
"Updating software and operating systems regularly to helps to patch vulnerabilities and enhance security measures against potential threats. Creating strong and unique passwords for each online account since cyberattacks often exploit weak or stolen passwords. Implementing Multi-Factor Authentication (MFA) which involves multiple identification forms before account access, reducing the risk of unauthorized access. Cisco Duo includes MFA that can integrate with most major applications as well as custom apps."
]

 
questions = ["What are cyberattacks?",

             "What is phising?",

             "What is ransomware?",

             "Which one is the correct scenario for social engineering?",

             "How can you protect yourself from cyberattacks?"]

 

correct_answers = [

"A",

"B",

"A",

"A",

"B"]

 

option_a = [

"A:  A deliberate attempt by an individual or organization to breach the information system of another individual or organization to disrupt, damage, steal, or gain unauthorized access to data",

"A:  The most common cybersecurity technique used by companies to protect user data through encryption and secure communication",

"A:  Software designed to obtain money by blocking access to the computer until the ransom is paid.",

"A:  Bob receives a text message from an unknown number informing him that his BBC bank account needs to be reseted. He agrees and sends the required information the “bank account” needs, such as his email, and bank account password.",

"A:  Multi-factor authentication (MFA) only works with custom applications and cannot be used with major platforms. Operating system updates are optional since they do not significantly impact cybersecurity."

]

 
option_b = [

"B:  A physical assault on a computer or device to destroy it using tools like hammers or drills, without the authorization of an adult",

"B:  The most common cyberattack hackers use by sending fraudulent emails to steal your personal information",

"B:  Hacker who gains money by blocking access to the files until the ransom is paid",

"B:  Noah enters his email and finds an advertisement from a pet agency informing his that they need their help to save a dog rescued 3 days ago. He sees a “Click Here To Save An Important Life” button and clicks on it.",

"B:  Using similar passwords for each online account can enhance cyberattacks. Implementing more multiple authentication before account access reduces the risk of unauthorized access."

]

description_1 = "Find the mushroom to begin learning!"

background_counter = 0

# Character positioning

character_speed = 7
character_width = character_right.get_width()
character_height = character_right.get_height()
character_x_1 = SCREEN_WIDTH // 2 - 650
character_y_1 = SCREEN_HEIGHT - 50 - character_height


# Define the character rectangle

character_rect = pygame.Rect(character_x_1, character_y_1, character_width, character_height)
 
# Score, and question checker

score = 0
blurb_counter = 0
question_counter = 0

def switch_bkg():
    # Apply blur to the endworld image
    blurred_endworld = blur_surface(endworld)

    # Scale and render the blurred endworld background
    scaled_endworld = pygame.transform.scale(blurred_endworld, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_endworld, (0, 0))
    pygame.display.flip()



def info_blurbs(blurb_counter, background):
    """Display the current info blurb on a blurred background."""
    global font, score
    # Draw the blurred background
    blurred_bg = blur_surface(background)
    screen.blit(blurred_bg, (0, 0))

    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (20, 20))  # Position the score at the top-left corner

    # Define textbook dimensions
    textbook_width = 1000
    textbook_height = 500
    textbook_x = (SCREEN_WIDTH - textbook_width) // 2
    textbook_y = (SCREEN_HEIGHT - textbook_height) // 2

    # Draw the textbook (white rectangle with border)
    pygame.draw.rect(screen, WHITE, (textbook_x, textbook_y, textbook_width, textbook_height), border_radius=20)
    pygame.draw.rect(screen, BLACK, (textbook_x, textbook_y, textbook_width, textbook_height), width=3, border_radius=20)

    # Font setup
    font = pygame.font.Font(None, 36)
    line_spacing = 40  # Vertical spacing between lines

    # Text wrapping
    max_line_width = textbook_width - 40  # Leave some padding inside the box
    blurb_lines = textwrap.wrap(information[blurb_counter], width=max_line_width // 18)

    # Calculate starting Y position for text inside the rectangle
    total_text_height = len(blurb_lines) * line_spacing
    start_y = textbook_y + (textbook_height - total_text_height) // 2

    # Render and display the text lines
    for i, line in enumerate(blurb_lines):
        blurb_text = font.render(line, True, BLACK)
        text_rect = blurb_text.get_rect(midtop=(SCREEN_WIDTH // 2, start_y + i * line_spacing))
        screen.blit(blurb_text, text_rect)

    # Add a "continue" instruction at the bottom
    continue_text = font.render("Press any key to continue", True, WHITE)
    continue_rect = continue_text.get_rect(center=(SCREEN_WIDTH // 2, textbook_y + textbook_height + 25))
    screen.blit(continue_text, continue_rect)

    pygame.display.flip()

    # Wait for user input (non-blocking)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                return
 
def check_answer(user_input, textbook_rect):
    global score, question_counter, blurb_counter

    # Get the correct answer
    correct_input = correct_answers[question_counter].strip().lower()

    # Check if the user input matches the correct answer
    if user_input == correct_input:
        score += 1  # Increase the score
        res = True 
    else:
        res = False

    # Move to the next question
    blurb_counter += 1
    question_counter += 1
    return res 

 
def wrap_text(text, font, max_width):

    # Wrap the text within the maximum width

    wrapped_text = textwrap.wrap(text, width=60)  # Wraps text at a reasonable length based on font size

    lines = []

    for line in wrapped_text:

        rendered_line = font.render(line, True, BLACK)

        lines.append(rendered_line)

    return lines

 
def ask_question(question_num):
    global score_text, question_counter
    question_counter = question_num
    # Blit the background
    screen.blit(blur_surface(bg), (0, 0))

    # Textbox dimensions
    textbook_width = 600
    textbook_height = 80
    textbook_x = (SCREEN_WIDTH - textbook_width) // 2
    textbook_y = 50
    textbook_rect = pygame.Rect(textbook_x, textbook_y, textbook_width, textbook_height)

    # Draw the textbox (initially white)
    pygame.draw.rect(screen, WHITE, textbook_rect, border_radius=20)
    pygame.draw.rect(screen, BLACK, textbook_rect, width=3, border_radius=20)

    # Render the question text
    font = pygame.font.Font(None, 36)
    question_text = font.render(questions[question_counter], True, BLACK)
    question_rect = question_text.get_rect(center=(SCREEN_WIDTH // 2, textbook_y + textbook_height // 2))
    screen.blit(question_text, question_rect)

    # Draw ellipses (changed to rectangles) for the options
    options_y = textbook_y + textbook_height  # Start below the question text with some spacing
    ellipse_width = 1000  # Adjusted to a reasonable width for readability
    ellipse_height = 100  # Initial height for ellipses
    spacing = 60  # Space between each ellipse

    # Wrap text for the options
    correct_answer_lines = wrap_text(option_a[question_counter], font, ellipse_width)
    wrong_answer_lines = wrap_text(option_b[question_counter], font, ellipse_width)

    # Calculate the vertical height based on the number of lines wrapped
    correct_answer_ellipse_height = len(correct_answer_lines) * 40 + 45  # Adjust height based on wrapped lines
    wrong_answer_ellipse_height = len(wrong_answer_lines) * 40 + 45

    pygame.display.flip()

    # Handle user input
    my_font = pygame.font.Font(None, 30)
    field_value = ""
    waiting = True

    # Define the text input field dimensions
    field_width = 400
    field_height = 50
    field_x = (SCREEN_WIDTH - field_width) // 2  # Center horizontally
    field_y = SCREEN_HEIGHT - 100  # Near the bottom of the screen
    field_rect = pygame.Rect(field_x, field_y, field_width, field_height)
    color = WHITE
    while waiting:
        # Redraw the screen elements in each frame
        screen.blit(blur_surface(bg), (0, 0))
        

        # Redraw question and options
        screen.blit(question_text, question_rect)

        # Redraw rectangles and options
        pygame.draw.rect(screen, WHITE, (SCREEN_WIDTH // 2 - ellipse_width // 2, options_y, ellipse_width, correct_answer_ellipse_height))
        current_y = options_y + (correct_answer_ellipse_height - len(correct_answer_lines) * 40) // 2
        for line in correct_answer_lines:
            line_rect = line.get_rect(center=(SCREEN_WIDTH // 2, current_y))
            screen.blit(line, line_rect)
            current_y += 40

        pygame.draw.rect(screen, WHITE, (SCREEN_WIDTH // 2 - ellipse_width // 2, options_y + correct_answer_ellipse_height + spacing, ellipse_width, wrong_answer_ellipse_height))
        current_y = options_y + correct_answer_ellipse_height + spacing + (wrong_answer_ellipse_height - len(wrong_answer_lines) * 40) // 2
        for line in wrong_answer_lines:
            line_rect = line.get_rect(center=(SCREEN_WIDTH // 2, current_y))
            screen.blit(line, line_rect)
            current_y += 40

        # Redraw the input field    
        pygame.draw.rect(screen, color, field_rect, border_radius=10)
        pygame.draw.rect(screen, BLACK, field_rect, width=2, border_radius=10)

        # Render the text entered
        field_text = my_font.render(field_value, True, BLACK)
        field_text_rect = field_text.get_rect(midleft=(field_rect.x + 10, field_rect.centery))
        screen.blit(field_text, field_text_rect)

        # Instruction to the user
        instruction = my_font.render("Type your answer 'A' or 'B' and press ENTER:", True, WHITE)
        instruction_rect = instruction.get_rect(center=(SCREEN_WIDTH // 2, field_rect.y - 15))
        screen.blit(instruction, instruction_rect)

        # Display the current score
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (20, 20))  # Position the score at the top-left corner

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if color == WHITE:
                        result = check_answer(field_value.strip().lower(), textbook_rect)  # Pass textbox rect
                        if result:
                            color = GREEN
                        else:
                            color = RED
                    else:
                        waiting = False
                elif event.key == pygame.K_BACKSPACE:
                    field_value = field_value[:-1]  # Remove last character
                elif (event.unicode.isalnum() or event.unicode == " ") and len(field_value) < 20:
                    field_value += event.unicode  # Add new character
        pygame.display.flip()  # Update the screen

def blur_surface(surface, scale_factor=0.1):
    """Applies a blur effect by scaling the surface down and back up."""
    small_width = int(surface.get_width() * scale_factor)
    small_height = int(surface.get_height() * scale_factor)
    if small_width <= 0 or small_height <= 0:
        return surface
    small_surface = pygame.transform.smoothscale(surface, (small_width, small_height))
    return pygame.transform.smoothscale(small_surface, surface.get_size())


def show_starting_screen():
    # Create a blurred version of the background
    blurred_bg = blur_surface(bg)

    # Draw the blurred background
    screen.blit(blurred_bg, (0, 0))

    # Render the instructions and title
    title_font = pygame.font.Font(None, 100)
    description_font = pygame.font.Font(None, 50)
    startbutton_font = pygame.font.Font(None, 60)

    title_text = title_font.render("Welcome To Cyberland...", True, WHITE)
    startbutton_text = startbutton_font.render("CLICK SCREEN FOR INSTRUCTIONS", True, WHITE)

    description_lines = [
        "By completing this video game, you will gain the necessary tools to",
        "protect your digital presence against cybersecurity threats.",
    ]

    # Adjusted line spacing multiplier
    line_spacing = 70  

    # Draw title and instructions
    description_start_y = SCREEN_HEIGHT // 1.9 - (len(description_lines) * line_spacing) // 2
    screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, 50))

    # Render each description line with increased spacing
    for i, line in enumerate(description_lines):
        line_text = description_font.render(line, True, WHITE)
        screen.blit(line_text, (SCREEN_WIDTH // 2 - line_text.get_width() // 2, description_start_y + i * line_spacing))

    # Render instruction text closer to the bottom
    screen.blit(startbutton_text, (SCREEN_WIDTH // 2 - startbutton_text.get_width() // 2, SCREEN_HEIGHT - 100))

    pygame.display.flip()

    # Wait for user input to start the game
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                waiting = False
 

def show_text_screen():

    """Displays a centered image on a black background before the main game starts."""

    screen.fill(BLACK)

 

    # Load the image

    image = pygame.image.load("beginning.png").convert_alpha()  # Replace with your image path

 

    # Scale the image if needed
    new_width = 1200  # Desired width of the image
    new_height = 700  # Desired height of the image
    image = pygame.transform.scale(image, (new_width, new_height))


    # Get the image rectangle

    image_rect = image.get_rect()

    # Center the image on the screen

    image_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    # Draw the image onto the screen

    screen.blit(image, image_rect.topleft)

    pygame.display.flip()

    # Wait for user input

    waiting = True

    while waiting:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                pygame.quit()

                sys.exit()

            if event.type == pygame.KEYDOWN:

                waiting = False
   

def show_game_over_screen(final_score):
    title_font = pygame.font.Font(None, 100)
    instruction_font = pygame.font.Font(None, 50)
    title_text = title_font.render("Game Over!", True, BLACK)
    score_text = instruction_font.render(f"Your final score is: {final_score}/5", True, BLACK)
    restart_text = instruction_font.render("Press any key to EXIT", True, BLACK)

    # Ensure the screen is cleared before showing game over text
    screen.fill((255, 255, 255))  # Optional background color
    switch_bkg()  # Render the endworld background

    # Overlay the game over text
    screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, SCREEN_HEIGHT // 2 - 100))
    screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, SCREEN_HEIGHT // 2))
    screen.blit(restart_text, (SCREEN_WIDTH // 2 - restart_text.get_width() // 2, SCREEN_HEIGHT // 2 + 100))
    pygame.display.flip()

    # Handle game over input
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:  # Restart the game
                waiting = False
    pygame.quit()
    sys.exit()

    """waiting = True

    while waiting:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                pygame.quit()

                sys.exit()

            if event.type == pygame.KEYDOWN:

                waiting = False

                # main_game()"""

 
def main_game():
    global score, character_x_1, character_y_1, character_rect, description_1, start_ticks, question_ticks, blurb_counter

    # Initialize Pygame
    pygame.init()

    # Game setup
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Set screen dimensions
    pygame.display.set_caption("Cyberland")
    clock = pygame.time.Clock()

    # Font setup for score
    font = pygame.font.Font(None, 36)  # Use default font, size 36

    run = True
    score = 0  # Initialize score

    character_direction = "right"
    blurb_counter = 0  # To track the current info blurb index
    question_counter = 0  # To track the current question index

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Update the display
        screen.blit(bg, (0, 0))  # Background image
        screen.blit(object_1, (ufo_x, ufo_y))  # Object (e.g., UFO)

        # Display score
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))  

        # Display description in a white textbox with black font
        text_surface = font.render(description_1, True, (0, 0, 0))  # Black text
        text_box = pygame.Surface((text_surface.get_width() + 20, text_surface.get_height() + 10))  # Create white box
        text_box.fill((255, 255, 255))  # Fill box with white color
        screen.blit(text_box, (SCREEN_WIDTH - text_box.get_width() - 10, 10))  # Position in top-right corner
        screen.blit(text_surface, (SCREEN_WIDTH - text_box.get_width() - 10 + 10, 10 + 5))  # Center text in box

        # Key press handling for character movement
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and character_x_1 > 0:
            character_direction = "left"
            character_x_1 -= character_speed

        if keys[pygame.K_RIGHT] and character_x_1 < SCREEN_WIDTH - character_width:
            character_direction = "right"
            character_x_1 += character_speed

        if keys[pygame.K_UP] and character_y_1 > 0:
            character_y_1 -= character_speed

        if keys[pygame.K_DOWN] and character_y_1 < SCREEN_HEIGHT - character_height:
            character_y_1 += character_speed

        # Update character position
        character_rect.topleft = (character_x_1, character_y_1)

        # Update the character's image depending on direction
        if character_direction == "left":
            screen.blit(character_left, (character_x_1, character_y_1))
        elif character_direction == "right":
            screen.blit(character_right, (character_x_1, character_y_1))

        if character_rect.colliderect(ufo_rect):
            # Loop through the 5 rounds
            for i in range(5):                # Display the current info blurb (based on the blurb_counter)
                info_blurbs(i, bg)  # Show the info blurb for the current round
                ask_question(i)  # Display the question for the current round
                if i == 4:
                    show_game_over_screen(score)

        # Update the display
        pygame.display.flip()
        clock.tick(60)  # Limit to 60 frames per second


# Main program
show_starting_screen()
show_text_screen()
main_game()
pygame.quit()