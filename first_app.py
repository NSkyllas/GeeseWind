import streamlit as st
import pandas as pd

st.write('Hello, world!')
st.title("This is the app title")
st.header("This is the header")
st.markdown("This is the markdown")
st.subheader("This is the subheader")
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
	st.video('../MSc_project2_Jolieke/Publication/quiver_gifs/Gr_2020_spring-ezgif.com-gif-to-mp4-converter.mp4')
elif (population == 'Greenland') & (year == '2020') & (season == 'Autumn'):
        st.video('Gr_2020_autumn-ezgif.com-gif-to-mp4-converter.mp4')
elif (population == 'Greenland') & (year == '2021') & (season == 'Spring'):
        st.video('../MSc_project2_Jolieke/Publication/quiver_gifs/Gr_2021_spring-ezgif.com-gif-to-mp4-converter.mp4')
elif (population == 'Greenland') & (year == '2021') & (season == 'Autumn'):
        st.video('../MSc_project2_Jolieke/Publication/quiver_gifs/Gr_2021_autumn-ezgif.com-gif-to-mp4-converter.mp4')
elif (population == 'Greenland') & (year == '2022') & (season == 'Spring'):
        st.video('../MSc_project2_Jolieke/Publication/quiver_gifs/Gr_2022_spring-ezgif.com-gif-to-mp4-converter.mp4')
elif (population == 'Greenland') & (year == '2022') & (season == 'Autumn'):
        st.video('../MSc_project2_Jolieke/Publication/quiver_gifs/Gr_2022_autumn-ezgif.com-gif-to-mp4-converter.mp4')
elif (population == 'Greenland') & (year == '2023') & (season == 'Spring'):
        st.video('../MSc_project2_Jolieke/Publication/quiver_gifs/Gr_2023_spring-ezgif.com-gif-to-mp4-converter.mp4')

elif (population == 'Russia') & (year == '2019') & (season == 'Spring'):
        st.video('../MSc_project2_Jolieke/Publication/quiver_gifs/Ru_2019_spring-ezgif.com-gif-to-mp4-converter.mp4')
elif (population == 'Russia') & (year == '2019') & (season == 'Autumn'):
        st.video('../MSc_project2_Jolieke/Publication/quiver_gifs/Ru_2019_autumn-ezgif.com-gif-to-mp4-converter.mp4')
elif (population == 'Russia') & (year == '2020') & (season == 'Spring'):
        st.video('../MSc_project2_Jolieke/Publication/quiver_gifs/Ru_2020_spring-ezgif.com-gif-to-mp4-converter.mp4')
elif (population == 'Russia') & (year == '2020') & (season == 'Autumn'):
        st.video('../MSc_project2_Jolieke/Publication/quiver_gifs/Ru_2020_autumn-ezgif.com-gif-to-mp4-converter.mp4')
elif (population == 'Russia') & (year == '2021') & (season == 'Spring'):
        st.video('../MSc_project2_Jolieke/Publication/quiver_gifs/Ru_2021_spring-ezgif.com-gif-to-mp4-converter.mp4')
elif (population == 'Russia') & (year == '2021') & (season == 'Autumn'):
        st.video('../MSc_project2_Jolieke/Publication/quiver_gifs/Ru_2021_autumn-ezgif.com-gif-to-mp4-converter.mp4')
elif (population == 'Russia') & (year == '2022') & (season == 'Spring'):
        st.video('../MSc_project2_Jolieke/Publication/quiver_gifs/Ru_2022_spring-ezgif.com-gif-to-mp4-converter.mp4')
elif (population == 'Russia') & (year == '2022') & (season == 'Autumn'):
        st.video('../MSc_project2_Jolieke/Publication/quiver_gifs/Ru_2022_autumn-ezgif.com-gif-to-mp4-converter.mp4')
elif (population == 'Russia') & (year == '2023') & (season == 'Spring'):
        st.video('../MSc_project2_Jolieke/Publication/quiver_gifs/Ru_2023_spring-ezgif.com-gif-to-mp4-converter.mp4')
elif (population == 'Russia') & (year == '2023') & (season == 'Autumn'):
        st.video('../MSc_project2_Jolieke/Publication/quiver_gifs/Ru_2023_autumn-ezgif.com-gif-to-mp4-converter.mp4')

elif (population == 'Svalbard') & (year == '2020') & (season == 'Autumn'):
        st.video('../MSc_project2_Jolieke/Publication/quiver_gifs/Sv_2020_autumn-ezgif.com-gif-to-mp4-converter.mp4')
elif (population == 'Svalbard') & (year == '2021') & (season == 'Spring'):
        st.video('../MSc_project2_Jolieke/Publication/quiver_gifs/Sv_2021_spring-ezgif.com-gif-to-mp4-converter.mp4')
elif (population == 'Svalbard') & (year == '2021') & (season == 'Autumn'):
        st.video('../MSc_project2_Jolieke/Publication/quiver_gifs/Sv_2021_autumn-ezgif.com-gif-to-mp4-converter.mp4')
elif (population == 'Svalbard') & (year == '2022') & (season == 'Spring'):
        st.video('../MSc_project2_Jolieke/Publication/quiver_gifs/Sv_2022_spring-ezgif.com-gif-to-mp4-converter.mp4')
elif (population == 'Svalbard') & (year == '2022') & (season == 'Autumn'):
        st.video('../MSc_project2_Jolieke/Publication/quiver_gifs/Sv_2022_autumn-ezgif.com-gif-to-mp4-converter.mp4')
elif (population == 'Svalbard') & (year == '2023') & (season == 'Spring'):
        st.video('../MSc_project2_Jolieke/Publication/quiver_gifs/Sv_2023_spring-ezgif.com-gif-to-mp4-converter.mp4')
elif (population == 'Svalbard') & (year == '2023') & (season == 'Autumn'):
        st.video('../MSc_project2_Jolieke/Publication/quiver_gifs/Sv_2023_autumn-ezgif.com-gif-to-mp4-converter.mp4')

else:
	'No available video for this migration'
