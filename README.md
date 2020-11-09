# AZGW_research
Matts repo for AZ groundwater data analysis

___
## Table of contents
Merge_WL_w_basinid.py    imports GW levels and excel containing basin ids and merges them
				and exports wl_data2 to a csv in output_files


pump_data_concat.py.      imports all csv files for pump data and merge them with cadastral id so
				they are now linked with wellid and output a csv pump_data_full


pump_data_manipulate.py. imports pump_data_full and manipulates it to make graphs


pumpdata_join_welldata.py    imports the pump data file and imports the wl data file and joins them
					and creates pump_wl and exports it to csv


WL_Data_Eval.py 		imports the wl data file and manipulates it to make graphs


pump_wl_combined_manipulate.py     imports the combined pump & wl data file and manipulates it
