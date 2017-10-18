'''
@SOURCE http://zqsmm.qiniucdn.com/data/20140904220136/index.html
'''
from marshmallow import Schema, fields, pprint
 
class UserSerializer(Schema):
   class Meta:
        fields = ("id", "email", "password",)
 
class PostSerializer(Schema):
    user = fields.Nested(UserSerializer)
    
    class Meta:
        fields = ("id", "title", "body", "user", "created_at")