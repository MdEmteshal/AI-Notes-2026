from google import genai
from google.genai import types
import httpx,pathlib,io


client=genai.Client(api_key="")

# doc_url="https://www.cuyamaca.edu/academics/departments/math/m180/differentiation-formulas.pdf"

# doc_data=httpx.get(doc_url).content

prompt="summarize the document"

# this is for local pdf read
# filepath=pathlib.Path('pdfs/sample1.pdf')
# doc_data=filepath.read_bytes()

# pdf=types.Part.from_bytes(
#     data=doc_data,
#     mime_type="application/pdf"
# )

long_context_pdf_path="https://www.cuyamaca.edu/academics/departments/math/m180/differentiation-formulas.pdf"

doc_data=io.BytesIO(httpx.get(long_context_pdf_path).content)

pdf=client.files.upload(
    file=doc_data,
    config={
        "mime_type":"application/pdf"
    }
)

response=client.models.generate_content(
    model="gemini-2.5-flash-lite",
    contents=[pdf,prompt],
    config=types.GenerateContentConfig(
    system_instruction="Answer within 200 charaters"
        )                                  
        
    )

print(response.text
      )




