from flask import Flask, render_template
import requests
from lxml import html

app = Flask(__name__)


@app.route('/pokemon/<query>', methods=['GET'])
def show_query(query):
    response = requests.get('https://pokeapi.co/api/v2/pokemon-species/' + query)
    
    if query.isnumeric():
        query_value = response.json()["name"]
        return render_template('pokemon.html', message = 'The pokemon with id %d is %s' % (int(query), query_value))
    
    else:
        query_value = response.json()["id"]
        string = str(query).capitalize()
        return render_template('pokemon.html', message = '%s has id %d' % (string, query_value))
    

def main():

    return render_template('pokemon.html')


if __name__ == '__main__':
    app.run()
