
from numpy import double
import streamlit as st 
from pandas import DataFrame
import numpy as np
import pymongo


# Connect with MongoDB:
myclient = pymongo.MongoClient("mongodb://localhost:27017/",username='root',password='example')


