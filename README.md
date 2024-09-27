# Pastel Color Generator and Visualizer
#### Video Demo:  [https://youtu.be/NMefxkS7eb0]
#### Description:
This project is a Python-based Pastel Color Generator that allows users to generate random pastel colors and display them graphically using matplotlib. The application generates a random color in hex format, converts it to an RGB format, and displays it on the screen. It then asks the user if they want to generate another color. The main purpose of the project is to practice Python programming, explore random color generation, and implement simple plotting functionality.

The project consists of several functions, each with a specific purpose. The user then has the option to continuously generate new colors or exit the program after viewing a generated pastel color.

#### Files in the Project:
random_pastel:
This is the primary file of the project and contains the following key functions:

main()
The main function serves as the entry point of the program. It runs an infinite loop where it generates a pastel color, displays it, and then asks the user if they would like to generate another color. If the user chooses not to continue, the loop is broken, and the program terminates.

generate_pastel_color()
This function generates a random pastel color by selecting RGB values within a range that ensures the color is light and soft, typical of pastels. It limits the RGB values between 127 and 255, ensuring no dark colors are generated. The function then converts the RGB values to hex format, which is commonly used in web design.

hex_to_rgb(hex_color)
This helper function converts a hex color string into an RGB format. The RGB values are normalized to the range [0, 1], which is required by the matplotlib library for plotting the color on a graph.

display_color(hex_color)
This function takes a hex color, converts it to RGB using hex_to_rgb(), and uses matplotlib to display the generated pastel color in a 2x2 plot. It also saves the color image as pastel_color.png for reference.

**Key Features:**
- Random generation of pastel colors using RGB values between 127 and 255.
- Conversion of RGB colors into hexadecimal format, commonly used in web design.
- Visual display of the generated color in a small graphical plot.
- An interactive loop that allows users to generate multiple pastel colors.

**Modules Used:**
- `random` for generating random RGB values.
- `matplotlib.pyplot` for displaying the generated colors in real-time.

This project is useful for designers or anyone looking for quick inspiration using beautiful pastel colors.
