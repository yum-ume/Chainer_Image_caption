Chainer-Slack-Twitter-Dialogue
====


## Description

This tool is for Imagenet using chiner and MicrosoftCOCO

#
### Install
If you don't install Chainer you have to install bellow
https://github.com/pfnet/chainer


MicrosoftCOCO(Python API)
```
git clone https://github.com/pdollar/coco
```


####Prepare the Data

MicrosoftCOCO(Images, Annotations)
```
http://mscoco.org/dataset/#download
```



####Prepare enviroment.yml

Installing a library bellow

##Requirements

```
Python 2.7.11
       numpy
       PIL
       scikit-image
cython  
chainer

```


#
### Usage 
#

Preparing data 1

```
*Prepare resized images(256, 256)
cd data
python prepare_data.py {YOUR_IMAGE_PATH} {YOUR_RESIZE_IMAGE_PATH} > {MS_COCO_img_label_list.txt}

*change the images' relative path to absolute path

```
Prepareing for Traing (chainer)
```
cd chainer_code/
python compute_mean.py {MS_COCO_img_label_list.txt} > {rmGray.txt}
```
Preparing data 2

```
cd data/
python rmGray.py  {MS_COCO_img_label_list.txt} {rmGray.txt} {MS_COCO_img_label_list_rmGray.txt}

```

Traing (chainer)
```
cd chainer/examples/imagenet
python train_imagenet.py {MS_COCO_img_label_list_rmGray.txt} {MS_COCO_img_label_list_rmGray.txt} --arch alex

```



#
### Code Directory Structure 
#
```
Dialogue ipython notebook and Encoder Decoder Model
  - data/　　　　　... Preparing data Code
  -　chainer_code/       ... Preparing for using chainer  Code


```

#
### Licence
#
```
The MIT License (MIT)

Copyright (c) 2016 Yumi Hamazono

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
```
#
### Author
#
Hama
### References 
#
>[Chainer]http://chainer.org/<br>
>[MicrosoftCOCO]http://mscoco.org/<br>