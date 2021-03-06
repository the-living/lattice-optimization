import os, hashlib, json, sys, datetime, time, subprocess
from subprocess import Popen
from math import sqrt

from latoptim.graph import Graph

basedir = os.curdir

											#	# sample lattice 
# sim_name = 'truss_0'
# fp_new_nas = os.path.join('nastran', '{}_100.nas'.format(sim_name))
# fp_existing_grid = os.path.join(basedir, 'nastran', 'existing_grid.json')
# fp_existing_lookup = os.path.join(basedir, 'nastran', 'lookup.json')
# fp_old_nas = os.path.join('nastran','{}.nas'.format(sim_name))
# fp_neu = os.path.join('nastran','{}_100.neu'.format(sim_name))
# fp_rsf = os.path.join('nastran', '{}_100.rsf'.format(sim_name))


												# mini test lattice 
sim_name = 'mini'
fp_new_nas = os.path.join('input','{}_100.nas'.format(sim_name))
fp_old_nas = os.path.join('input', '{}.nas'.format(sim_name))
fp_existing_grid = os.path.join('input', 'existing_grid.json')
fp_existing_lookup = os.path.join('input', 'existing_grid_lookup.json')
# fp_quad_lookup = os.path.join('nastran', 'data', 'grid_quad_lookup.json')
fp_neu = os.path.join('input','{}_100.neu'.format(sim_name))
fp_rsf = os.path.join('input', '{}_100.rsf'.format(sim_name))



											#	# comment for prototype lattice
# sim_name = 'le_og_f_r'
# fp_new_nas = os.path.join('nastran', 'data','{}_100.nas'.format(sim_name))
# fp_old_nas = os.path.join('nastran','data', '{}.nas'.format(sim_name))
# fp_existing_grid = os.path.join('nastran', 'data', 'existing_grid_list.json')
# fp_existing_lookup = os.path.join('nastran', 'data', 'existing_grid_lookup.json')
# fp_quad_lookup = os.path.join('nastran', 'data', 'grid_quad_lookup.json')
# fp_neu = os.path.join('nastran', 'data','{}_100.neu'.format(sim_name))
# fp_rsf = os.path.join('nastran', 'data', '{}_100.rsf'.format(sim_name))

grid_D = {}
data_grid_pt ={}	

d = open(fp_existing_grid)
data_grid_j = json.load(d) 	

try:
	d = open(fp_quad_lookup)		
	data_quad_lookup = json.load(d) 		
except:
	pass

d = open(fp_existing_lookup)
data_lookup = json.load(d) 		

# print("existing data_grid_j: ", str(data_grid_j))		
# print("existing data_lookup: ", str(data_lookup))	
		

def rsf_reader(output_fp):
	# read RSF

	print(fp_rsf)

	str1 = "MAXIMUM DISPLACEMENT MAGNITUDE ="
	str2 = "TOTAL MASS = "
	str4 = "MAXIMUM BAR ELEMENT VON MISES STRESS ="
	str5 = "BAR EQV STRESS "

	print("\nopening results file: ", fp_rsf)
	f = open(fp_rsf, 'r+')
	rsf = f.read() 	

	mass1 = rsf[rsf.find(str2, 40)+13:rsf.find(str2, 40)+25]
	mass1 = '{:40.6E}'.format(float(mass1)).strip()
	disp1 = rsf[rsf.find(str1, 60)+34:rsf.find(str1, 60)+46]
	disp1 = '{:40.6E}'.format(float(disp1)).strip()
	stress1 = rsf[rsf.find(str4, 70)+40:rsf.find(str4, 70)+53]
	stress1 = '{:40.6E}'.format(float(stress1)).strip()

	# design1 = [ ((float(mass1)-1.489307)*1000), float(mass1), round(float(disp1),3), round(float(stress1),3)]
	design1 = []
	design1.append(['mass','displacement','stress'])
	design1.append([float(mass1)*1000, round(float(disp1),3), round(float(stress1),3)])

	with open(output_fp, "w") as csv:
		csv.write(str(design1))	

	print( "\ncsv write done: ", output_fp ,"\n\n")
	print("rsf reader:  [mass, disp, stress]")

	return design1

def nas_run(name):

	baseDir = os.path.join(os.curdir, r'nas')

	print('\nsys arguments:', name+'.nas', '\nbase directory: ', baseDir, '\n')

	simPath = r'"C:\Program Files\Autodesk\Nastran 2016\NASTRAN.EXE"'
	initPath = r"nastran\init.ini"
	# initPath = os.path.join('nastran', 'init.ini')
	# initPath = r'C:\test\Nastrynamo\init.ini'

	# run Nastran SIM
	print('calling file: \n\n', simPath, initPath, name, '\n\n\n')
	os.system('{} {} {}'.format(simPath, initPath, name))

	return "nas written at: " + name + "\n\n"


def graph_stats(g):
	for n, i in enumerate(g):
		a = i[0] #data point 1
		b = i[1] #data point 2
		dist = sqrt(sum( (a - b)**2 for a, b in zip(a, b)))
		vol = 3.14 * (dist/2)

		print(i, dist)

	return "done"

def hashbrown(a):
    
    m = hashlib.md5()
    m.update(str(a).encode('utf-8'))
    m.digest()
    h = m.hexdigest()[:8]

    return h


def pt_string(new_pt):
	x = new_pt[0]
	y = new_pt[1]
	z = new_pt[2]

	coord = str(round(x,3)) + str(round(y,3)) + str(round(z,3))
	return coord


def find_grid_hash(p):

	last = 50000001             # base number for CBAR
	coord = pt_string(p)


	key_H = hashbrown(coord)


	try:										# if point already exists
		b = data_lookup[key_H]
		# print("match key", key_H)
		return b
	except Exception as e:
		# print('no match 1: ', e)
		try:
			c = data_quad_lookup[key_H]
			# print("..............................................quad match key", c, p)
			return c
		
		except Exception as e:										#if new point
			last_count = len(grid_D) + last + 1
			data_lookup[key_H] = str(last_count)
			grid_D[last_count] = p
			# print("----------------------------no match-------key", key_H, last_count, p)
			return last_count

pbar_num = 10000
def pbarMaker(start,end,inc):

	rad = []
	bar_dict = {}	

	r = start
	i = 0
	while r < end:
		rad.append(round(r,3))
		r = r + inc
		bar_dict[i] = 0
		i+=1

	strF = "PBAR    "  
	pbarList = "\n\n"
	strE = "        0.      0.      0.      0.      0.      0.      0.      0.\n"
	strE1 = "        0.      0.\n"		
					
	for i, a in enumerate(rad):
		#circles
		area = float(3.14159*a**2)
		i1 = (3.14159/4)*a**4
		i2 = (3.14159/4)*a**4
		j = (3.14159*(a*2)**4)/32

		newPBAR =  "$pbar r = {}\n{}{:<8}{:<8}{:<8}{:<8}{:<8}{:<8}\n{}{} \n".format(a, strF, pbar_num+i, "101", str(area)[0:7],str(i1)[0:7], str(i2)[0:7], str(j)[0:7], strE, strE1 )
		pbarList = pbarList + newPBAR

	return pbarList, rad, bar_dict 


def get_nastran_model(graph):

																				#add new grid to master grid list
																		
	cbar_ind = []	

	for n, i in enumerate(graph):
		# print("graph edges radius: ", i[2])
		# print("graph object: ", i[1], i[0])

		r = int(i[2] * 10) / 10.0
		
		radius = pbar_num + (r - 0.5) * 10
		pair = [ find_grid_hash(i[0]), find_grid_hash(i[1]), radius ]	
		cbar_ind.append(pair)																		
		# print(n, pair)

																				#write new NASTRAN string for GRID

	nas_grid = ""
	for key, value in grid_D.items():
		output = "GRID    {:<8}        {:<8}{:<8}{:<8}  ".format(key, value[0], value[1], value[2] )
		nas_grid = nas_grid + '\n' + output

	print("s_gnm - GRID:\n", nas_grid[:500])

																				#write new PBAR elem

	pbar_data = pbarMaker(0.5,6.1,0.1)
	pbar_txt = pbar_data[0]

	strB4 = "1.      1.      1."
	nas_cbar = ""
	cbar_num = 60000000

																				#create nas string for CBAR
	cbar_list = {}
	for n, i in enumerate(cbar_ind):
		cbar_id = str(n + cbar_num)
		connT = "CBAR    {:<8}{:<8}{:<8}{:<8}{}  ".format( cbar_id, str(int(i[2])), str(i[0]), str(i[1]), strB4 )
		cbar_list[cbar_id] = [str(i[0]), str(i[1])]
		nas_cbar = nas_cbar + "\n" + connT 

	print("s_gnm - \n", nas_cbar[:1000])
																				#splice new data with old Nas file
	old_nas = open(fp_old_nas)
	nas_txt = old_nas.read()

	cbar_start = nas_txt.find("$cbar")
	grid_start = nas_txt.find("$end Grid")

	print("s_gnm - NEW POINTS grid D: ", len(grid_D), len(cbar_list) )

	new_txt = "{}\n{}\n{}\n{}\n{}\n{}".format(nas_txt[:cbar_start], nas_cbar, nas_txt[cbar_start:grid_start], "$pbar_txt", nas_grid, nas_txt[grid_start:])


	graph_stats(graph)

	with open(fp_new_nas, "w") as f:
		f.write( new_txt )

	with open('edge_output.txt', "w") as f:
		f.write( str(graph) )

	return graph


# function to simulate model in Nastran
def compute_nastran_model():

    																	# RUN NASTRAN
	nas_run(fp_new_nas)

																		#open results NEU file
	print("s_cnm - opening .neu results file: ", fp_neu)

	with open(fp_neu) as csvfile:
		csv_string = csvfile.read()

	s1 = 'TOTAL TRANSLATION'
	s2 = '-1,0.,'
	s3 = 'T1 TRANSLATION'
	s4 = 'BAR EQV STRESS'
	s5 = 'BAR SA-AXIAL'
	s6 = 'BAR SA-C'

	f3 = csv_string.find(s4)

	s4a = csv_string[f3+len(s4):]
	s4b = s4a[:s4a.find(s2)]
	s4b_list = s4b.split('\n')
	stress_list_vm = []

	for i in s4b_list[4:]:
		try:
			a = i.split(',')
			b = int(a[0])
			c = float(a[1])
			stress_list_vm.append([b,c])
		except Exception as e:
			print('s_cnm - exception stress finder: ', e)
			pass

	print("\ns_cnm - von mises stress: ", stress_list_vm[2:20], "\n")
	rsf_reader('simmary.csv')

	return stress_list_vm[2:]
