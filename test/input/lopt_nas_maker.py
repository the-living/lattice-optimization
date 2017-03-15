__author__ = 'Damon, TheLiving'
__email__ = 'damon.lau@autodesk.com'

import os, sys, time, json, csv, hashlib

start = time.time()
mode = "grid"
																# BASE NAS TO LOAD              

fp_og_nas = r"tester.nas" 
fp_new_nas = r"mini.nas"
																# WORKING NAS FILE

# fp_grid = r"data\grid_hash.csv"
# fp_grid_j = r"data\existing_grid_list.json"
# fp_grid_lookup  = r"data\existing_grid_lookup.json"

# fp_grid_new_quad = r"data\grid_new_quad.json"
# fp_grid_quad_lookup = r"data\grid_quad_lookup.json"

fp_existing_grid = r"existing_grid.json"
fp_existing_grid_lookup = r"existing_grid_lookup.json"
fp_grid_feet  = r"feet_grid.json"
fp_rbe  = r"rbe.json"
fp_setup_points = r'setup_points.json'

# fp_grid_new = r"parallels\{}\grid_new.csv".format(direction)
# fp_json_new = r"parallels\{}\grid_new.json".format(direction)
# fp_lookup_new = r"parallels\{}\grid_lookup_new.json".format(direction)
# fp_cbar_new = r"parallels\{}\cbar_new.json".format(direction)

																# load option A lines
old_nas = open(fp_og_nas)
nas_txt = old_nas.read()
																# load all nas data_j

d = open(fp_existing_grid)
data_grid_j = json.load(d) 


d = open(fp_existing_grid_lookup)
data_grid_lookup = json.load(d) 


d = open(fp_grid_feet)
data_quad = json.load(d) 


d = open(fp_setup_points)
data_sp_points = json.load(d)  



print('data_grid_j: ',  str(data_grid_j)[0:200], '\n')
print('data_grid_lookup: ',  str(data_grid_lookup)[0:200], '\n')
# print('\n\ngrid dict: ', grid_D)

																# match line end points with nas grid
last = 50000001             # base number for CBAR
# last = 91000001             # base number for RBE
grid_D = {}

lookup_fresh = {}

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

base_last = 20000000
grid_base = {}

def find_grid_hash(p):

	coord = pt_string(p)
	key_H = hashbrown(coord)

	try:								# if point already exists
		b = data_grid_lookup[key_H]
		grid_base[key_H] = b
		# print("existing key", key_H, b, p)
		return b
																			#if point is in quad grid list

	except Exception as e:						#if new point
		last_count = len(grid_D) + last + 1
		print("no match------------------------key", key_H, last_count, e)

		data_grid_lookup[key_H] = str(last_count)
		lookup_fresh[key_H] = str(last_count)

		grid_D[last_count] = (x, y, z)

		

		return last_count

																#find CBAR end points

pload_quads = []

def cquad(fp_json, fp_json_lookup):
	new_grid = []
	quads = []
	quad_str = ""

	# d = open(fp_json)
	data_q = fp_json

	# d1 = open(fp_json_lookup)
	data_q_lu = fp_json_lookup 

	start = 30000001								 # base number for CQUAD (40000000 for CQUAD grid points)

	for key, value in data_q.items():
		# print('quad', key, value)
		try:
			vertex1 = data_q_lu[ hashbrown(pt_string(value['v0'])) ]
			vertex2 = data_q_lu[ hashbrown(pt_string(value['v1'])) ]
			vertex3 = data_q_lu[ hashbrown(pt_string(value['v2'])) ]
			vertex4 = data_q_lu[ hashbrown(pt_string(value['v3'])) ]

			if value['pload'] == 1:
				pload_quads.append(start)

			quad_unit = [vertex1, vertex2, vertex3, vertex4]
		
			new_txt = "{:<8}{:<8}{:<8}{:<8}{:<8}{:<8}{:<8}".format("CQUAD4",start ,102 , vertex1, vertex2, vertex3, vertex4)
			start += 1


			quad_str = quad_str + "\n" + new_txt
		except Exception as e:
			print("exception CQUAD4",start ,102 , vertex1, vertex2, vertex3, vertex4, e)

	return quad_str


def rbe(RBE_c, RBE_s, points):

	spoke = []

	eid = len(points) + 1
	spokeList = []
	outputGRID = "\n"
	outputGRID_2 = "\n"

	for c, i in enumerate(RBE_c):
		
		outputT = "{:<9}{:<8}{:<8}{:<8}{:<7}{:<9}{:<8}".format('RBE3',eid+c, '', data_grid_lookup[i], '123456', '1.', '123')
		outputR = "{:<9}{:<8}{:<8}{:<8}{:<7}".format('RBE2',eid+c, '', data_grid_lookup[i], '123456')
		
		
		for c1, j in enumerate(spoke[c]):
			if c1 < 2:
				outputT = "{}{:<8}".format(outputT,j)
			if (c1+6)% 8 == 0 and c1 >= 2:
				outputT = "{} \n{:<9}{:<8}".format(outputT,'',j)			
			if (c1+6)% 8 != 0 and c1 >= 2:
				outputT = "{}{:<8}".format(outputT,j)
		
		for c2, j in enumerate(spoke[c]):
			if c2 < 5:
				outputR = "{}{:<8}".format(outputR,j)
			if c2 == 5:
				outputR = "{} \n{:<9}{:<8}".format(outputR,'',j)	
			if (c2+6)% 8 == 0 and c2 >= 5:
				outputR = "{} \n{:<9}{:<8}".format(outputR,'',j)			
			if (c2+6)% 8 != 0 and c2 >= 5:
				outputR = "{}{:<8}".format(outputR,j)
				
		outputGRID_2 = outputGRID_2 + outputR + '\n'		
		outputGRID = outputGRID + outputT + '\n'

	#$ ------1-------2-------3-------4-------5-------6-------7-------8-------9-------0
	#BE3     6600            6436    123456 1.       123     2384    2539
	#        2673    2768    3753    3894    4077

	outputGRID = outputGRID +"\n\n\n$end RBE3"
	outputGRID_2 = outputGRID_2 +"\n\n\n$end RBE2"


print("\n\n grid len", len(data_grid_lookup))

for key, value in data_grid_j.items():
	a  = [ value[0], value[1], value[2] ]
	pair = find_grid_hash(a)
	# print("pair", a, pair, pair[0])
	try:
		grid_D[pair] = value
	except Exception as e:
		print(" grid error ", pair, value, e)


# print(grid_base)
															# write new GRID points

nas_grid = ""

for key, value in grid_D.items():
	output = "GRID    {:<8}        {:<8}{:<8}{:<8}  ".format(key, value[0], value[1], value[2] )
	nas_grid = nas_grid + '\n' + output


rbe_ind = []
cbar_list = {}
nas_rbe = ""


d = open(fp_rbe)
data_rbe = json.load(d) 

															# make RBE elements

# for n, i in enumerate(data_rbe):
# 	mp  = ( i['mp'])
# 	s1 = ( i['s1'] )  
# 	s2 = ( i['s2'] )  
# 	s3 = ( i['s3'] )  
# 	s4 = ( i['s4'] )  


# 	sp_all = [find_grid_hash(mp), find_grid_hash(s1), find_grid_hash(s2), find_grid_hash(s3), find_grid_hash(s4)]
# 	print("rbe ", mp, s1, pair)
	
# 	rbe_unit = rbe(mp, sp_all, data_grid_j)
# 	print(rbe_unit)

# print("rbe ind ", rbe_ind)


rbe_num = 90000000
for n, i in enumerate(data_rbe):
	cbar_id = str(n + rbe_num)
	connT = "RBE3    {:<8}{:<8}{:<8}{:<8}{:<8}{:<8}{:<8}  ".format( cbar_id, "", find_grid_hash(i["point1"]), "123456", "1.", "123", find_grid_hash(i["point2"]) )

	nas_rbe = nas_rbe + "\n" + connT 

print("RBE", nas_rbe)

															# make CQUAD elements

nas_quad = cquad(data_quad, data_grid_lookup)
# print("CQUAD", nas_quad)


															# make LOAD and SPC points
load = ""
spc = ""
#LOAD4  1       300000011777.6  1777.6  1777.6  1777.6 
#ORCE   1       20000005        999.    0.0     0.0     1.0
#PC     1       20000001123456

nas_sp = ""
load_m = -5.1  					#LOAD CASE FOR SHELL
print("special points ", data_sp_points)
for n, i in enumerate(data_sp_points):
	if i[0] >  92000000:
		id_pt = find_grid_hash([i[1], i[2], i[3]])

		connT = "{:<8}{:<8}{:<8}{:<8}{:<8}{:<8}{:<8}{:<8} ".format("PLOAD", 1, id_pt, "",0.0, load_m, 0.0, 1.0)
		nas_sp = nas_sp + "\n" + connT 

		# print('load element', n, i , id_pt)
	else:
		id_pt = find_grid_hash([i[1], i[2], i[3]])

		connT = "SPC     {:<8}{:<8}{:<8} ".format(1, id_pt, 123)
		nas_sp = nas_sp + "\n" + connT 

for n, i in enumerate(pload_quads):
	connT = "{:<8}{:<8}{:<8}{:<8}{:<8}{:<8}{:<8} ".format("PLOAD4", 1, i, load_m, load_m, load_m, load_m )
	nas_sp = nas_sp + "\n" + connT 


# print("\nRBE lines: ", nas_rbe)
															# new NASTRAN file
print('\nnas maker - opening ', fp_og_nas)

old_nas = open(fp_og_nas)
nas_txt = old_nas.read()
cbar_start = nas_txt.find("$start Grid")
grid_start = nas_txt.find("$end Grid")
load_end = nas_txt.find("$load")

new_txt = "{}\n\n{}\n\n$end_grid_pt \n\n$cquad\n{}\n\n$rbe\n{}\n\n$spc + load points\n {}\n{}".format(nas_txt[:cbar_start], nas_grid, nas_quad, nas_rbe, nas_sp, nas_txt[load_end:])

with open(fp_new_nas, "w") as f:
	f.write( new_txt )



print("\n-----------------------------new points grid D: ", len(grid_D))

end = time.time()
print("\nnastran maker has used up {} seconds of your time".format( round(end-start,3) ), "\n" )








# with open(fp_grid) as csvfile:
# 	reader = csv.reader(csvfile)
# 	for row in reader:
# 		grid.append(row)

# 		x = round( float(row[1]), 3 )
# 		y = round( float(row[2]), 3 )
# 		z = round( float(row[3]), 3 )
	
# 		coord = str(x) + str(y) + str(z)
# 		# key_H = hashbrown(coord)
# 		key_H = row[4]

# 		grid_lookup[key_H] = row[0]
# 		grid_D[row[0]] = (x, y, z)
