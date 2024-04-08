![image](https://github.com/heroamd/EasyTyporaTransformToGridea/assets/47046657/74b049b7-b21c-4a02-b7e1-10f6dfb35949)
## EasyTyporaTransformToGridea is an easy way to create and edit MD documents with Typora and deploy them to pages by Gridea.
## The most inconvenient part of using Gridea is how to quickly replace the picture file PATHs and copy picture files to adapt to the Gridea environment.

### This script help you use Typora as MD document editor and use Gridea as deployor for your own Blog.

### Here is the using DEMO:

##### 1、Your configuration for image insert in Tyopra must as: 
First, When insert: Copy image to custom folder, and the folder path should be as './pic'
![image](https://github.com/heroamd/EasyTyporaTransformToGridea/assets/47046657/66be05c4-8c08-41bc-aff1-74e08ee83067)
then, when you insert a new image, here is the line in your document:
Just like: `![image-1](.\pic\image-1.png)`
![image](https://github.com/heroamd/EasyTyporaTransformToGridea/assets/47046657/33233e7b-3ebe-4ae7-a1c9-ac99da1f80f2)

##### 2、Then you need to copy one of the ENGLISH version or CHINESE version script in your folder, and modify these path:
![image](https://github.com/heroamd/EasyTyporaTransformToGridea/assets/47046657/24171d47-e3a1-4fcc-82a5-56116aa20c17)
+ THE directory_path REFER to your <Gridea project was created path>/poster, such as 'D:/blog/posts'
+ THE dst REFER to <The directory location for storing images in Gridea>/post-images, such as 'D:/blog/posts/post-images'
+ THE pic_path REFER to <The default location where Typora automatically saves inserted images>/pic. such as  'C:/Users/xxx/Desktop/master/Notes/pic/'
+ THE new_base_path means the replaced image path in your unmodified MD document. Such as 'file://D:/blog/posts/post-images/' Tips: must same as 'dst' PATH

* IMPORTANT: use '/' but not '/\' in windows!!!!

* THIS SCRIPT WILL AUTO COPY IMAGE FILES TO GRIDEA IMAGE_PATH AND REPLACE THE OLD MD DOCUMENTS!

* ![Uploading 9b28b00c805014d4c23acabba0f348d.jpg…]()

