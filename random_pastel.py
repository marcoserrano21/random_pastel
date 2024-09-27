import random
import matplotlib.pyplot as plt

def generate_pastel_color():
    # Generate random RGB values
    red = random.randint(127, 255)
    green = random.randint(127, 255)
    blue = random.randint(127, 255)

    # Convert RGB to hex
    hex_color = '#{:02x}{:02x}{:02x}'.format(red, green, blue).upper()

    return hex_color

def hex_to_rgb(hex_color):
    # Convert hex to RGB tuple
    hex_color = hex_color.lstrip('#')
    rgb_color = []

    for i in (0, 2, 4):
        rgb_value = int(hex_color[i:i+2], 16) / 255.0
        rgb_color.append(rgb_value)

    return rgb_color

def display_color(hex_color):
    # Convert hex to RGB
    rgb_color = hex_to_rgb(hex_color)

    # Create a plot with the specified color
    plt.figure(figsize=(2, 2))
    plt.imshow([[rgb_color]])
    plt.axis('off')
    plt.savefig("pastel_color.png")
    plt.show()

def main():
    while True:
        pastel_color = generate_pastel_color()
        print(f"Generated Pastel Color: {pastel_color}")

        display_color(pastel_color)

        user_input = input("Generate another color? (yes/no): ").strip().lower()
        if user_input != 'yes':
            break

if __name__ == "__main__":
    main()


