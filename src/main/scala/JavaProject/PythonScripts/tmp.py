import pymongo 
import sys 
import os 
from pymongo import MongoClient 
from moveBatch import moveBatch
rString = moveBatch([0.37301711552435846,0.0869497194140938,0.6146458354668716,0.3046446626318081,0.09569713669220825,0.2970030603927247,0.15450626166378467,0.7274549888779412,0.7448103391579374,0.5507167749126036,0.643319016875172,0.2902996485546889,0.2560512404962657,0.7621487944503191,0.14788064928093914,0.7641896346223487,0.6069035043032824,0.6921827718858085,0.6509849493169236,0.25128836941166255,0.5958807149923653,0.7760467010579876,0.3135344793685563,0.1807003026811409,0.3254000214175268,0.4784582106386963,0.18452713409931276,0.188326351109822,0.07482750566078455,0.49850730732138937,0.10118613636256513,0.7006386544296328,0.5969244771276366,0.38188245103953755,0.24080084697656867,0.5455742374382531,0.7088317509416351,0.04709613439514537,0.34181016183805435,0.6935818212156517,0.7468996564812764,0.24639232513679732,0.41857453176831527,0.4404957118494788,0.7815307876956975,0.6230302421516615,0.5547792077428918,0.31829003701339664,0.5983945111852687,0.4143417845216475,0.7943491159979813,0.6086659474975054,0.3953295917787103,0.48229840835440785,0.1990312180758128,0.3299298032398005,0.5820372793551308,0.511115205768274,0.47183917377113416,0.3972446145712648,0.5405945794936816,0.5566305734030274,0.6589842783469988,0.4962416700799247,0.09445190421281824])
print str(rString)
