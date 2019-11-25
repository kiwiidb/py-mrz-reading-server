# Py-MRZ-Reader

First, we extract the MRZ based on [this PyImageSearch tutorial](https://www.pyimagesearch.com/2015/11/30/detecting-machine-readable-zones-in-passport-images/),

then we use https://github.com/konstantint/PassportEye to return the MRZ data in json format.

Flask is used to serve this over http.
