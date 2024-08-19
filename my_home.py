'''我的主页'''
import streamlit as st
from PIL import Image
page = st.sidebar.radio("我的首页", ["我的兴趣推荐", "我的图片处理工具", "我的智慧词典", "我的留言区"])

#def img_change(img, rc, gc, bc):
    #'''图片处理'''
    #width, height = img.size
    #img_array = img.load()
    #for x in range(width):
        #for y in range(height):
            #r = img_array[x,y][rc]
            #g = img_array[x,y][gc]
            #b = img_array[x,y][bc]
            #img_array[x,y] = (r,g,b)
    #return img

def img_change_ch(img):
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            # 获取RGB值，反色处理
            r = 255 - img_array[x, y][0]
            g = 255 - img_array[x, y][1]
            b = 255 - img_array[x, y][2]
            img_array[x, y] = (r, g, b)
    return img

def img_change_co(img):
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            # 获取RGB值
            r = img_array[x, y][0]
            g = img_array[x, y][1]
            b = img_array[x, y][2]
            # RGB值中，哪个更大，就再大一些
            if r == max(r, g, b):
                if r >= 200:
                    r = 255
                else:
                    r += 55
            elif g == max(r, g, b):
                if g >= 200:
                    g = 255
                else:
                    g += 55
            else:
                if b >= 200:
                    b = 255
                else:
                    b += 55
            img_array[x, y] = (r, g, b)
    return img

def img_change_bw(img):
    img = img.convert('L') # 转换为灰度图
    return img

def page_1():
    """我的主页"""
    with open("Lyn - Life Will Change.ogg", "rb") as f:
        backgroundmusic = f.read()
    st.audio(backgroundmusic, format="audio/ogg", start_time=0)
    st.image("Persona5.jpeg")
    st.write("我的游戏推荐")
    #col1, col2, col3 = st.columns([1, 2, 2])with col1:
    st.text("《女神异闻录5》")
    st.image("P5介绍1.png")
    st.image("P5介绍2.png")
    st.image("P5介绍3.png")
    st.text("白天是普通的学生，享受丰富的校园活动夜晚化身怪盗")
    st.text("目标是那些欲望扭曲的堕落者们，通关他们的宫殿， 偷走他们的密宝，让他们悔改吧")
    st.text("为弱者夺回被偷走的世界！")
    #with col2:
    #st.text("《无畏契约》")
    st.write("----")
    st.write("我的书籍推荐")
    st.text("《诡秘之主》")
    st.image("诡秘之主.jpeg")
    st.text("蒸汽与机械的浪潮中，谁能触及非凡。历史和黑暗的迷雾里，又是谁在耳语。")
    st.text("我从诡秘中醒来，睁眼看见这个世界：枪械，大炮，巨舰，飞空艇，差分机；魔药，占卜，诅咒，倒吊人，封印物……光明依旧照耀，神秘从未远离，这是一段“愚者”的传说。") 
    st.text("黑铁纪元，七位正统神灵与四大国统治着北大陆。蒸汽与机械的浪潮中，工业化社会迅速发展成形，而在看似平静繁荣的表面下，则是一个神秘扭曲，乃至疯狂的非凡世界。")
    
def page_2():
    '''我的图片处理工具'''
    st.write(":sunglasses:图片处理小程序:sunglasses:")
    uploaded_file = st.file_uploader("上传图片", type=["png", "jpeg", "jpg"])
    if uploaded_file:
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        #st.image(img)
        #st.image(img_change(img, 0, 2, 1))
        
        #tab1, tab2, tab3, tab4 = st.tabs["原图", "改色1", "改色2", "改色3"]
        #with tab1:
         #       st.image(img)
        #with tab2:
         #       st.image(img_change(img, 2, 0, 1))
        #with tab3:
         #       st.image(img_change(img, 2, 1, 0))
        #with tab4:
         #       st.image(img_change(img, 1, 2, 0))
        col1, col2, col3 = st.columns([3, 2, 4])
        with col1:
            st.image(img)
        with col2:
            ch = st.toggle('反色滤镜')
            co = st.toggle('增强对比度')
            bw = st.toggle('黑白滤镜')
        with col3:
            st.write('对图片进行反色处理')
            st.write('让图片颜色更加鲜艳')
            st.write('将图片变为灰度图')
        # 点击按钮处理图片
        b = st.button('开始处理')
        if b:
            if ch:
                img = img_change_ch(img)
            if co:
                img = img_change_co(img)
            if bw:
                img = img_change_bw(img)
            st.write('右键"另存为"保存图片')
            st.image(img)

    
def page_3():
    '''我的智慧词典'''
    st.write("智慧词典")
    with open("words_space.txt", "r", encoding="utf-8") as f:
        words_list = f.read().split("\n")

    for i in range(len(words_list)):
        words_list[i] = words_list[i].split("#")

    words_dict = {}
    for i in words_list:
        words_dict[i[1]] = [int(i[0]), i[2]]

    with open("check_out_times.txt","r",encoding="utf-8") as f:
        times_list = f.read().split('\n')

    for i in range(len(times_list)):
        times_list[i] = times_list[i].split("#")
        
    times_dict = {}
    for i in times_list:
        times_dict[int(i[0])]= int(i[1])

    word = st.text_input("请输入想要查询的单词：")

    if word in words_dict:
        cixing, ciyi = words_dict[word][1].split('.')
        st.write('单词的意思是：', ciyi)
        #st.text('单词的词性是：' + cixing + '.')
        st.text('这是词典中的第' + str(words_dict[word][0]) + '个单词')
        #st.write(words_dict[word])
        n = words_dict[word][0]
        if n in times_dict:
            times_dict[n] += 1
        else:
            times_dict[n] = 1
        with open("check_out_times.txt", "w", encoding="utf-8") as f:
            message = ""
            for k, v in times_dict.items():
                message += str(k) + "#" + str(v) + "\n"
            message = message[:-1]
            f.write(message)
        st.write("查询次数：", times_dict[n])
        if word == "python":
            st.code("""
                    # 恭喜你触发彩蛋，这是一行Python代码
                    print("hello world")""")
        elif word == "snow" or word == "winter":
            st.snow()
        elif word == "birthday":
            st.balloons()
    elif word == "persona":
        st.write("偏铝酸钠！")

def page_4():
    '''我的留言区'''
    st.write("我的留言区")
    with open("leave_messages.txt", "r", encoding="utf-8") as f:
        messages_list = f.read().split("\n")
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split("#")
    for i in messages_list:
        if i[1] == "阿短":
            with st.chat_message("🌞"):
                st.write(i[1], ":", i[2])
        elif i[1] == "编程猫":
            with st.chat_message("🍥"):
                st.write(i[1], ":", i[2])
    name = st.selectbox("我是...", ["阿短", "编程猫", "一个路过的假面骑士", "怪盗", "凉厨", st.text_input("你的身份(如已有请无视)")])
    new_message = st.text_input("想要说的话：")
    if st.button("留言"):
        messages_list.append([str(int(messages_list[-1][0])+1), name, new_message])
        with open("leave_messages.txt", "w", encoding="utf-8") as f:
            message = ""
            for i in messages_list:
                message += i[0] + "#" + i[1] + "#" + i[2] + "\n"
            message = message[:-1]
            f.write(message)

if page == "我的兴趣推荐" :
    page_1()
elif page == "我的图片处理工具" :
    page_2()
elif page == "我的智慧词典" :
    page_3()
elif page == "我的留言区" :
    page_4()