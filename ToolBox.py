

#딕셔너리를 csv파일로
def dict_to_file(dic, filename ):
    with open(f'data/date/{filename}.csv', 'w') as f:

        if dic == None:
            f.writelines([])
        else:

            list = []
            for i in [*dic[[*dic][0]]]:
                list.append(str(i))
                list.append(',')
            list[-1] = '\n'
            # print(list)
            f.writelines(list)

            for i in [*dic]:
                list = []
                for ii in [*dic[i]]:
                    list.append(str(dic[i][ii]))
                    list.append(',')
                list[-1] = '\n'
                # print(list)
                f.writelines(list)



#딕셔너리 순서정렬
def dict_sort(dict0, key0='key0'):
    dict0 = {k:v for k, v in sorted(dict0.items(), reverse=True, key=lambda item: item[1][key0])}
    return dict0
