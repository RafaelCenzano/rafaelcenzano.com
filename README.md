# [RafaelCenzano.com](https://rafaelcenzano.com)

Flask website hosted on heroku and can be found at [https://rafaelcenzano.com](https://rafaelcenzano.com)

## Setup

Clone the repository and enter it

```
git clone https://github.com/RafaelCenzano/rafaelcenzano.com.git
cd rafaelcenzano.com
```

### Requirements

Use pip to install needed libraries

```
pip install -r requirements.txt
```

<!-- DO NOT REMOVE - contributor_list:start -->
<!-- DO NOT REMOVE - contributor_list:end -->

## Run

You can run the code with python just uncomment app.run in [run.py](run.py). To run it in development use gunicorn the command below is what I use in production
```
gunicorn run:app --preload --timeout 10 --max-requests 50
```

## Quote

A computer vision image classifier api using an advanced machine learning algorithm to classify an item in an image, but it really just say your paper is cardboard

\- Raf 2019

## License

This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details
