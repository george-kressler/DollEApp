import pytest
from project import generate_image

# Test the generate_image function
def test_generate_image():
    prompt = "A sunset over a mountain range"
    image_url = generate_image(prompt)

    # Basic check to see if the function returns a string
    assert isinstance(image_url, str)

    # Simple check to see if the returned string is a URL format
    assert image_url.startswith("http://") or image_url.startswith("https://")
