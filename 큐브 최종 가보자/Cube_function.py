import sys
# 큐브 초기화
def Cube_reset(Cube_type):
    Cube_reset_temp1 = []
    for i in range(6):
        Cube_reset_temp2 = []
        for j in range(Cube_type):
            Cube_reset_temp2.append([])
        Cube_reset_temp1.append(Cube_reset_temp2)
    return Cube_reset_temp1
    #print(Cube_reset_temp1)

#큐브 색깔 숫자로 변경
color_dic = {
        'w' : 1,
        'r' : 2,
        'b' : 3,
        'o' : 4,
        'g' : 5,
        'y' : 6
    }

Cube_input_list = ['Front', 'Left', 'Right', 'Top', 'Down', 'Back']
Cube_input_kind_list = ['r', 'b', 'g', 'w', 'y', 'o']
def Cube_input(Cube_type):
    Cube_list_temp = Cube_reset(Cube_type)
    for i in range(6):
        print(Cube_input_list[i])
        Cube_list_temp2 = []
        for j in range(Cube_type):
            temp = list(map(str, input().split()))
            if len(temp) == Cube_type:
                for k in range(Cube_type):
                    if temp[k] not in Cube_input_kind_list:
                        print("입력을 잘못하셨습니다")
                        sys.exit()
                Cube_list_temp2.append(temp)
            else:
                print("입력을 잘못하셨습니다")
                sys.exit()
        Cube_list_temp[i].append(Cube_list_temp2)


