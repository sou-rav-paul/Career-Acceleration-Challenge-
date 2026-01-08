FUNCTION merge_sort(list):
    IF size(list)<=1 :
        RETURN list

    # Divide 
    mid = size / 2
    left = merge_sort(list[0:mid])
    right = merge_sort(list[mid:end])
    RETURN merge(left,right)
    