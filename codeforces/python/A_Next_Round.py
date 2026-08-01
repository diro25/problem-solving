n,k=map(int,input().split())
scores=list(map(int,input().split()))
threshold_score=scores[k-1]
qualified_count=0
for score in scores:
    if score>=threshold_score and score>0:
        qualified_count+=1
print(qualified_count)