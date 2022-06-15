## Practice/Test File to try getting data from the cdaweb NASA Database and writing it to a file

## Libraries and add-ons:
## spacepy -> Recommended
## cdasws -> Required
## CDF Software -> Required? https://cdf.gsfc.nasa.gov/html/sw_and_docs.html

#### Installing Libraries using pip:
## pip install -U spacepy
## pip install -U cdasws


from cdasws import CdasWs as cda

## Instrument: (String)
instrument = 'WI_H0_SWE'

## Sample Start and End time of data (String)
## Format: [_Year_]-[_Month_]-[_Day_]T[_Hour_]:[_Minute_]:[_Second_].[_Millisecond_]Z
dataStartTime = '1998-04-11T12:00:00.000Z'
dataEndTime = '1998-04-12T12:00:09.000Z'

## Instrument Parameters (Array)
params = ['Te','Te_anisotropy','average_energy','pa_press_tensor','pa_dot_B','heat_flux_magn','heat_flux_el','heat_flux_az','Q_dot_B','sc_position','el_bulk_vel_magn','el_bulk_vel_el','el_bulk_vel_az','el_density','sc_pot','flag','major_fr_rec','major_fr_spin_number']

## get_data([__], [__], [_start-time_], [_end-time_])
stat, data = cda().get_data(instrument, params, dataStartTime, dataEndTime)

## File Location (String)
folder = "replace this"

## File Name (String)
fileName = "testfile"

## Extension Type (String)
type = ".txt"

## Write data to file
## open(_file_, _mode_) "r" = read (get from file), "a" = append (add to file), "w" = write (create or override file), "x" = create (create file), "t" = text, "b" = binary
file = open(folder + "\\" + fileName + type, "w")
file.write(str(data['el_density']))
file.close()

