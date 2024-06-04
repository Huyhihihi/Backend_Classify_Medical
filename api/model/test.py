from api.model.models import Dataset, Model
from api.user.models import User

user = User.objects.create(username="admin",password="1234", email="admin@gmail.com",name="anh le")
data= Dataset.objects.create(path="medical6",class_num = 9)
model = Model.objects.create(path="yolov8-cls.pt",user=user,dataset=data)