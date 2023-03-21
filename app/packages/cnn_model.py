from tensorflow.keras.applications.vgg16 import VGG16
from tensorflow.keras import models, layers, regularizers
from tensorflow.keras import metrics as mets
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.utils import image_dataset_from_directory
from tensorflow import cast, expand_dims, float32
import numpy as np
from tensorflow.image import resize,resize_with_pad
from PIL import Image
import tensorflow_addons as tfa
import cv2

import matplotlib.pyplot as plt
import pickle #for history

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

batch_size = 16 #None = 1 #16 #32
IMG_SIZE = 224
seed_train_validation = 69 # Must be same for train_ds and val_ds

#path_to_dataset = os.path.join("..","..","data","food")
path_to_dataset = os.path.join("..","test_data","0_local_500")

path_to_dataset_train = os.path.join(path_to_dataset, "train")
path_to_dataset_test = os.path.join(path_to_dataset,  "test")
path_to_dataset_val = os.path.join(path_to_dataset,   "val")

#returns X_train, X_val, X_test
def load_data():
    """returns X_train, X_val, X_test
    """
    label_mode="int"
    X_train = image_dataset_from_directory(
        path_to_dataset_train,
        label_mode=label_mode,
        color_mode="rgb",
        seed=seed_train_validation,
        image_size=(IMG_SIZE, IMG_SIZE),
        batch_size=batch_size,
        shuffle=True
        )

    X_val = image_dataset_from_directory(
        path_to_dataset_val,
        label_mode=label_mode,
        color_mode="rgb",
        seed=seed_train_validation,
        image_size=(IMG_SIZE, IMG_SIZE),
        batch_size=batch_size,
        shuffle=True
        )

    X_test = image_dataset_from_directory(
        path_to_dataset_test,
        label_mode=label_mode,
        color_mode="rgb",
        seed=seed_train_validation,
        image_size=(IMG_SIZE, IMG_SIZE),
        batch_size=batch_size,
        shuffle=False
        )
    return X_train,X_val,X_test

def show_one_image():
    count = 0
    test_image, test_label = None, None

    for image, label in X_train:#.take(1):
        if count == 0 :
            test_image = image.numpy()
            test_label = label.numpy()
        count+=1
        if count > 0: break

    #if you want to see an image
    print("test label:", test_label)
    print("first test label:", test_label[0])

    plt.imshow(test_image[0]/255)
    plt.title(target_dict[test_label[0]])

    return

#functions that we'll actually need...

def create_target_dict():
    classes_dict = {}
    classes_list = [
        'apple', 'avocado', 'banana',
        'beef', 'blueberry', 'broccoli',
        'cabbage', 'bell_pepper', 'carrot',
        'cauliflower', 'celery', 'chicken',
        'aubergine', 'grape',
        'lemon', 'lettuce', 'milk', 'mushroom',
        'orange', 'pineapple',
        'pork', 'potato', 'strawberry',
        'tomato', 'white_wine', 'courgette' ] #'cucumber', kiwi, onion

    # classes_list = [
    #     'apple', 'avocado', 'banana',
    #     'strawberry', 'blueberry', 'broccoli',
    #     'lettuce', 'bell_pepper', 'carrot',
    #     'courgette', 'celery', 'milk',
    #     'aubergine', 'grape',
    #     'lemon', 'cabbage', 'chicken', 'mushroom',
    #     'orange', 'pineapple',
    #     'pork', 'potato', 'beef',
    #     'tomato', 'white_wine', 'cauliflower' ] #!!! *__*

    for i, food in enumerate(classes_list):
        classes_dict[i] = food

    return classes_dict

def load_best_model(model_name = "cnn_best_model", print_model = False):
    #load a model
    models_folder = os.path.join("","models")

    model_path = os.path.join(models_folder,model_name)

    model = models.load_model(model_path)

    print("loaded {model_name}:")

    if print_model:
        model.summary()
        print()

    return model

def load_vit_model():
    model_name = "vit_food_cherry"
    models_folder = os.path.join("","models","vit_model_cherry")
    # model_name = "new_model_21_classes"
    # models_folder = os.path.join("models")
    model_path = os.path.join(models_folder,model_name)

    loaded_model = models.load_model(model_path)

    return loaded_model


def make_vit_prediction(img_in, model,index=0):

    print(type(img_in)) # PIL Image
    print("mode: ", img_in.mode)

    rgb_image = img_in.convert('RGB')
    np_image = np.array(rgb_image)
    cheeky_bgr = np_image[:, :, ::-1].copy()
    # full_resize = cv2.resize(cheeky_bgr, (224,224))
    full_resize = cv2.resize(cheeky_bgr, (200,200))
    rgb_cv2 = cv2.cvtColor(full_resize, cv2.COLOR_BGR2RGB)
    #rgb_cv2 = full_resize[:, :, ::-1].copy() #also works, I was saving wrong variable
    # prepped_img = np.array(rgb_cv2).reshape(1,224,224,3)
    prepped_img = np.array(rgb_cv2).reshape(1,200,200,3)

    # Convert RGB to BGR
    #open_cv_image = np_image[:, :, ::-1].copy()
    #full_resize = cv2.resize(open_cv_image, (200,200))
    #prepped_img = np.array(full_resize).reshape(1,200,200,3)

#SAVING FILE
    save_folder = os.path.join("","temp")
    filename = f"vit_sees_cv2color_{index}.jpg"
    save_path = os.path.join(save_folder,filename)
    #rgb_image.save(save_path)
    cv2.imwrite(save_path, rgb_cv2)
    # resized = cv2.resize(img_in, (200,200))
    # prepped_img = resized

    result = model.predict(prepped_img)
    #result looks like [0.1, 0.4, 0.5]

    target_dict = create_target_dict()
    print("vit result: ", result)
    pred_encoded = result.argmax()
    print("vit result argmax: ", pred_encoded)
    #breakpoint()
    pred_class = target_dict[pred_encoded]
    print("vit class: ", pred_class)
    confidence = result[0][pred_encoded] #batch size 1
    rounded_confidence = "{0:.1f}".format(confidence * 100)

    return pred_class, rounded_confidence

# def make_predictions(img_list_in, model):
#     print(f"making {len(img_list_in)} predictions...")

#     predictions_out = []
#     for index, img in enumerate(img_list_in):
#         print("predicting ", index)
#         #get one prediction
#         #food, confidence = make_one_prediction(img, model,index)
#         food, confidence = make_vit_prediction(img, model,index)

#         #append to list
#         predictions_out.append((food,confidence))
#         print(f"thinks image {index} is {food}")

#     print(predictions_out)

#     return predictions_out

def make_predictions_refactored(img_list_in, model):
    print(f"making {len(img_list_in)} predictions...")

    predictions_out = []
    for index, img in enumerate(img_list_in):
        print("predicting ", index)
        #make one prediction

        rgb_image = img.convert('RGB')
        np_image = np.array(rgb_image)
        cheeky_bgr = np_image[:, :, ::-1].copy()
        # full_resize = cv2.resize(cheeky_bgr, (224,224))
        full_resize = cv2.resize(cheeky_bgr, (200,200))
        rgb_cv2 = cv2.cvtColor(full_resize, cv2.COLOR_BGR2RGB)
        #rgb_cv2 = full_resize[:, :, ::-1].copy() #also works, I was saving wrong variable
        # prepped_img = np.array(rgb_cv2).reshape(1,224,224,3)
        prepped_img = np.array(rgb_cv2).reshape(1,200,200,3)

        result = model.predict(prepped_img)
        #result looks like [0.1, 0.4, 0.5]
        print("before", result)

        result = np.array( [softmax(result[0])] )
        print("after", result)

        target_dict = create_target_dict()
        pred_encoded = result.argmax()

        # print(f"{target_dict}, argmax ----- {pred_encoded}")

    #     #breakpoint()
        pred_class = target_dict[pred_encoded]
        print("vit result123123: ", result)
        print("vit result argmax: ", pred_encoded)
        print("vit class: ", pred_class)
        confidence = result[0][pred_encoded] #batch size 1
        rounded_confidence = "{0:.1f}".format(confidence * 100)

        food, confidence = pred_class, rounded_confidence
        #food, confidence = make_one_prediction(img, model,index)
        #food, confidence = make_vit_prediction(img, model,index)

        #append to list
        predictions_out.append((food,confidence))
        print(f"thinks image {index} is {food}")

    # print(predictions_out)

    return predictions_out

#convert back from logit
def softmax(x):
    """Compute softmax values for each sets of scores in x."""
    return np.exp(x) / np.sum(np.exp(x), axis=0)

def convert_image_old(img_in):
    IMG_SIZE=224
    rgb_image = img_in.convert('RGB')
    np_image = np.asarray(rgb_image)
    image_out = resize(np_image, [IMG_SIZE,IMG_SIZE])

    return image_out

def prep_image_new(img_in,index):

    #image_orig = Image.open(img_in)
    print("type of image in:", type(img_in))

    rgb_image = img_in.convert('RGB')
    image_np = np.array(rgb_image)
    print("np image shape: ", image_np.shape)

    print("np image max: ", image_np.max())
    print("np image min: ", image_np.min())

    image_rescaled = image_np/255
    print("image_rescaled max: ", image_rescaled.max())
    print("image_rescaled min: ", image_rescaled.min())

    save_folder = os.path.join("","temp")
    filename = f"cnn_sees_{index}.jpg"
    save_path = os.path.join(save_folder,filename)
    image_rescaled.save(save_path)
    #cv2.imwrite(save_path, image_np)
    # turns everything into strawberries...
    # image_rescaled = image_np/255
    # image_resized = resize_with_pad(image_rescaled, IMG_SIZE,IMG_SIZE, antialias=True)

    #image_resized = resize_with_pad(image_np, IMG_SIZE,IMG_SIZE, antialias=True)

    image_resized = resize(image_rescaled, (IMG_SIZE,IMG_SIZE))
    print("resized image:", image_resized.shape)

    image_as_batch = cast(expand_dims(image_resized, 0), float32)
    return image_as_batch



def make_one_prediction(img_in, model, index):

    #prepped_img = convert_image_old(img_in)
    prepped_img = prep_image_new(img_in, index)

    #load model already
    # model_name = "current_best_model"
    #model = load_best_model()

    #model = app.state.cnn_model

    #add image to batch of one so can get prediction
    #image = cast(expand_dims(prepped_img, 0), float32)
    #result = model.predict(image)

    result = model.predict(prepped_img)
    #result looks like [0.1, 0.4, 0.5]

    target_dict = create_target_dict()

    pred_encoded = result.argmax()
    #breakpoint()
    pred_class = target_dict[pred_encoded]
    confidence = result[0][pred_encoded] #batch size 1
    rounded_confidence = "{0:.1f}".format(confidence * 100)

    #plt.imshow the prediction!
    #plt.title(f"We are {rounded_confidence  }% sure that this is {pred_class}")
    #plt.imshow(img_in)

    return pred_class, rounded_confidence


if __name__ == "__main__":

    #X_train, X_val, X_test = load_data()
    target_dict = create_target_dict()

    X_test = image_dataset_from_directory(
        path_to_dataset_test,
        label_mode="int",
        color_mode="rgb",
        seed=seed_train_validation,
        image_size=(IMG_SIZE, IMG_SIZE),
        batch_size=batch_size,
        shuffle=False
        )

    count = 0
    test_image_batch, test_label_batch = None, None

    for image, label in X_test:
        if count == 0 :
            test_image_batch = image.numpy()
            test_label_batch = label.numpy()
        count+=1
        if count > 0: break

    test_image = test_image_batch[1]
    test_label = test_label_batch[1]
    #plt.imshow(test_image[0]/255)
    #plt.show()
    prediction, confidence = make_one_prediction(test_image)
    print("prediction: ", prediction)
    print("confidence: ", confidence)

    print("actual label: ", test_label)
    print("actual class: ", target_dict[test_label])

    #works but loads model everytime
    #make_predictions(test_image_batch)
    make_predictions_batch(test_image_batch)

#to save model from google cloud to home dir
#➜  your_kitchen_ai git:(la_package_start) ✗ gcloud compute scp jupyter@user-managed-notebook-1678200135:~/ ./location
#gcloud compute scp --recurse jupyter@user-managed-notebook-1678200135:~/gh_folder/your_kitchen_ai/models/current_best_model/ models/
#if asks for password then give it empty

 #gcloud compute scp --recurse jupyter@user-managed-notebook-1678200135:~/gh_folder/your_kitchen_ai/models/current_best_model/ models/cnn_best_model


# gcloud compute scp --recurse jupyter@user-managed-notebook-1678200135:~/gh_folder/your_kitchen_ai/test_data/17_250_no_lime 17_250_no_lime

 #gcloud compute scp --recurse jupyter@user-managed-notebook-1678200135:~/gh_folder/your_kitchen_ai/models/vgg_cherry_picked_no_split/ models/cherry_picked_first

#gcloud compute scp --recurse jupyter@user-managed-notebook-1678200135:~/gh_folder/your_kitchen_ai/models/vgg_cherry_picked_no_split_dense_1500/ models/cherry_picked_1500

# im_bgr = cv2.imread(f"data/cherry_picked/{filename}/{file.name}")
# RGB_image = im_bgr[:, :, ::-1]
