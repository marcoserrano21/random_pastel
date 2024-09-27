from random_pastel import generate_pastel_color, hex_to_rgb, display_color

# Test functions
def test_generate_pastel_color():
    color = generate_pastel_color()
    assert color.startswith("#"), f"Hex color {color} should start with #."
    assert len(color) == 7, f"Hex color {color} should be 7 characters long (including #)."
    print(f"Test passed: {color} is a valid hex color.")

def test_hex_to_rgb():
    color = generate_pastel_color()
    rgb = hex_to_rgb(color)
    assert all(0.5 <= value <= 1.0 for value in rgb), f"RGB values {rgb} should be between 0.5 and 1.0 for pastel colors."
    print(f"Test passed: {color} correctly converted to {rgb}.")

def test_display_color():
    color = generate_pastel_color()
    try:
        display_color(color)
        print(f"Test passed: {color} was successfully displayed.")
    except Exception as e:
        print(f"Test failed: {e}")

# Running all tests
def run_tests():
    test_generate_pastel_color()
    test_hex_to_rgb()
    test_display_color()

# Calling the test runner
if __name__ == "__main__":
    run_tests()
