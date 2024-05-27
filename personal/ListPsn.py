# Data with [N] persons
from enum import Enum
#means = [
#art[music,draw,dance,film],
#logic[game,math,literature,theory],
#communi[friendly,mindly,confident,mature],
#like[game,read,sport,sleep]]
class Personality(list,Enum):

    def __repr__(self):
        return self.value

    introversion = [
        [1,1,0,1],
        [0,1,1,0],
        [0,0,0,1],
        [0,1,0,1]
    ]
    extroversion = [
        [1,0,1,0],
        [1,0,0,1],
        [1,0,1,1],
        [1,0,1,0]
    ]
    individualist = [
        [1,0,0,0],
        [1,1,0,1],
        [0,1,0,1],
        [1,0,0,1]
    ]
    perfection = [
        [1,0,0,0],
        [0,1,1,1],
        [0,1,1,1],
        [0,1,1,1]
    ]
    friendly = [
        [1,0,0,1],
        [1,0,1,0],
        [1,0,1,1],
        [1,0,1,1]
    ]
    pass

# Unsupervised learning: classification, K - type of peoples
# Predict me belong to what type?
# Request 5 girl from same type.