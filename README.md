# SI507-project

Code for the final project of SI507.

To run the flask app:

1. Go to `flask` directory and run:

   ```python
   python3 app.py
   ```

2. Open the browser and go to: <http://127.0.0.1:5000>

3. In the terminal, press `CTRL+C` to quit.

To update data:

1. Go to `retrieve_data` directory.

2. You need a client id and corresponding secret from Battle.net API and create a file called `client.txt` under this directory like:

   ```text
   xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx  // first line is id
   xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx  // second line is secret
   ```

3. Clear **all** JSON files in `data` and `raw_data` folder to clear cache.

4. Run following commands in the terminal under `retrieve_data` directory:

   ```python
   python3 cards_data_collection.py
   python3 meta_data.py
   python3 crawl_deck_data.py
   python3 link_deck_data.py
   python3 organize_data.py
   ```

5. Check directory structure:

   ```text
   .
   ├── cache.py
   ├── cards_data_collection.py
   ├── client.txt
   ├── crawl_deck_data.py
   ├── data // the data used in flask app
   │   ├── cards_tree.json
   │   └── decks_tree.json
   ├── link_deck_data.py
   ├── meta_data.py
   ├── oauth_token.py
   ├── organize_data.py
   └── raw_data
       ├── cards.json
       ├── decks.json
       ├── decksMeta.json
       └── metaInfo.json
   ```

**Required packages**: flask, requests, logging, sys, urllib, BeautifulSoup, operator, json.
