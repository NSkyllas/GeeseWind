import streamlit as st
import pandas as pd

#st.write('Hello, world!')
st.title("Pressure systems and geese")
#st.header("Do pressure systems influence the take-off decisions of Barnacle geese?")
st.subheader("Do pressure systems influence the take-off decisions of Barnacle geese?")
st.markdown("Studies increasingly show that wind conditions play an important role in shaping the movement and distribution patterns of migratory birds. 
We tracked barnacle geese Branta leucopsis from three populations that breed in geographically disparate locations—Greenland, Svalbard and Arctic Russia—and have 
markedly different migratory routes. We show that barnacle geese from all three locations select supportive wind conditions for their migratory departure, especially in autumn, 
suggesting that all three populations experience stronger time constraints in spring. We also show that barnacle geese do not change their migration route or duration under 
different wind conditions; rather, they opt for the same route and incur additional costs when encountering unsupportive wind conditions. Furthermore, we found no clear 
differences between populations in the amount of wind support or wind-related cost. The total air distance on spring migration was on average … of the great circle distance on 
all three routes. However, the accumulated energetic cost varied considerably among individuals and years. Future research should investigate whether this variation translates 
in differences in survival and reproduction. ")

#st.subheader("This is the subheader")
st.caption("This is the caption")
#st.code("x = 2021")
#st.latex(r''' a+a r^1+a r^2+a r^3 ''')
#st.checkbox('Yes')
#st.button('Click Me')
#st.radio('Pick your gender', ['Male', 'Female'])
#st.selectbox('Pick a year', ['2002', '2003'])
#st.multiselect('Choose a planet', ['Jupiter', 'Mars', 'Neptune'])
#st.select_slider('Pick a mark', ['Bad', 'Good', 'Excellent'])
#st.slider('Pick a number', 0, 50)

year = st.selectbox(
    'Pick a year',['No selection', '2019', '2020', '2021', '2022', '2023'])
population = st.selectbox('Pick a population', ['No selection', 'Greenland', 'Svalbard', 'Russia'])
season = st.selectbox('Pick a season', ['No selection', 'Spring', 'Autumn'])

'You selected: ', population, year, season

if (population == 'Greenland') & (year == '2020') & (season == 'Spring'):
	st.video('Gr_2020_spring-ezgif.com-gif-to-mp4-converter.mp4')
elif (population == 'Greenland') & (year == '2020') & (season == 'Autumn'):
        st.video('Gr_2020_autumn-ezgif.com-gif-to-mp4-converter.mp4')
elif (population == 'Greenland') & (year == '2021') & (season == 'Spring'):
        st.video('Gr_2021_spring-ezgif.com-gif-to-mp4-converter.mp4')
elif (population == 'Greenland') & (year == '2021') & (season == 'Autumn'):
        st.video('Gr_2021_autumn-ezgif.com-gif-to-mp4-converter.mp4')
elif (population == 'Greenland') & (year == '2022') & (season == 'Spring'):
        st.video('Gr_2022_spring-ezgif.com-gif-to-mp4-converter.mp4')
elif (population == 'Greenland') & (year == '2022') & (season == 'Autumn'):
        st.video('Gr_2022_autumn-ezgif.com-gif-to-mp4-converter.mp4')
elif (population == 'Greenland') & (year == '2023') & (season == 'Spring'):
        st.video('Gr_2023_spring-ezgif.com-gif-to-mp4-converter.mp4')

elif (population == 'Russia') & (year == '2019') & (season == 'Spring'):
        st.video('Ru_2019_spring-ezgif.com-gif-to-mp4-converter.mp4')
elif (population == 'Russia') & (year == '2019') & (season == 'Autumn'):
        st.video('Ru_2019_autumn-ezgif.com-gif-to-mp4-converter.mp4')
elif (population == 'Russia') & (year == '2020') & (season == 'Spring'):
        st.video('Ru_2020_spring-ezgif.com-gif-to-mp4-converter.mp4')
elif (population == 'Russia') & (year == '2020') & (season == 'Autumn'):
        st.video('Ru_2020_autumn-ezgif.com-gif-to-mp4-converter.mp4')
elif (population == 'Russia') & (year == '2021') & (season == 'Spring'):
        st.video('Ru_2021_spring-ezgif.com-gif-to-mp4-converter.mp4')
elif (population == 'Russia') & (year == '2021') & (season == 'Autumn'):
        st.video('Ru_2021_autumn-ezgif.com-gif-to-mp4-converter.mp4')
elif (population == 'Russia') & (year == '2022') & (season == 'Spring'):
        st.video('Ru_2022_spring-ezgif.com-gif-to-mp4-converter.mp4')
elif (population == 'Russia') & (year == '2022') & (season == 'Autumn'):
        st.video('Ru_2022_autumn-ezgif.com-gif-to-mp4-converter.mp4')
elif (population == 'Russia') & (year == '2023') & (season == 'Spring'):
        st.video('Ru_2023_spring-ezgif.com-gif-to-mp4-converter.mp4')
elif (population == 'Russia') & (year == '2023') & (season == 'Autumn'):
        st.video('Ru_2023_autumn-ezgif.com-gif-to-mp4-converter.mp4')

elif (population == 'Svalbard') & (year == '2020') & (season == 'Autumn'):
        st.video('Sv_2020_autumn-ezgif.com-gif-to-mp4-converter.mp4')
elif (population == 'Svalbard') & (year == '2021') & (season == 'Spring'):
        st.video('Sv_2021_spring-ezgif.com-gif-to-mp4-converter.mp4')
elif (population == 'Svalbard') & (year == '2021') & (season == 'Autumn'):
        st.video('Sv_2021_autumn-ezgif.com-gif-to-mp4-converter.mp4')
elif (population == 'Svalbard') & (year == '2022') & (season == 'Spring'):
        st.video('Sv_2022_spring-ezgif.com-gif-to-mp4-converter.mp4')
elif (population == 'Svalbard') & (year == '2022') & (season == 'Autumn'):
        st.video('Sv_2022_autumn-ezgif.com-gif-to-mp4-converter.mp4')
elif (population == 'Svalbard') & (year == '2023') & (season == 'Spring'):
        st.video('Sv_2023_spring-ezgif.com-gif-to-mp4-converter.mp4')
elif (population == 'Svalbard') & (year == '2023') & (season == 'Autumn'):
        st.video('Sv_2023_autumn-ezgif.com-gif-to-mp4-converter.mp4')

else:
	'No available video for this migration'
