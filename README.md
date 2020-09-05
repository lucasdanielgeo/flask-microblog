# flask-microblog

The Flask Mega-Tutorial, by Miguel Grinberg - Available on [Miguel Grinberg's Blog](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)

## Setting virtualenv on bash terminal

Create de virtual enviroment:
```bash
    python -m venv venv
```
then activate with:
```bash
    source venv/Scripts/activate
```
then install packages:
```bash
    pip install -r requirements.txt
```

.flaskenv automatically imports flask's environment variables. To run with debug mode on, justa run:
```bash
    flask run
```
Or do it:

```bash
python -m venv venv && source venv/Scripts/activate && pip install -r requirements.txt
```