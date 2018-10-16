from skimage import color
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
import numpy as np
img=mpimg.imread("task2.jpg")
orig=img
img=color.rgb2gray(img)
#plt.imshow(img)
#plt.show()
def laplace(im):
   #laplace
   kernel=np.array([[1,1,1],[1,-8,1],[1,1,1]])
   ker=np.flipud(np.fliplr(kernel))
   output=np.zeros_like(im)
   impad=np.zeros((im.shape[0]+4,im.shape[1]+4))
   impad[2:-2,2:-2]=im
   for x in range(im.shape[1]):
       for y in range(im.shape[0]):
           output[y,x]=(ker*impad[y:y+3,x:x+3]).sum()
   stacim=color.gray2rgb(output);
   plt.axis("off");
   plt.imshow(stacim);
   plt.title('Laplace');
   plt.show();
def average(im):
   #blur
   kernel=np.ones([25,25])
   ker=np.flipud(np.fliplr(kernel))
   output=np.zeros_like(im)
   impad=np.zeros((im.shape[0]+24,im.shape[1]+24))
   impad[12:-12,12:-12]=im
   for x in range(im.shape[1]):
       for y in range(im.shape[0]):
           output[y,x]=(ker*impad[y:y+25,x:x+25]).sum()
   plt.axis("off")
   plt.imshow(output,cmap=plt.get_cmap('gray'))
   plt.show();

def shor(im):
   #sobel horizontal
   kernel=np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
   ker=np.flipud(np.fliplr(kernel))
   output=np.zeros_like(im)
   impad=np.zeros((im.shape[0]+4,im.shape[1]+4))
   impad[2:-2,2:-2]=im
   for x in range(im.shape[1]):
       for y in range(im.shape[0]):
           output[y,x]=(ker*impad[y:y+3,x:x+3]).sum()
   plt.axis("off");
   plt.imshow(output,cmap=plt.get_cmap('gray'));
   plt.title('Sobel Horizontal');
   plt.show();

def sver(im):
   #sobel vertical
   kernel=np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
   ker=np.flipud(np.fliplr(kernel))
   output=np.zeros_like(im)
   impad=np.zeros((im.shape[0]+4,im.shape[1]+4))
   impad[2:-2,2:-2]=im
   for x in range(im.shape[1]):
       for y in range(im.shape[0]):
           output[y,x]=(ker*impad[y:y+3,x:x+3]).sum()
   plt.axis("off");
   plt.imshow(output,cmap=plt.get_cmap('gray'));
   plt.title('Sobel Vertical');
   plt.show();

def hboost(im):
   #highboost
   kernel=np.array([[-1,-1,-1],[-1,17,-1],[-1,-1,-1]])
   ker=np.flipud(np.fliplr(kernel))
   output=np.zeros_like(im)
   impad=np.zeros((im.shape[0]+4,im.shape[1]+4))
   impad[2:-2,2:-2]=im
   for x in range(im.shape[1]):
       for y in range(im.shape[0]):
           output[y,x]=(ker*impad[y:y+3,x:x+3]).sum()
   plt.axis("off");
   plt.imshow(output,cmap=plt.get_cmap('gray'));
   plt.title('High Boost');
   plt.show();

#laplace RGB

input_dict={1:'Blur',2:'Sobel horizontal',3:'Sobel Vertical',4:'High Boost ', 5: 'Laplace'}
print ("select an option: /n 1: Average /n 2: Sobel horizontal /n 3:Sobel vertical /n 4: High Boost /n 5 : Laplace" )
option= input("Enter the option selected: ")



while option:

   switcher={

   1: average(img),
   2: shor(img),
   3: sver(img),
   4: hboost(img),
   5: laplace(img),

   }
   option=input("Enter the option to select and 0 to finish: ")

print ("Finished!")

