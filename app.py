import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from utils import *

st.set_page_config(page_title = 'Cell Tracker App', layout = 'wide', page_icon=🦠)
st.title("Cell Tracker")

########## SIDEBAR ##########
