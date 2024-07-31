import ollama

class ImageAnalysisPipeline:
    def __init__(self, model: str):
        self.model = model

    def analyze_image(self, image_path: str, prompt: str) -> str:
        """Analyze the given image with a prompt using the specified model."""
        with open(image_path, 'rb') as file:
            response = ollama.chat(
                model=self.model,
                messages=[
                    {
                        'role': 'user',
                        'content': prompt,
                        'images': [file.read()],
                    },
                ],
            )
        return response['message']['content']

# Example usage
image_path = 'images/Teaser Pedigree Cats.jpg'
prompt = 'Explain about this image?'
image_analysis = ImageAnalysisPipeline(model='llava-phi3')
result = image_analysis.analyze_image(image_path, prompt)
print(result)
