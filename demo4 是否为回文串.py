# 作者：宁方笑
# 开发时间：2021/3/5 19:11
def isPalomstr(s):
    n=int(len(s))
    flag=0
    if n%2==0:  #n是偶数
        for i in range(int(n/2)):
            if s[i]==s[n-i-1]:
                flag=flag+1
        if flag==n/2:
            print("True")
        else:
            print("False")
    else:
        for i in range(int((n+1)/2-1)):
            if s[i]==s[n-i-1]:
                flag=flag+1
        if flag==(n+1)/2-1:
            print("True")
        else:
            print("False")

s="fjnfkfbfeuujctmyttwidcrdjtkfoaylsceqqzzmkpyvljkwcxxtmxiwkrgoahxztuppnvxhyionhpakvjoizdzcqxuyaidjadrhfhuhbncijokbthvuigjytipgygnonhgkpvsqimxpslmptieumhunjlafttjstaxnivrpqcxrgocvaicpwfnmtkgbjnbfopxaiduqihomrdmhzzyzddytiqdjzmmqwmeyoqnttmiujobihdifkbntpphjhgxzbjpulnokvceohloltyosddbopgkllcxzzkfzmkywxlpkdjlorgorxzownuajjzcxuhyqexfklssbtralzlvdbtxapccipvvgjtusfsanvnyehpkwirygqogtsicwycgnajwekuzffhlsvfgqwpbuinwhvpqxjhamhxayicchmxmurakhzhoghnupohaqanduhjkegggpyetwebcjgavpspfjaoakjkktaxwehpyqvsczhbbhzcsvqyphewxatkkjkaoajfpspvagjcbewteypgggekjhudnaqahopunhgohzhkarumxmhcciyaxhmahjxqpvhwniubpwqgfvslhffzukewjangcywcistgoqgyriwkpheynvnasfsutjgvvpiccpaxtbdvlzlartbsslkfxeqyhuxczjjaunwozxrogroljdkplxwykmzfkzzxcllkgpobddsoytlolhoecvkonlupjbzxghjhpptnbkfidhibojuimttnqoyemwqmmzjdqityddzyzzhmdrmohiqudiaxpofbnjbgktmnfwpciavcogrxcqprvinxatsjttfaljnuhmueitpmlspxmiqsvpkghnongygpityjgiuvhtbkojicnbhuhfhrdajdiayuxqczdziojvkaphnoiyhxvnpputzxhaogrkwixmtxxcwkjlvypkmzzqqecslyaofktjdrcdiwttymtcjuuefbfkfnjf"
isPalomstr(s)