# InteliWaiter

This project was developed with Flask version 2.0.3

## Development server

Run `python main.py` for a dev server. Navigate to `http://localhost:5000/`. You need to manually reload if you change any of the source files.

## Code scaffolding

Run `python requirments.txt` to install all the dependencies.

## Further Info

This project uses Chatterbot's ListTrainer. The training data json files can be found in `static/data`

## Custom `preprocessor.py`

Is responsible for further evalutating the users info and comparing it with chatterbots trained data. The reponse object will be be produced more accurately.

## `popualte_trainer_data.py`

Is responsible for populating the data that needs to be trained by `ListTrainer`. This module uses `extract_data.py` to extract the ata from json file.
