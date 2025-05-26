import os
from pyprojroot import here

DB_PATH = str(here("src/data/fortaleza_trajetorias.sqlite"))
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = "gpt-4o-mini"