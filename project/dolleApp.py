import openai 

openai.api_key = open('apikey.txt','r').read()


response = openai.images.generate(
  model="dall-e-3",
  prompt=(input("Please enter a prompt for Doll E: ")),
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url

print(image_url)