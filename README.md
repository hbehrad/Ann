# Ann
use artificial neural networks to differentiate between odd and even numbers
 be fore combile and test this code you must import numpy and keras in anaconda by command pip
 for example you pip in your environment to import numpy : pip install numpy
 for install keras you must first install tensorflow
 use following command in your invironment :
python3 --version
Output should be similar to:

Python 3.8.2
Run the following command to ensure that the latest version of pip is installed:

pip install --upgrade pip
To install TensorFlow for CPU and GPU processors, run the following command:

pip install tensorflow
If you’re fine with using the CPU to train your neural network, your installation is done. If you want to use your GPU to the training, you’ll need to do the following:

For AMD GPUs, refer to the article Install Tensorflow 2 for AMD GPUs
For Nvidia GPUs:
Ensure you’re running a CUDA®-enabled card
Install v11 or later of the CUDA® Toolkit
If you’re working with Deep Neural Networks, you’ll should also install the latest version of the cuDNN library
 The installation installs a slew of TensorFlow and Keras dependencies:

tensorflow                                 
├── absl-py~=0.10                          
│   └── six                                
├── astunparse~=1.6.3                      
│   ├── six<2.0,>=1.6.1                    
│   └── wheel<1.0,>=0.23.0                 
├── flatbuffers~=1.12.0                    
├── gast==0.3.3                            
├── google-pasta~=0.2                      
│   └── six                                
├── grpcio~=1.32.0                         
│   └── six>=1.5.2                         
├── h5py~=2.10.0                           
│   ├── numpy>=1.7                         
│   └── six                                
├── keras-preprocessing~=1.1.2             
│   ├── numpy>=1.9.1                       
│   └── six>=1.9.0                         
├── numpy~=1.19.2                          
├── opt-einsum~=3.3.0                      
│   └── numpy>=1.7                         
├── protobuf>=3.9.2                        
│   └── six>=1.9                           
├── six~=1.15.0                            
├── tensorboard~=2.4                       
│   ├── absl-py>=0.4                       
│   │   └── six                            
│   ├── google-auth-oauthlib<0.5,>=0.4.1   
│   │   ├── google-auth>=1.0.0             
│   │   │   ├── cachetools<5.0,>=2.0.0     
│   │   │   ├── pyasn1-modules>=0.2.1      
│   │   │   │   └── pyasn1<0.5.0,>=0.4.6   
│   │   │   ├── rsa<5,>=3.1.4              
│   │   │   │   └── pyasn1>=0.1.3          
│   │   │   ├── setuptools>=40.3.0         
│   │   │   └── six>=1.9.0                 
│   │   └── requests-oauthlib>=0.7.0       
│   │       ├── oauthlib>=3.0.0            
│   │       └── requests>=2.0.0            
│   │           ├── certifi>=2017.4.17     
│   │           ├── chardet<5,>=3.0.2      
│   │           ├── idna<3,>=2.5           
│   │           └── urllib3<1.27,>=1.21.1  
│   ├── google-auth<2,>=1.6.3              
│   │   ├── cachetools<5.0,>=2.0.0         
│   │   ├── pyasn1-modules>=0.2.1          
│   │   │   └── pyasn1<0.5.0,>=0.4.6       
│   │   ├── rsa<5,>=3.1.4                  
│   │   │   └── pyasn1>=0.1.3              
│   │   ├── setuptools>=40.3.0             
│   │   └── six>=1.9.0                     
│   ├── grpcio>=1.24.3                     
│   │   └── six>=1.5.2                     
│   ├── markdown>=2.6.8                    
│   ├── numpy>=1.12.0                      
│   ├── protobuf>=3.6.0                    
│   │   └── six>=1.9                       
│   ├── requests<3,>=2.21.0                
│   │   ├── certifi>=2017.4.17             
│   │   ├── chardet<5,>=3.0.2              
│   │   ├── idna<3,>=2.5                   
│   │   └── urllib3<1.27,>=1.21.1          
│   ├── setuptools>=41.0.0                 
│   ├── six>=1.10.0                        
│   ├── tensorboard-plugin-wit>=1.6.0      
│   ├── werkzeug>=0.11.15                  
│   └── wheel>=0.26                        
├── tensorflow-estimator<2.5.0,>=2.4.0    
├── termcolor~=1.1.0                       
├── typing-extensions~=3.7.4               
├── wheel~=0.35                            
└── wrapt~=1.12.1
Update Tensorflow and Keras Using Pip
If you already have TensorFlow and Keras installed, they can be updated by running the following command:

pip install -U tensorflow
You can verify the TensorFlow installation with the following command:

python -m pip show tensorflow
Output should be similar to: 

Name: tensorflow
Version: 2.2.0
Summary: TensorFlow is an open source machine learning framework for everyone.
Home-page: https://www.tensorflow.org/
Author: Google Inc.
Author-email: packages@tensorflow.org
License: Apache 2.0
Location: c:\python38\lib\site-packages
Requires: google-pasta, gast, six, protobuf, tensorboard, h5py, termcolor, absl-py, opt-einsum, wrapt, grpcio, keras-preprocessing, tensorflow-estimator, numpy, astunparse, wheel, scipy
Required-by:
If you intend to create plots based on TensorFlow and Keras data, then consider installing Matplotlib. For information about Matplotlib and how to install it, refer to What is Matplotlib in Python?

How to Import Keras and TensorFlow
Once TensorFlow and Keras are installed, you can start working with them. 

# Begin a Keras script by importing the Keras library:
import keras
or 

from tensorflow import keras 

# Import TensorFlow:
import tensorflow as tf
It’s not necessary to import all of the Keras and Tensorflow library functions. Instead, import just the function(s) you need for your project.

# Import the Sequential model class from Keras
# to form the framework for a Sequential neural network:
from keras.models import Sequential
For more information on working with Keras, refer to What is a Keras Model. <– link needed


 
