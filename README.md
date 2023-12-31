Permeability-Reservoir-Rock-Prediction
====================================

Introduction
------------
Build a model for predicting permeability of reservoir rock

How to use
------------
1. Click this [streamlit web app](https://permeability-reservoir-rock-prediction-je5meccr384etxyo7jnnsu.streamlit.app/)!
2. Input your data
3. Click the predict button!

Data Understanding
------------
Dataset can be access through this link: [dataset](https://github.com/Divyanshu-ISM/Machine-Learning-Deep-Learning/blob/main/PhiK.csv)!

| Columns                                            | Definition                                                   | 
| ------------------------------------------------- | ------------------------------------------------------------ |
| `Porosity` | ratio of the volume of pores to the volume of bulk rock (fraction)/kemampuan batuan untuk menyimpan fluida |
| `Swc` | connate water saturation is the minimum water saturation which would remain adhered to the pores and not become mobile |
| `Permeability(D)` | measure of the connectivity of pores in the subsurface (Darcy)/kemampuan batuan untuk mengalirkan fluida |

Project Organization
------------
    ├── data               <- dataset for modeling
    │
    ├── model              <- final model
    │
    ├── notebooks          <- Jupyter notebooks with naming convention: a number (for ordering), a tag name,
    │                         and a short `-` delimited description, e.g. `1.0-fnk-permeability-prediction`
    │                         
    ├── reports            <- images
    │
    ├── app.py             <- streamlit web app source code
    ├── README.md          <- brief explanation about the project
    └── requirements.txt   <- requirements file for reproducing the analysis environment, e.g.
                            generated with `pip freeze > requirements.txt`

Contribute
------------
If you'd like to contribute to Permeability Prediction, check out https://github.com/fnkhairudin/Permeability-Reservoir-Rock-Prediction