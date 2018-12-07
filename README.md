# rasp-face
Face Detection using CNN on Raspberry-PI

`Training Loss: 0.0021, Accuray: 99.95% (after 30 epochs)`
`Validation Loss: 0.0452, Accuray: 99.37% (after 30 epochs)`
`Test Loss: 4.53, Accuracy: 71.64% (overfitted version 1)`

`model_low_size:`

`loss: 0.0219 - acc: 0.9930 - val_loss: 0.0511 - val_acc: 0.9902`

`test: [3.5237612545082944, 0.7782840037671743]`

# Instructions

1. Download the trained model https://drive.google.com/open?id=1KO7RXmEGuMTMZpBZrVv_5865kyx_ux20
   Low size model https://drive.google.com/open?id=1hSf3bX1I7u78hszNSaHMODUfPZaIW8hV
2. Run script rasp_test.py
3. To re-train the model with more classes -> raspberry-pi-face-detection.ipynb


# Instructions (Eigen-face)

1. Download the trained SVM model https://drive.google.com/open?id=1O_EBYmE1HuX5vcTrzG9Cw1Md4EojjsAx
2. PCA coefficients https://drive.google.com/open?id=1xx0Nnravy8MIn5v_aqFsTXDxbwCGCOxZ
2. Run script rasp_test_svm.py
3. To re-train the model with more classes -> eigen_face.ipynb