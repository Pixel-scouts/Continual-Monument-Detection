import torch
BATCH_SIZE = 10 # increase / decrease according to GPU memeory
RESIZE_TO = 512 # resize the image for training and transforms
NUM_EPOCHS = 100 # number of epochs to train for
DEVICE = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
# training images and XML files directory
TRAIN_DIR = ''
# validation images and XML files directory
VALID_DIR = ''
# classes: 0 index is reserved for background
CLASSES = ['indrapura',
 'kala-bhairava',
 'trailokya mohan',
 'taleju bell_KDS',
 'taleju temple',
 'bhuvana lakshmeshvara',
 'vishnu temple',
 'gaddi durbar',
 'kumari ghar',
 'basantapur tower',
 'lalitpur tower',
 'narayan temple',
 'jagannatha temple',
 'degu tale temple_KDS',
 'panchamukhi hanuman',
 'shveta bhairava',
 'kritipur tower',
 '\\',
 'chasin dega',
 'pratap malla column',
 'bhimeleshvara',
 'kasthamandap',
 'kavindrapura sattal',
 'shiva temple',
 'simha sattal',
 'garud',
 'bhagavati temple',
 'hanuman idol',
 'bhaktapur tower',
 'king statue',
 'degutale temple',
 'kotilingeshvara']
NUM_CLASSES = 2
# whether to visualize images after crearing the data loaders
VISUALIZE_TRANSFORMED_IMAGES = False
# location to save model and plots
OUT_DIR = '../outputs'
SAVE_PLOTS_EPOCH = 2 # save loss plots after these many epochs
SAVE_MODEL_EPOCH = 2 # save model after these many epochs