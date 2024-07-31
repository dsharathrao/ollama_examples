## Image Analysis Example

The **Image Analysis** is a Python class for analyzing images using the Ollama large language model (LLM). This class encapsulates the functionality of sending images and prompts to the LLM and retrieving detailed responses. It is designed to make it easy to interact with AI models for image-based queries.

## Features

- **Image Analysis**: Analyze images with detailed explanations using state-of-the-art AI models.
- **Customizable**: Easily change the model and prompt for different use cases.
- **Simple API**: Provides a straightforward interface for querying and retrieving responses.

## Installation

To use the Image Analysis Pipeline, you need to have the following packages installed:

- `ollama`

You can install these packages using pip:

```bash
pip install ollama
```

### Note: Ensure that your model is running in background with ollama
Ex: 
```bash
ollama run llava
```

Usage
Initializing the Pipeline
To initialize the pipeline, create an instance of the ImageAnalysisPipeline class with your desired model. For example, if you want to use the llava-phi3 model:

```python
from image_analysis_pipeline import ImageAnalysisPipeline
```
## Initialize the pipeline with the desired model
image_analysis = ImageAnalysisPipeline(model='llava-phi3')
Analyzing an Image
To analyze an image, use the analyze_image method, which requires the image file path and a prompt. The method will return the response from the model.

```python
# Path to the image file
image_path = 'Teaser Pedigree Cats.jpg'

# Prompt for the analysis
prompt = 'Explain about this image?'

# Analyze the image and get the response
result = image_analysis.analyze_image(image_path, prompt)
print(result)
```
Example Output
The output will be a detailed explanation of the image based on the provided prompt. For instance:

```sql
The image depicts a group of pedigree cats, each with distinct features and patterns. The cats appear to be of various breeds, showcasing the diversity within feline species...
```

## TODO
- Create end-to-end pipeline.
- Error handling
