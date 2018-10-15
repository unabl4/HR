# https://www.hackerrank.com/challenges/designer-pdf-viewer/problem

#!/bin/python3

# Complete the designerPdfViewer function below.
def designerPdfViewer(h, w):
    v = max(h[i] for i in map(lambda c: ord(c)-97, w))
    return v * len(w) 
    
h = list(map(int, input().rstrip().split()))
word = input()
result = designerPdfViewer(h, word)
print(result)
