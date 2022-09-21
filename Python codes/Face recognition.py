import cv2
face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
camera = cv2.VideoCapture(0)
'''i=0
while i==0:
    
    return_value, image = camera.read()
    cv2.imwrite('opencv'+str(i)+'.png', image)
    print('Saved you current image:')
    i= i+1
camera.release()'''
path = 'C:/Users/phani/OneDrive/Desktop/softwares/Python codes/Project01/CurrImg'
count=0

def save(image,path,obj, width=300,height=300):
    x,y,w,h= obj
    facecrop = image[y:y+h,x:x+w]
    facecrop = cv2.resize(facecrop, (width,height))
    
    cv2.imwrite(path+'.jpg',imagecrop)
    print("Image saved process completed")
    
while True:
    _, image = camera.read()
    grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face.detectMultiScale(grey,1.1,4)
    for x,y,w,h in faces:
        cv2.rectangle(image, (x,y),(x+w,y+h),(0,10,0),2)
    cv2.imshow('frame',image) 
    k = cv2.waitKey(1)
    if k==27: #press escape to exit
        print("Exit")
        break
    elif k==32: # press spacebar to capture and save the image
        imagecapture = ".png".format(count)
        print('Image captured.')
        count+=1
        save(image,path,(x,y,w,h))
        break
