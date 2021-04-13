#这是一个弱口令生成器
#如果指定信息进行弱口令生成


class hack_password:
    def __init__(self,taskID=None,Name=None,email=None,domain=None,IDCard=None,phoneNumber=None,
                 Birth_Day=None,idnumber=None):
        self.Name = Name        # √             #将姓名设置为必填项
        self.email = email    # √
        self.domain = domain        # √
        self.IDCard = IDCard    # √
        self.phoneNumber = phoneNumber   #  √
        self.special_position = ''
        self.idNumber = idnumber#  √
        self.Birth_Day = Birth_Day#  √
        self.path = open('../Hack_pw_dict/{}.txt'.format(taskID),'a')
        self.short_name = []
        self.Name_list_all = [] # 常用名称表 含简写
    def run(self):
        special_position = ''
        for i in range(0,len(self.Name),1):
            if ord(self.Name[i]) <= ord('Z'):
                special_position=special_position+str(i)
        self.special_position = special_position
        if self.Name :
            self.By_name()
        if self.email :
            self.By_email()
        if self.domain :
            self.By_domain()
        if self.phoneNumber:
            self.By_phone()
        if self.idNumber:
            self.By_Idnunmber()
        if self.IDCard :
            self.By_IDCard()
        elif self.Birth_Day:
            self.By_Birth_Day(self.Birth_Day)
    def By_IDCard(self):
        char_ = ['.','!','@','#','_']
        end_4 = self.IDCard[-4:]
        end_6 = self.IDCard[-6:]
        B_year = self.IDCard[6:10]
        B_Month = self.IDCard[10:12]
        B_Day = self.IDCard[12:14]
        print(B_year,B_Month,B_Day)
        name_list = []
        if len(self.Name_list_all)==0:
            words = ''
            res = []
            for i in range(0, len(self.Name), 1):
                if str(i) in self.special_position:
                    words = words + self.Name[i]
            words = list(words)
            self.By_name_helper(words, 0, res)
            for j in res:
                name = self.Name
                for i in range(0, len(self.special_position), 1):
                    name = list(name)
                    name[int(self.special_position[i])] = j[i]
                name_list.append(''.join(name))
            name_list.extend([x for x in res])
        else:
            for i in self.Name_list_all:
                name_list.append(i)
        print(name_list)
        for i in name_list:
            self.write_file(i+B_year+B_Month+B_Day+end_4)
        for i in name_list:
            self.write_file(i+end_4)    #名称+身份证号后4位
        for i in name_list:
            self.write_file(i+end_6)        #名称+身份证号后6位
        next = []
        for i in name_list:
            self.write_file(i+B_Month+B_Day)   #名称+出生年月日
            self.write_file(i+B_year)
            self.write_file(i+B_year+B_Month+B_Day)
            next.append(i+B_Month+B_Day)
            next.append(i+B_year)
            next.append(i+B_year+B_Month+B_Day)
        for i in next:
            for j in char_:
                self.write_file(i+j)  #名称+身份证信息+特殊字符
    def By_Birth_Day(self,Birth_Day=None):
        B_year = Birth_Day[:4]
        B_Month = Birth_Day[4:6]
        B_Day = Birth_Day[6:8]
        char_ = ['.', '!', '@', '#', '_']
        print(B_year,B_Month,B_Day)
        name_list  = []
        if len(self.Name_list_all)==0:
            self.push_name_list(name_list)
        else:
            for i in self.Name_list_all:
                name_list.append(i)
        next = []
        for i in name_list:
            self.write_file(i + B_Month + B_Day)  # 名称+出生年月日
            self.write_file(i + B_year)
            self.write_file(i + B_year + B_Month + B_Day)
            next.append(i + B_Month + B_Day)
            next.append(i + B_year)
            next.append(i + B_year + B_Month + B_Day)
        for i in next:
            for j in char_:
                self.write_file(i+j)
    def By_domain(self):
        short_pw = self.read_file('../Hack_pw_dict/short_pw.txt','r')
        for i in short_pw:
            self.write_file(self.domain+i)
    def By_email(self):
        '''
        @360.com
        1.名称+邮箱
        '''
        name_list = []
        show_pw = self.read_file('../Hack_pw_dict/short_pw.txt','r')
        if len(self.Name_list_all)==0:
            words = ''
            res = []
            for i in range(0, len(self.Name), 1):
                if str(i) in self.special_position:
                    words = words + self.Name[i]
            words = list(words)
            self.By_name_helper(words, 0, res)
            for j in res:
                name = self.Name
                for i in range(0, len(self.special_position), 1):
                    name = list(name)
                    name[int(self.special_position[i])] = j[i]
                name_list.append(''.join(name))
            name_list.extend([x for x in res])
        else:
            for i in self.Name_list_all:
                name_list.append(i)
        for i in name_list:
            self.write_file(i+self.email)  #直接写入
        for i in name_list:
            for j in show_pw:
                self.write_file(i +j+ self.email)
    def By_phone(self):
        start_3 = self.phoneNumber[0:3]
        start_6 = self.phoneNumber[0:6]
        end_4 = self.phoneNumber[-4:]
        end_6 = self.phoneNumber[-6:]
        center_4 = self.phoneNumber[3:7]
        phone = self.phoneNumber
        words = ''
        res = []
        result = []
        char_ = []
        fo = open('../Hack_pw_dict/old_char.txt','r')
        push_ = fo.readline()
        while push_:
            push_ = push_.replace('\n','')
            char_.append(push_)
            push_ = fo.readline()
        fo.close()
        for i in range(0,len(self.Name),1):
            if  str(i) in self.special_position:
                words = words+self.Name[i]
        print(words)
        words = list(words)
        self.By_name_helper(words, 0, res)
        print(res)
        '''
        1.名字+手机尾号4 
        2.名字+手机全
        3.手机号+short_pw
        4.名字简称+手机号全
        5.
        '''
        print(center_4)
        for i in res:
            result.append(i+phone)                          ###    名称简写+加手机号
        name_list = []
        for j in res:
            name = self.Name
            for i in range(0, len(self.special_position), 1):
                name = list(name)
                name[int(self.special_position[i])] = j[i]
            name_list.append(''.join(name))
        for i in name_list:
            result.append(i+end_4)                  ###   全称+手机尾号4
        for i in name_list:
            result.append(i+end_6)                  ###   全称+手机尾号6
        for i in name_list:
            result.append(i+center_4)                ###   全称+手机中间4位
        for i in name_list:
            result.append(i+start_3)
        self.write_file(result)   ###初始写入文件
        for i in result:
            for j in char_:
                self.write_file(i+j)  ##加入特殊符号
    def By_Idnunmber(self):
        char_ = ['.','!','_','@','#',',']
        words = ''
        start_3 = self.phoneNumber[:3]
        end_4 = self.phoneNumber[-4:]
        res = []
        for i in range(0, len(self.Name), 1):
            if str(i) in self.special_position:
                words = words + self.Name[i]
        words = list(words)
        self.By_name_helper(words, 0, res)

        self.write_file('QQ'+self.idNumber)
        self.write_file('qq'+self.idNumber)
        next = []
        for i in res:
            self.write_file(i+self.idNumber) #名字+id号
            next.append(i+self.idNumber)
        for i in res:
            self.write_file(i+i+self.idNumber) #名字双写简写+ID号
            next.append(i + self.idNumber)
        for i in next:
            for j in char_:
                self.write_file(i+j)  ##名字+id号+特殊符号
        name_list = []
        for j in res:
            name = self.Name
            for i in range(0,len(self.special_position),1):
                name = list(name)
                name[int(self.special_position[i])]=j[i]
            name_list.append(''.join(name))
        for i in name_list:
            self.write_file(i+start_3)
        for i in name_list:
            self.write_file(i+end_4)
        print('name_list',name_list)
    def push_name_list(self,name_list):
        words = ''
        res = []
        for i in range(0, len(self.Name), 1):
            if str(i) in self.special_position:
                words = words + self.Name[i]
        words = list(words)
        self.By_name_helper(words, 0, res)
        for j in res:
            name = self.Name
            for i in range(0, len(self.special_position), 1):
                name = list(name)
                name[int(self.special_position[i])] = j[i]
            name_list.append(''.join(name))
        name_list.extend([x for x in res])

    # -》姓名生成    #必填项: 姓名、关键位
    # 姓名中存在flag—position,进行排列组合
    def By_name(self):
        words = ''
        """
        base_pw ：字典
        num_pw : 数字字典
        res : 关键字列表
        char_ : 字符列表
        name_list : 关键字替换名称后的字典
        """
        res = []
        name_list = []
        char_ = self.read_file('../Hack_pw_dict/old_char.txt','r')
        base_pw = self.read_file ('../Hack_pw_dict/base_pw.txt','r')
        short_num_pw = self.read_file('../Hack_pw_dict/short_pw.txt','r')
        long_num_pw = self.read_file('../Hack_pw_dict/long_pw.txt','r')
        for i in range(0,len(self.Name),1):
            if  str(i) in self.special_position:
                words = words+self.Name[i]
        print(words)
        words=list(words)

        self.By_name_helper(words,0,res)
        print(res)
        self.short_name = res
        print(base_pw)

        for j in res:
            name = self.Name
            for i in range(0,len(self.special_position),1):
                name = list(name)
                name[int(self.special_position[i])]=j[i]
            name_list.append(''.join(name))
        print(short_num_pw)
        self.write_file(name_list)        #名称
        self.Name_list_all.extend([x for x in name_list])
        self.Name_list_all.extend([x for x in res])

        self.write_file(base_pw)              #base——password

        #使用姓名全称进行拼接:
        #此时拼接使用数字3位
        #当收集到更多信息时进行组合拼接
        for i in name_list:
            for j in short_num_pw:
                self.write_file(i+j)        #名称+短数字

        if len(self.Name)<=7:
            x = []
            for i in name_list:
                for j in name_list:
                    for k in short_num_pw:
                        self.write_file(i+j+k)      ###名称双拼加拼接+短数字
                        x.append(i+j+k)
            x1 = []
            for i in x:
                for j in char_:
                  x1.append(i+j)
            #print('名称双拼加拼接+短数字',len(x1),x1)
            self.write_file(x1)     #名称双拼加拼接+短数字+字符
        else:
            b=[]
            for j in res:
                for i in name_list:
                    b.append(j+i)
            self.write_file(b)       #简写+全称
            for i in b:
                for j in char_:
                    self.write_file(i+j)               #  简写+全称+特殊字符
            next = []
            for i in res:
                next.append(i)
            next.extend([x for x in name_list])
            for i in next:
                for j in base_pw:
                    self.write_file(i+j)
        ##将名字全称加入特殊字符
        # for i in a:
        #     for j in char_:
        #         self.write_file(i+j)
        a=[]
        #使用关键位进行拼接
        for i in res:
            for j in base_pw:
               #print(i+j)
               a.append(i+j)
        print(a)
        print(len(a))
        self.write_file(a)   #简写+base
        for i in res:
            for j in long_num_pw:
                self.write_file(i+j)
        print(res)
        print(name_list)
    def write_file(self,list_dict):
        #print(type(list_dict))
        if type(list_dict)==list:
            #print('write_file',list_dict)
            for i in list_dict:
                self.path.write(i+'\n')
        elif type(list_dict)==str:
            #print('write_file',list_dict)
            self.path.write(list_dict+'\n')
    def read_file(self,file_path,method):
        result = []
        fo = open(file_path,method)
        push_ = fo.readline()
        while push_:
            push_ = push_.replace('\n','')
            result.append(push_)
            push_ = fo.readline()
        fo.close()
        return result
    def By_name_helper(self,S,i,res):
        if i>=len(S):
            res.append("".join(S))
            return
        c=ord(S[i])
        if c>=65 and c<=90 :
            self.By_name_helper(S,i+1,res)
            S[i]=S[i].lower()
            self.By_name_helper(S,i+1,res)
        elif c>=97 and c<=122:
            self.By_name_helper(S,i+1,res)
            S[i]=S[i].upper()
            self.By_name_helper(S,i+1,res)
        else:
            self.By_name_helper(S,i+1,res)
if __name__ == '__main__':
     a = hack_password(Name='姓名:如：李明 LiMing(首字母大写)',phoneNumber="手机号"
                       ,email='@qq.com',IDCard="身份证号",idnumber='QQ号或任意号',Birth_Day='出生年月日:19971023')
     a.run()