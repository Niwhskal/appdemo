import streamlit as st
import numpy as np
import time
import matplotlib.pyplot as plt
import base64

fig, ax = plt.subplots(figsize = (10,2))

ax.set_xlim(0,500)
ax.set_ylim(40,120)
hl, = plt.plot([], [])
plt.title('Heart rate')
tplot = st.pyplot(plt)

st.markdown('<style>body{background-color: #102224;}</style>',unsafe_allow_html=True)

def update_line(hl, new_data):
    hl.set_xdata(np.append(hl.get_xdata(), new_data[0]))
    hl.set_ydata(np.append(hl.get_ydata(), new_data[1]))
    ax.set_title('Heart rate = {}'.format(new_data[1]))
    tplot.pyplot(plt) 
    
start_execution = st.button('Run')

if start_execution:
    vidfile = open('./out2 (4).mp4', 'rb') 
    mymidia_bytes = vidfile.read()

    mymidia_placeholder = st.empty()

    mymidia_str = "data:video/ogg;base64,%s"%(base64.b64encode(mymidia_bytes).decode())
    mymidia_html = """
                    <style>video::-webkit-media-controls {
                    display: none !important;
                        }
                    </style>
                    <video width="800" height="600" controls autoplay>
                    <source src="%s" type="video/ogg">
                    Your browser does not support the video tag.
                    </video>
                """%mymidia_str

    mymidia_placeholder.empty()
    time.sleep(1)
    mymidia_placeholder.markdown(mymidia_html, unsafe_allow_html=True)

    for i in range(500):

        p = np.random.rand()

        if p>0.95:
            hr = np.random.randint(90,120)

        else:
            hr = np.random.randint(40, 90)

        time.sleep(0.3)
     
        update_line(hl,[i,hr])
    mymidia_placeholder.empty()
