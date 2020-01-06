### Required

*  Python 3 (Tested with v3.6. Other versions should work fine)
*  Pretrained word vectors file [(Download)](https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit?usp=sharing)

### Optional

*  Pipenv [(Installation)](https://docs.pipenv.org/en/latest/install/)

### Setup
```sh
cd wmd-poc/
pipenv install  # Installs your dependencies
pipenv shell  # Activates your virtual environment
```
Note: If you do not want to use `pipenv`, just refer to the `Pipfile` and install the packages using `pip`.

### Running the program

*  Run `generate_model.py` once to generate the model. This would create a vector file `word_vectors.kv` in your temp folder. But you can change the code to create it wherever you like.

*  Place the `word_vectors.kv` file in project directory and run `distancer.py`.<br> If your system has enough resources, uncomment the code line: `wordVectorModel.init_sims(replace=True)` before running the program.