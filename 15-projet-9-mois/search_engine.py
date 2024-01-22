import json
from meilisearch import Client
from databases import config
import mysql.connector
import markdown2
import re
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig


client = Client('http://localhost:7700', 'api_key')

def table_to_json(table_name, fields='*'):
# Connect to the database
    conn = mysql.connector.connect(
        host=config.DATABASE_HOST,
        user=config.DATABASE_USERNAME,
        password=config.DATABASE_PASSWORD,
        database=config.DATABASE_NAME
    )
    cursor = conn.cursor()
    query = f"SELECT {fields} FROM {table_name}"
    cursor.execute(query)
    rows = cursor.fetchall()
    result = []
    for row in rows:
        d = {}
        for i, col in enumerate(cursor.description):
            # Replace breakline characters with <br>
            res = re.sub(pattern_1, '', str(row[i]))
            res = re.sub(pattern_2, '', res)
            d[col[0]] = str(res).replace('\n', '').replace('\\', '').replace('*', '')
            result.append(d)
    json_result = json.dumps(result)
    return json_result

# Import JSON to meilisearch
def json_to_meilisearch(table_name, fields='*', primary_key='id'):
    client.index(table_name).delete()
    json_result = table_to_json(table_name=table_name, fields=fields)
    client.index(table_name).update_documents(primary_key=primary_key,documents=json.loads(json_result))
    client.index(table_name).update_stop_words(stop_words)
    client.index(table_name).update_ranking_rules(rules)
    return json_result

rules = [
    "proximity",
    "words",
    "typo",
    "attribute",
    "sort",
    "exactness",
    "release_date:desc"
]
# Import stop words
with open('stopwords-fr.json', 'r') as file:
    stop_words = json.load(file)

tables = {
    0:{
         'table_name': 'food',
         'fields': 'code, name, img',
         'primary_key': 'code'
      },
    1:{
         'table_name': 'recipes',
         'fields': 'id, name, time, difficulty, budget, review, nb_portions, side_food, steps, food',
         'primary_key': 'id'
    },
    2:{
         'table_name': 'articles',
         'fields': 'id, title, content',
         'primary_key': 'id'
    },
    3:{
         'table_name': 'questions',
         'fields': 'id, question, answer, state, url_article',
         'primary_key': 'id'
    }
}


# for table in tables:
#     fields = ''
#     table_name = tables[table]['table_name']
#     for field in tables[table]['fields'].split(', '):
#         if field != 'code' and field != 'id' and field != 'img':
#             fields += field + ', '
#     fields = fields[:-2]
#     print(fields)
#     primary_key = tables[table]['primary_key']
#     json_to_meilisearch(table_name, fields, primary_key)

# Retirer les balises
pattern_1 = re.compile('<.*?>')
pattern_2 = re.compile('\(.*?\)')
pattern_3 = re.compile('\[.*?\]')

data = {}
for table in tables:
    table_name = tables[table]['table_name']
    fields = tables[table]['fields']
    primary_key = tables[table]['primary_key']
    data[table] = json_to_meilisearch(table_name, fields, primary_key)
    data[table] = json.loads(data[table])


# Export json
json_data = json.dumps(data[table])
with open('data.json', 'w') as file:
    file.write(json_data)


# # Make training and testing datasets
# split_len = int(len(result) * 0.8)
# train_data = result[:split_len]
# test_data = result[split_len:]

# def formatting_func(example):
#     text = f"### Question: {example['input']}\n ### Answer: {example['output']}"
#     return text

# # Load Base Model

# base_model_id = "mistralai/Mistral-7B-v0.1"
# bnb_config = BitsAndBytesConfig(
#     load_in_4bit=True,
#     bnb_4bit_use_double_quant=True,
#     bnb_4bit_quant_type="nf4",
#     bnb_4bit_compute_dtype=torch.bfloat16
# )

# model = AutoModelForCausalLM.from_pretrained(base_model_id, quantization_config=bnb_config)

# # Tokenization

# tokenizer = AutoTokenizer.from_pretrained(
#     base_model_id,
#     padding_side="left",
#     add_eos_token=True,
#     add_bos_token=True,
# )
# tokenizer.pad_token = tokenizer.eos_token

# def generate_and_tokenize_prompt(prompt):
#     return tokenizer(formatting_func(prompt))



  