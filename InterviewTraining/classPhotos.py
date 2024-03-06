def classPhotos(redShirtHeights, blueShirtHeights):
    # Write your code here.
	sortedRed=sorted(redShirtHeights)
	sortedBlue=sorted(blueShirtHeights)
	bluefront=True
	redfront=True
	for i in range(len(sortedRed)):
		if sortedRed[i]<=sortedBlue[i]:
			redfront=False
		if sortedBlue[i]<=sortedRed[i]:
			bluefront=False
		
	if bluefront or redfront:
		return True
	
    return False
