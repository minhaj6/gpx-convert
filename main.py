# pip install gpx-converter (pip is pip3)
# https://mapstogpx.com/
# https://gpx-converter.readthedocs.io/en/latest/readme.html

from gpx_converter import Converter

# dic = Converter(input_file='gpx.gpx').gpx_to_dictionary(latitude_key='latitude', longitude_key='longitude')
# # now you have a dictionary and can access the longitudes and latitudes values from the keys
# latitudes = dic['latitude']           # list
# longitudes = dic['longitude']         # list

df = Converter(input_file='gpx.gpx').gpx_to_dataframe()

print(df)    # you got your dataframe brou