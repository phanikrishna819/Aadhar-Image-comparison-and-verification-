import cv2
import dlib
detector = dlib.get_frontal_face_detector()
def save(image,path,obj, width=300,height=300):
    x,y,w,h= obj
    imagecrop = image[y:h,x:w]
    imagecrop = cv2.resize(imagecrop, (width,height))
    
    cv2.imwrite(path+'.jpg',imagecrop)
    print("Image saved process completed")

#--------------------------------Starting point----------------------------------
photo = cv2.imread('upload your Aadhar card image here')
path = 'here enter the path to save the image'
gray = cv2.cvtColor(photo,cv2.COLOR_BGR2GRAY)
faces  = detector(gray)
'''start_point = [375, 300]
end_point = [100, 600]
color = (0,10, 0)
thickness = 4'''    
for counter, face in enumerate(faces):
        print(counter)
        x,y = face.left(), face.top()
        w,h = face.right(), face.bottom()
        cv2.rectangle(photo, (375,250),(100,600), (0,10,0), 4)
        save(photo,path+str(counter),(x,y,w,h))
#image = cv2.rectangle(photo, start_point, end_point, color, thickness)
# Displaying the image 
photo = cv2.resize(photo,(800,800))
cv2.imshow('img', photo) 
cv2.waitKey(0) 