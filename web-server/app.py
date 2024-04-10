import txtai, json
from flask import Flask, request, jsonify

# TXTAI Embeddings
embeddings = txtai.Embeddings(path="sebastian-hofstaetter/distilbert-dot-tas_b-b256-msmarco", content=True)

def to_displayable_text(row):
    return f"{row['url']}\n{row['summary']}"

if 'final_urls' not in globals():
    try:
        with open('./data/sublist_llm_summaries_from_pipeline.json', 'r') as f:
            final_urls = json.load(f)
    except FileNotFoundError:
        print('No file found')

if final_urls is not None:
    embeddings.index([(row["url"], to_displayable_text(row)) for row in final_urls])

def search(query, max_results=1):
    results = embeddings.search(query, max_results)
    return results

def explain(query, limit=1):
    results = embeddings.explain(query,limit=limit)
    return results

# Server
app = Flask(__name__)

@app.route('/search', methods=['POST'])
def search_endpoint():
    """Search the embeddings index."""
    data = request.get_json()
    query = data.get('query', '')
    max_results = data.get('max_results', 5)
    results = search(query, max_results=max_results)
    return jsonify({'results': results})

@app.route('/explain', methods=['POST'])
def explain_endpoint():
    """Explain the embeddings index."""
    data = request.get_json()
    query = data.get('query', '')
    max_results = data.get('max_results', 1)
    results = explain(query, max_results)
    return jsonify({'results': results})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)