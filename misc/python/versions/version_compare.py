s1="TestPackage-1.2.18"
s2="TestPackage-1.2.215"
s3="TestPackage-1.2.210"

#-1 first larger, 0 equal, 1 second greater
def compare_versions(s1,s2):
  version1=s1.split("-")[1]
  v_parts1=version1.split(".")

  version2=s2.split("-")[1]
  v_parts2=version2.split(".")

  for i in range(len(v_parts1)):
    if int(v_parts1[i])>int(v_parts2[i]):
        return -1
    elif int(v_parts1[i])<int(v_parts2[i]):
        return 1

  return 0

print s1,s2,compare_versions(s1,s2)
print s2,s3,compare_versions(s2,s3)

