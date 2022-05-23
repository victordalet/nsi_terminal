def mini(t_moy,annees):
	t_min = t_moy[0],annees[0]
	for i in range(len(t_moy)):
		if t_moy[i] < t_min[0]:
			t_min = t_moy[i],annees[i]
	return t_min

def main():
	t_moy = [14.9, 13.3, 13.1, 12.5, 13.0, 13.6, 13.7]
	annees = [2013, 2014, 2015, 2016, 2017, 2018, 2019]
	print(mini(t_moy, annees))

main()