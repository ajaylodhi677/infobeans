"""
# 4. Cloud Storage Duplicate File Name Resolver

A cloud storage company stores uploaded filenames from users.

Sometimes multiple duplicate filenames are uploaded.

The system should:

* Keep the first occurrence unchanged
* Add (1), (2), (3)... for duplicates

### Input:

text
file file image file image data


### Output:

text
file file(1) image file(2) image(1) data"""

s=input("Enter file names :")
word=s.split()
vis=[]
s1=""
i=0
while i<len(word):
   ch=word[i]
   if ch not in vis:
      vis.append(ch)
      s1=s1+ch+" "
   else:
      c=0
      j=0
      while j<len(vis):
          if ch==vis[j]:
              c=c+1
          j=j+1
      vis.append(ch)
      s1=s1+ch+"("+str(c)+")"+" "
   i=i+1
print(s1)