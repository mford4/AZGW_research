#Read_Me

These python files can be found on my GitHub repo @ https://github.com/mford4/AZGW_research

Merge Files:
Merge_WL_w_basinid.py    imports GW levels and excel containing basin ids and merges them
				and exports wl_data2 to a csv in output_files

pump_data_concat.py.      imports all csv files for pump data and merge them with cadastral id so
				they are now linked with wellid and output a csv pump_data_full

pumpdata_join_welldata.py    imports the pump data file and imports the wl data file and joins them 
					and creates pump_wl and exports it to csv


Manipulation Files:
pump_data_manipulate.py. imports pump_data_full.csv and manipulates it to make graphs
				To run this file you will need to download pump_data_full.csv which can be 				found at https://drive.google.com/drive/u/0/folders/					1J3SjjTUHMRXKCPFWZa0yb-22okZGJ1N4 you will need to change line 12 to the
				 current directory on your computer where its located

pump_wl_combined_manipulate.py     imports Pump_wl.csv file and manipulates it to make graphs 
						To run this file you will need to download Pump_wl.csv which can be 						found at https://drive.google.com/drive/u/0/folders/
						1J3SjjTUHMRXKCPFWZa0yb-22okZGJ1N4 you will need to change line 12 to the
						 current directory on your computer where its located


WL_Data_Eval.py 		imports the wl_data2.csv file and manipulates it to make graphs
				To run this file you will need to download wl_data2.csv which can be 				found at https://drive.google.com/drive/u/0/folders/					1J3SjjTUHMRXKCPFWZa0yb-22okZGJ1N4 you will need to change line 12 to the
				current directory on your computer where its located





