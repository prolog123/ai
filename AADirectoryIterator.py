# Neural Network Imp code

import cv2
import numpy as np
import pandas as pd
from keras.optimizers import Adam
from keras.models import Sequential
from keras.utils import img_to_array,to_categorical
from sklearn.preprocessing import label_binarize
from sklearn.model_selection import train_test_split
from keras.layers import Conv2D,Flatten,Dense,MaxPool2D

from keras.preprocessing.image import ImageDataGenerator

base_dir = 'path/to/dataset'

train_dir = os.path.join(base_dir, 'Train') 
validation_dir = os.path.join(base_dir, 'Val')
test_dir = os.path.join(base_dir, 'Test')
test_datagen = ImageDataGenerator(rescale=1./255)
train_datagen = ImageDataGenerator(rescale=1./255)
validation_datagen = ImageDataGenerator(rescale=1. / 255)

train_generator = train_datagen.flow_from_directory(
        # This is the target directory
        train_dir,
        # All images will be resized to 224x224
        target_size=(224, 224),
        batch_size=20,
        # Since we have more than 2 classes hence we use class_mode=categorical
        class_mode='categorical')

validation_generator = validation_datagen.flow_from_directory(
        validation_dir,
        target_size=(224, 224),
        batch_size=20,
        class_mode='categorical')

test_generator = test_datagen.flow_from_directory(
        test_dir,
        target_size=(224, 224),
        batch_size=20,
        class_mode='categorical')
        
model.evaluate(test_generator)

pred=model.predict_generator(test_generator)

from keras.callbacks import EarlyStopping
early_stopping=EarlyStopping(monitor='val_loss',patience=10,mode='min')

ypred=np.argmax(pred,axis=1)
test_generator.classes
confusion_matrix(ypred,test_generator.classes)

model=Sequential()
model.add(Conv2D(32,(3,2),input_shape=(224,224,3),activation='relu'))
model.add(Conv2D(32,(3,2),activation='relu',kernel_regularizer='l2'))
model.add(MaxPool2D(pool_size=(3,3)))
model.add(Conv2D(32,(3,2),activation='relu',kernel_regularizer='l2'))
model.add(MaxPool2D(pool_size=(3,3)))
model.add(Conv2D(32,(3,2),activation='relu',kernel_regularizer='l2'))
model.add(MaxPool2D(pool_size=(3,3)))
model.add(Flatten())
model.add(Dense(20,activation='relu'))
model.add(Dense(3,activation='softmax'))
model.summary()

model.compile(optimizer=RMSprop(lr=2e-5),loss='categorical_crossentropy',metrics=['accuracy'])
history = model.fit(train_generator,steps_per_epoch=10,epochs=50,validation_data=validation_generator,validation_steps=5,verbose=2,callbacks=[early_stopping])

hist.history.keys()

import matplotlib.pyplot as plt
plt.plot(history.history['loss'],label='Training Loss')
plt.plot(history.history['val_loss'],label='Validation Loss')
plt.xlabel('Number of Epochs')
plt.ylabel('Loss')
plt.title('Training Loss v/s Validation Loss')
plt.legend()



#convert image to array
def convertImgToArray(image_path):
    try:
        image=cv2.imread(image_path)
        if(image is not None):
            image=cv2.resize(image,(256,256))
            return img_to_array(image)
        else:
            return (np.array([]))
    except Exception as e:
        print('Error:',e)

path='F:/AI lab/NeuralNetwork/Plant_images'
root_dir=os.listdir(path)
root_dir

image_list,image_label=[],[]
temp=-1
for dir in root_dir:
    allImage=os.listdir(path+'/'+dir)
    temp+=1
    for file in allImage:
        newPath=path+'/'+dir+'/'+file
        image_list.append(convertImgToArray(newPath))
        image_label.append(temp)
        
np.unique(image_label,return_counts=True)
norm_list=np.array(image_list,dtype=np.float16)/255.0
ytrain=to_categorical(ytrain)
ytest=to_categorical(ytest)
ytrain

from sklearn.metrics import r2_score
r2_score(ytest,pred)



# RNN

data.set_index('date')[['Appliances','T_out','RH_out','Visibility']].plot(subplots=True)

TimeseriesGenerator(x,y,length=2,batch_size=1)[0]

xtrain,xtest,ytrain,ytest=train_test_split(x,y,random_state=0,shuffle=False)

win_length=720
train_generator=TimeseriesGenerator(xtrain,ytrain,length=win_length,batch_size=32)
test_generator=TimeseriesGenerator(xtest,ytest,length=win_length,batch_size=32)

model=Sequential()
model.add(LSTM(32,input_shape=(win_length,4),activation='tanh',return_sequences=True))
model.add(LSTM(32,activation='tanh',return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(32,activation='tanh',return_sequences=False))
model.add(Dense(1))
model.summary()

model.compile(loss=keras.losses.MeanSquaredError(),optimizer=keras.optimizers.Adam(),metrics=[keras.metrics.MeanAbsoluteError()])

early_stopping=tf.keras.callbacks.EarlyStopping(monitor='val_loss',patience=2,mode='min')

hist=model.fit_generator(train_generator,epochs=1,validation_data=test_generator,shuffle=False,callbacks=[early_stopping])

print(xtest.shape)
print(pred.shape)

data_pred=pd.concat([pd.DataFrame(pred),pd.DataFrame(xtest[:,1:][win_length:])],axis=1)
data_pred.shape

inv_data=sca.inverse_transform(data_pred)
inv_data

data_final=inputs[pred.shape[0]*-1:]

data_final['pred_appli']=inv_data[:,0]

data_final

data_final[['Appliances','pred_appli']].plot()
