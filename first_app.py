import streamlit as st
import pandas as pd

#st.write('Hello, world!')
st.title("Pressure systems and geese")
#st.header("Do pressure systems influence the take-off decisions of Barnacle geese?")
st.subheader("Do pressure systems influence the take-off decisions of Barnacle geese?")
st.markdown("Have you ever wondered how birds manage to fly such long distances? It turns out wind plays a huge role. Birds often fly at speeds similar to the wind, so whether they’re flying with or against it can make all the difference.")
st.markdown("Winds are driven by pressure systems: air flows from high to low pressure, but Earth’s rotation bends this flow, creating complex wind patterns. In northern Europe, the weather is unpredictable. This region sits near the polar front, where warm tropical air meets cold Arctic air. Here, low- and high-pressure systems form frequently, creating a constantly shifting “wind map” that birds must navigate. Migrating birds can use these winds to their advantage, riding tailwinds to save energy.")
st.markdown("We tracked barnacle geese from three populations (Greenland, Svalbard and Siberia), each traveling up to 3,000 km between their Arctic breeding grounds and wintering areas. Now, we’re investigating whether these geese strategically follow the winds to make their journeys easier.")

#st.subheader("This is the subheader")
#st.code("x = 2021")
#st.latex(r''' a+a r^1+a r^2+a r^3 ''')
#st.checkbox('Yes')
#st.button('Click Me')
#st.radio('Pick your gender', ['Male', 'Female'])
#st.selectbox('Pick a year', ['2002', '2003'])
#st.multiselect('Choose a planet', ['Jupiter', 'Mars', 'Neptune'])
#st.select_slider('Pick a mark', ['Bad', 'Good', 'Excellent'])
#st.slider('Pick a number', 0, 50)
st.markdown("### Go ahead and pick a year, a population and a season:")
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

st.caption("The moving black dots depict the bird locations, the arrows show the wind direction and speed (arrow length), while the background colours represent sea level pressure (purple means low pressure, red means high pressure).")



