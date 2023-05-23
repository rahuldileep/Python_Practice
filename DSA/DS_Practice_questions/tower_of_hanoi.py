def TowerOfHanoi(disk,src,aux,dest):
	if disk == 1:
		print("Moving Disk 1 from source %s to destination %s"%(src,dest))
		return
	TowerOfHanoi(disk-1, src, dest, aux)
	print("Moving disk %d from source %s to destination %s"%(disk,src,dest))
	TowerOfHanoi(disk-1, aux, src, dest)

n = 3
TowerOfHanoi(n,'A','B','C') 