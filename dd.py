def unique_sorted_string(str1,str2):

    unique_chars_str1 = set(str1)
    sorted_chars_str1 = sorted(unique_chars_str1)
    result_str1 = ''.join(sorted_chars_str1)
    print(result_str1)

    unique_chars_str2 = set(str2)
    sorted_chars_str2 = sorted(unique_chars_str2)
    result_str2 = ''.join(sorted_chars_str2)
    print(result_str2)

    if len(result_str1)>len(result_str2):
        return result_str1
    elif len(str2)>len(str1):
        return result_str2
    else:
        return 'a=b'
   




x=unique_sorted_string('sdsdsdfssgr','aegefaf')
print(x)