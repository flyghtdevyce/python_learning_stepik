Flag = False

for i in range(1,151):
	if Flag:
		break
	for j in range(i,151):	
		if Flag:
			break
		if i == j:
			continue
		for k in range(j,151):
			if Flag:
				break
			if j == k:
				continue
			for l in range(k,151):
				if Flag:
					break
				if k == l:
					continue
				for m in range(l,151):
					if i ** 5 + j ** 5 + k ** 5 + l ** 5 == m ** 5:
						Flag = True 		
						break
print(i,j,k,l,m,"=",i+j+k+l+m)
