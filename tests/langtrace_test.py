from langtrace_python_sdk import langtrace
from langtrace_python_sdk.utils.with_root_span import with_langtrace_root_span

langtrace.init(
  api_key="1fd09381c672c900dc18e0dcf26718f4451e480e57204489d88e95c772db02d0"
)

from openai import OpenAI

@with_langtrace_root_span()
def example():
  client = OpenAI()
  response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {
          "role": "system",
          "content": "How many states of matter are there?"
      }
    ],
  )
  print(response.choices[0].message.content)

example()