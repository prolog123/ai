Create Directory Iterator


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
