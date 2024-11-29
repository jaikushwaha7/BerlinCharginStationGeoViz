
currentWorkingDirectory = "https://raw.githubusercontent.com/jaikushwaha7/BerlinCharginStationGeoViz/refs/heads/main"
#currentWorkingDirectory = "/mount/src/berlingeoheatmap1/"

# -----------------------------------------------------------------------------
import os
os.chdir(currentWorkingDirectory)
print("Current working directory\n" + os.getcwd())

import pandas                        as pd
from core import methods             as m1
from core import HelperTools         as ht

from config                          import pdict

# -----------------------------------------------------------------------------
@ht.timer
def main():
    """Main: Generation of Streamlit App for visualizing electric charging stations & residents in Berlin"""

    df_geodat_plz   = pd.read_csv(f'{currentWorkingDirectory}\datasets\geodata_berlin_plz.csv',delimiter=';')#
    
    df_lstat        = pd.read_csv(f'{currentWorkingDirectory}\datasets\Ladesaeulenregister.csv',delimiter=';')#
    df_lstat2       = m1.preprop_lstat(df_lstat, df_geodat_plz, pdict)#
    gdf_lstat3      = m1.count_plz_occurrences(df_lstat2)#
    
    df_residents    = pd.read_csv(f'{currentWorkingDirectory}\datasets\plz_einwohner.csv')##
    gdf_residents2  = m1.preprop_resid(df_residents, df_geodat_plz, pdict)
    
# -----------------------------------------------------------------------------------------------------------------------

    # Running the streamlit function for the app
    m1.make_streamlit_electric_Charging_resid(gdf_lstat3, gdf_residents2)


if __name__ == "__main__": 
    main()

